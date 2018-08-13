# 使用pycharm和django进行开发实例

[toc]
## mysql在windows下的安装
### mysql的下载
    https://dev.mysql.com/downloads/mysql/
    直接选择不要注册，直接下载（No thanks, just start my download.）

### 配置my.ini
    注： 这里假设mysql安装路径在：E:\xgm\software\mysql-8.0.12-winx64目录
    在E:\xgm\software\mysql-8.0.12-winx64目录增加my.ini配置文件
    在E:\xgm\software\mysql-8.0.12-winx64目录新建data目录，这里存放mysql数据

    注： my.ini配置文件里，路径用2个反斜杠"\\"

```
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8

[mysqld]
lower_case_table_names=1
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 服务端使用的字符集默认为UTF8
character-set-server=utf8
# 设置mysql的安装目录
# 切记此处一定要用双斜杠\\，单斜杠这里会出错，不过看别人的教程，有的是单斜杠。自己尝试
basedir=E:\\xgm\\software\\mysql-8.0.12-winx64
# 设置mysql数据库的数据的存放目录
# 切记此处一定要用双斜杠\\，单斜杠这里会出错，不过看别人的教程，有的是单斜杠。自己尝试
datadir=E:\\xgm\\software\\mysql-8.0.12-winx64\\data
# 设置3306端口
port=3306
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES 
# 默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10

[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
```

### 配置系统变量以及path
    增加系统变量： MYSQL_HOME = E:\xgm\software\mysql-8.0.12-winx64
    PATH中添加%MYSQL_HOME%\bin路径

###  以管理员身份打开cmd窗口
#### 初始化
  一定要进行初始化，很多人不进行初始化，就出现了1067错误
  初始化完成之后，会生成一个临时密码这里需要注意把临时密码记住
```
1  mysqld --initialize --user=mysql --console
    会生成初始默认密码：cqt>;fuqu2lP
    要是你手贱，关快了，或者没记住，那也没事，删掉初始化的 datadir 目录，再执行一遍初始化命令，又会重新生成的。当然，也可以使用安全工具，强制改密码，用什么方法，随意
2 安装服务：
    mysqld -install MYSQL8.0.12
3 启动服务：
    net start MYSQL8.0.12
4 登录数据库，需要密码
    mysql -uroot -p   
5 修改数据库密码
    alter user root@localhost identified by '123456'
    flush privileges;

    备注：8.0之前版本，忘记密码修改方法
        找到bin目录：mysqld --skip-grant-tables
        重新在开一个cmd窗口
        找到bin目录：mysql就进入登陆状态了
        5.7.22修改密码语句：update user set authentication_string=password('123456') where user='root' and host='localhost';
        5.6.修改密码语句：update user set password=password('123456') where user='root' and host='localhost';  (我没有实验过，网上都是这么写的)
```

### 安装mysql-python
  默认是没有安装的
```
python -m pip install mysql-python
```
  安装出错："Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27"
  到微软的网站下载软件：https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
  安装VCForPython27.msi
  
  此时运行python -m pip install mysql-python命令还是报错，到此网站下载64位的mysql-python包：
  http://www.codegood.com/archives/129
  下载： http://www.codegood.com/download/11/MySQL-python-1.2.3.win-amd64-py2.7.exe
  安装MySQL-python-1.2.3.win-amd64-py2.7.exe


## pycharm（企业版）新建django工程
  >file-->new project-->django-->输入项目名称(django_mysql)

```
1 mkdir /test/djangotest
2 django-admin startproject django_mysql
```

### 关联mysql数据库
    打开/django_mysql/settings.py文件，找到DATABASES项， 默认是sqlite3
    将引擎改为mysql数据库
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test03', #数据库名字，
        'USER': 'root', #数据库登录用户名
        'PASSWORD': '123456', #数据库登录密码,我自己修改了
        'HOST': 'localhost', #数据库所在主机（公司中写真实主机地址）
        'PORT': '3306', #数据库端口
    }
```

  注： settings.py文件开头要确保utf8格式： # -*- coding: utf-8 -*-

### 手工创建mysql数据库
    打开新终端，在命令行登录mysql，创建数据库test03。
 create database test03 charset=utf8;


## 新建django的app应用booktest
  打开pycharm的terminal， 进入该工程的目录，新见一个django工程
  python manage.py startapp booktest

### 修改settings.py文件，注册该工程

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jdango_web'
]
```

Django的开发遵循MTV模式（models, templates, views），views.py负责执行操作，models.py负责数据处理（如数据库连接），templates目录下存放网页的模板


### 定义模型类
    模型类被定义在“应用/models.py”文件中，此例中为“booktest/models.py”文件。
    模型类必须继承自Model类，位于包django.db.models中。
    对于重要数据使用逻辑删除。

#### 具体模型models.py代码
```
#定义图书模型类BookInfo
class BookInfo(models.Model):
    #图书名称， 唯一
    btitle = models.CharField(max_length=50, unique=true)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    idDelete = models.BooleanField(default=false)

#定义英雄模型类HeroInfo
class HeroInfo(Models.Model):
    #英雄姓名，不唯一，可以有重名的英雄
    hname = models.CharField(max_length=50, unique=False)
    #英雄性别，默认False是男性，也可以设置为integer类型 0或者1
    hgender = models.BooleanField(default=False);
    isDelete = models.BooleanField(default=False);
    #英雄的描述
    hcontent = models.CharField(max_length=500);
    #图书和英雄的关系是一对多的关系，所有属于定义在英雄的模型类中
    hbook = models.ForeignKey('BookInfo');
```

### 迁移
```
python manage.py makemigrations
```
#### 执行迁移
```
python manage.py migrate
```
#### 打开数据库命令行，查看test03数据库的所有表
  表booktest_bookinfo结构如下：desc booktest_bookinfo;

  表booktest_heroinfo结构如下：desc booktest_heroinfo;

### 建立测试数据库
   在数据库命令行中，复制如下语句执行，向booktest_bookinfo表插入测试数据：
```
insert into booktest_bookinfo(btitle,bpub_date,bread,bcomment,isDelete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);

```
    执行如下语句， 向booktest_heroinfo表插入测试数据：
```
insert into booktest_heroinfo(hname,hgender,hbook_id,hcontent,isDelete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);
```

### 定义视图
    打开booktest/views.py文件，定义视图代码如下：
```
from datetime import date
from django.shortcuts import render,redirect
from booktest.models import BookInfo

# 查询所有图书并显示的视图函数
def index(request):
    books=BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

# 新增图书视图视图函数
def addBook(request):
    book=BookInfo()
    book.btitle='晓可自传'
    book.bpub_date=date(2017,6,27)
    book.save()
    # return HttpResponse('ok') 
    # 重定向跳转到首页
    return redirect('/index/')

# 根据图书id删除一本书的视图函数
def delBook(request,bid):
    # 查询出图书
    b=BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index/')

```

### 配置url
   打开test03/urls.py文件，配置url如下：
```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 配置成功之后去booktest的urls文件中找对应的视图函数
    url(r'^',include('booktest.urls'))
]
```

   在booktest应用下创建url.py, 代码如下：
```
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/$',views.delBook)
]
```

### 创建模板
   打开test03/settings.py，配置模板查找目录TEMPLATES的DIRS.
```
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
    在booktest目录创建模板目录：templates
    在booktest/templates/booktest/目录下建立模板文件index.html(如果booktest目录不存在，就建立之)，代码如下：
```
<html>
<head>
    <title>Python-晓可的图书网站</title>
</head>
<body>
<a href="/addBook/">创建</a>
<ul>
{%for book in books%}

<li>{{book.btitle}}--<a href="/delBook{{book.id}}/">删除</a></li>

{%endfor%}
</ul>
</body>
</html>
```