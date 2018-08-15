## 备份原数据库
    由于是对测试环境的数据库进行升级，数据量不多，我直接导出需要迁移的数据库的数据到sql文件里。
```
mysqldump  -uroot  -p  --database database_name >name.sql
```

## 卸载老的mariadb5.5
```
卸载mariadb
yum remove mariadb

删除配置文件
rm -f /etc/my.cnf

删除数据目录
rm -rf /var/lib/mysql/
```

## 添加mariadb 10.3的国内源
```
vim /etc/yum.repos.d/Mariadb.repo
```
添加如下内容：
```
[mariadb]
name = MariaDB
baseurl = http://mirrors.aliyun.com/mariadb/yum/10.3/centos7-amd64/
gpgkey =  http://mirrors.aliyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck = 1
```

  清除yum源缓存数据
```
yum clean all
yum makecache all
```

## mariadb 10.3的安装
```
yum install MariaDB-server MariaDB-client -y
```
启动并添加开机自启
```
systemctl start mariadb #启动服务
systemctl enable mariadb #设置开机启动
systemctl restart mariadb #重新启动
systemctl stop mariadb.service #停止MariaDB
```
## mariadb的初始化
此时mariadb的初始化密码为空，配置mariadb的密码
```
/usr/bin/mysql_secure_installation
```
一般按照提示设置密码
```
Enter current password for root (enter for none): Just press the Enter button
Set root password? [Y/n]: Y
New password: your-MariaDB-root-password
Re-enter new password: your-MariaDB-root-password
Remove anonymous users? [Y/n]: Y
Disallow root login remotely? [Y/n]: n
Remove test database and access to it? [Y/n]: Y
Reload privilege tables now? [Y/n]: Y
```

设置mariadb的字符集
```
文件/etc/my.cnf

vi /etc/my.cnf
在[mysqld]标签下添加
[mysqld]
init_connect='SET collation_connection = utf8_unicode_ci' 
init_connect='SET NAMES utf8' 
character-set-server=utf8 
collation-server=utf8_unicode_ci 
skip-character-set-client-handshake
文件/etc/my.cnf.d/client.cnf

vi /etc/my.cnf.d/client.cnf
在[client]中添加

default-character-set=utf8
文件/etc/my.cnf.d/mysql-clients.cnf

vi /etc/my.cnf.d/mysql-clients.cnf
在[mysql]中添加

default-character-set=utf8
 全部配置完成，重启mariadb

 systemctl restart mariadb
```

之后进入MariaDB查看字符集
```
mysql> show variables like "%character%";show variables like "%collation%";

MariaDB [(none)]>  show variables like "%character%";show variables like "%collation%";
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.001 sec)

+----------------------+-----------------+
| Variable_name        | Value           |
+----------------------+-----------------+
| collation_connection | utf8_unicode_ci |
| collation_database   | utf8_unicode_ci |
| collation_server     | utf8_unicode_ci |
+----------------------+-----------------+
3 rows in set (0.001 sec)
```

## 修改配置文件mysql-clients.cnf my.cnf供参考

修改配置文件/etc/my.cnf.d/mysql-clients.cnf，重点是[client]，其他的可以参考
```
[client]
port        = 3307
socket      = /var/data/db/mariadb/mysql.sock
 
[mysql]
no-auto-rehash
 
[mysqldump]
quick
max_allowed_packet = 64M
 
[myisamchk]
key_buffer_size = 128M
sort_buffer_size = 128M
read_buffer = 2M
write_buffer = 2M
 
[mysqlhotcopy]
interactive-timeout
```

修改配置文件/etc/my.cnf.d/server.cnf，这里的性能参数来自my-large.ini文件
```
[mysqld]
port            = 3307
datadir         = /var/data/db/mariadb
socket          = /var/data/db/mariadb/mysql.sock
skip-external-locking
key_buffer_size = 256M
max_allowed_packet = 64M
table_open_cache = 256
sort_buffer_size = 1M
read_buffer_size = 1M
read_rnd_buffer_size = 4M
myisam_sort_buffer_size = 64M
thread_cache_size = 8
query_cache_size= 16M
thread_concurrency = 8
log-bin=mysql-bin
binlog_format=mixed
server-id   = 1
```

## 添加用户，设置权限

```
创建用户命令

mysql>create user username@localhost identified by 'password';
直接创建用户并授权的命令

mysql>grant all on *.* to username@localhost indentified by 'password';
授予外网登陆权限 

mysql>grant all privileges on *.* to username@'%' identified by 'password';
授予权限并且可以授权

mysql>grant all privileges on *.* to username@'hostname' identified by 'password' with grant option;
简单的用户和权限配置基本就这样了。

其中只授予部分权限把 其中 all privileges或者all改为select,insert,update,delete,create,drop,index,alter,grant,references,reload,shutdown,process,file其中一部分。
```
