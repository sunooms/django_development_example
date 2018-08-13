# ʹ��pycharm��django���п���ʵ��

[toc]
## mysql��windows�µİ�װ
### mysql������
    https://dev.mysql.com/downloads/mysql/
    ֱ��ѡ��Ҫע�ᣬֱ�����أ�No thanks, just start my download.��

### ����my.ini
    ע�� �������mysql��װ·���ڣ�E:\xgm\software\mysql-8.0.12-winx64Ŀ¼
    ��E:\xgm\software\mysql-8.0.12-winx64Ŀ¼����my.ini�����ļ�
    ��E:\xgm\software\mysql-8.0.12-winx64Ŀ¼�½�dataĿ¼��������mysql����

    ע�� my.ini�����ļ��·����2����б��"\\"

```
[client]
# ����mysql�ͻ������ӷ����ʱĬ��ʹ�õĶ˿�
port=3306
default-character-set=utf8

[mysqld]
lower_case_table_names=1
# �����±�ʱ��ʹ�õ�Ĭ�ϴ洢����
default-storage-engine=INNODB
# �����ʹ�õ��ַ���Ĭ��ΪUTF8
character-set-server=utf8
# ����mysql�İ�װĿ¼
# �мǴ˴�һ��Ҫ��˫б��\\����б�������������������˵Ľ̳̣��е��ǵ�б�ܡ��Լ�����
basedir=E:\\xgm\\software\\mysql-8.0.12-winx64
# ����mysql���ݿ�����ݵĴ��Ŀ¼
# �мǴ˴�һ��Ҫ��˫б��\\����б�������������������˵Ľ̳̣��е��ǵ�б�ܡ��Լ�����
datadir=E:\\xgm\\software\\mysql-8.0.12-winx64\\data
# ����3306�˿�
port=3306
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES 
# Ĭ��ʹ�á�mysql_native_password�������֤
default_authentication_plugin=mysql_native_password
# �������������
max_connections=200
# ��������ʧ�ܵĴ���������Ϊ�˷�ֹ���˴Ӹ�������ͼ�������ݿ�ϵͳ
max_connect_errors=10

[mysql]
# ����mysql�ͻ���Ĭ���ַ���
default-character-set=utf8
```

### ����ϵͳ�����Լ�path
    ����ϵͳ������ MYSQL_HOME = E:\xgm\software\mysql-8.0.12-winx64
    PATH�����%MYSQL_HOME%\bin·��

###  �Թ���Ա��ݴ�cmd����
#### ��ʼ��
  һ��Ҫ���г�ʼ�����ܶ��˲����г�ʼ�����ͳ�����1067����
  ��ʼ�����֮�󣬻�����һ����ʱ����������Ҫע�����ʱ�����ס
```
1  mysqld --initialize --user=mysql --console
    �����ɳ�ʼĬ�����룺cqt>;fuqu2lP
    Ҫ�����ּ����ؿ��ˣ�����û��ס����Ҳû�£�ɾ����ʼ���� datadir Ŀ¼����ִ��һ���ʼ������ֻ��������ɵġ���Ȼ��Ҳ����ʹ�ð�ȫ���ߣ�ǿ�Ƹ����룬��ʲô����������
2 ��װ����
    mysqld -install MYSQL8.0.12
3 ��������
    net start MYSQL8.0.12
4 ��¼���ݿ⣬��Ҫ����
    mysql -uroot -p   
5 �޸����ݿ�����
    alter user root@localhost identified by '123456'
    flush privileges;

    ��ע��8.0֮ǰ�汾�����������޸ķ���
        �ҵ�binĿ¼��mysqld --skip-grant-tables
        �����ڿ�һ��cmd����
        �ҵ�binĿ¼��mysql�ͽ����½״̬��
        5.7.22�޸�������䣺update user set authentication_string=password('123456') where user='root' and host='localhost';
        5.6.�޸�������䣺update user set password=password('123456') where user='root' and host='localhost';  (��û��ʵ��������϶�����ôд��)
```

### ��װmysql-python
  Ĭ����û�а�װ��
```
python -m pip install mysql-python
```
  ��װ����"Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27"
  ��΢�����վ���������https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
  ��װVCForPython27.msi
  
  ��ʱ����python -m pip install mysql-python����Ǳ���������վ����64λ��mysql-python����
  http://www.codegood.com/archives/129
  ���أ� http://www.codegood.com/download/11/MySQL-python-1.2.3.win-amd64-py2.7.exe
  ��װMySQL-python-1.2.3.win-amd64-py2.7.exe


## pycharm����ҵ�棩�½�django����
  >file-->new project-->django-->������Ŀ����(django_mysql)

```
1 mkdir /test/djangotest
2 django-admin startproject django_mysql
```

### ����mysql���ݿ�
    ��/django_mysql/settings.py�ļ����ҵ�DATABASES� Ĭ����sqlite3
    �������Ϊmysql���ݿ�
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test03', #���ݿ����֣�
        'USER': 'root', #���ݿ��¼�û���
        'PASSWORD': '123456', #���ݿ��¼����,���Լ��޸���
        'HOST': 'localhost', #���ݿ�������������˾��д��ʵ������ַ��
        'PORT': '3306', #���ݿ�˿�
    }
```

  ע�� settings.py�ļ���ͷҪȷ��utf8��ʽ�� # -*- coding: utf-8 -*-

### �ֹ�����mysql���ݿ�
    �����նˣ��������е�¼mysql���������ݿ�test03��
 create database test03 charset=utf8;


## �½�django��appӦ��booktest
  ��pycharm��terminal�� ����ù��̵�Ŀ¼���¼�һ��django����
  python manage.py startapp booktest

### �޸�settings.py�ļ���ע��ù���

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

Django�Ŀ�����ѭMTVģʽ��models, templates, views����views.py����ִ�в�����models.py�������ݴ��������ݿ����ӣ���templatesĿ¼�´����ҳ��ģ��


### ����ģ����
    ģ���౻�����ڡ�Ӧ��/models.py���ļ��У�������Ϊ��booktest/models.py���ļ���
    ģ�������̳���Model�࣬λ�ڰ�django.db.models�С�
    ������Ҫ����ʹ���߼�ɾ����

#### ����ģ��models.py����
```
#����ͼ��ģ����BookInfo
class BookInfo(models.Model):
    #ͼ�����ƣ� Ψһ
    btitle = models.CharField(max_length=50, unique=true)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    idDelete = models.BooleanField(default=false)

#����Ӣ��ģ����HeroInfo
class HeroInfo(Models.Model):
    #Ӣ����������Ψһ��������������Ӣ��
    hname = models.CharField(max_length=50, unique=False)
    #Ӣ���Ա�Ĭ��False�����ԣ�Ҳ��������Ϊinteger���� 0����1
    hgender = models.BooleanField(default=False);
    isDelete = models.BooleanField(default=False);
    #Ӣ�۵�����
    hcontent = models.CharField(max_length=500);
    #ͼ���Ӣ�۵Ĺ�ϵ��һ�Զ�Ĺ�ϵ���������ڶ�����Ӣ�۵�ģ������
    hbook = models.ForeignKey('BookInfo');
```

### Ǩ��
```
python manage.py makemigrations
```
#### ִ��Ǩ��
```
python manage.py migrate
```
#### �����ݿ������У��鿴test03���ݿ�����б�
  ��booktest_bookinfo�ṹ���£�desc booktest_bookinfo;

  ��booktest_heroinfo�ṹ���£�desc booktest_heroinfo;

### �����������ݿ�
   �����ݿ��������У������������ִ�У���booktest_bookinfo�����������ݣ�
```
insert into booktest_bookinfo(btitle,bpub_date,bread,bcomment,isDelete) values
('���Ӣ�۴�','1980-5-1',12,34,0),
('�����˲�','1986-7-24',36,40,0),
('Ц������','1995-12-24',20,80,0),
('ѩɽ�ɺ�','1987-11-11',58,24,0);

```
    ִ��������䣬 ��booktest_heroinfo�����������ݣ�
```
insert into booktest_heroinfo(hname,hgender,hbook_id,hcontent,isDelete) values
('����',1,1,'����ʮ����',0),
('����',0,1,'�򹷹���',0),
('��ҩʦ',1,1,'��ָ��ͨ',0),
('ŷ����',1,1,'��󡹦',0),
('÷����',0,1,'�����׹�צ',0),
('�Ƿ�',1,2,'����ʮ����',0),
('����',1,2,'������',0),
('����',1,2,'��ɽ������',0),
('������',0,2,'���ɽ��',0),
('�����',1,3,'���¾Ž�',0),
('��ӯӯ',0,3,'����',0),
('����Ⱥ',1,3,'��ɽ����',0),
('��������',0,3,'��������',0),
('���',1,4,'���ҵ���',0),
('������',0,4,'����',0),
('������',0,4,'ҽ��',0),
('Ԭ����',0,4,'����ȭ',0);
```

### ������ͼ
    ��booktest/views.py�ļ���������ͼ�������£�
```
from datetime import date
from django.shortcuts import render,redirect
from booktest.models import BookInfo

# ��ѯ����ͼ�鲢��ʾ����ͼ����
def index(request):
    books=BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

# ����ͼ����ͼ��ͼ����
def addBook(request):
    book=BookInfo()
    book.btitle='�����Դ�'
    book.bpub_date=date(2017,6,27)
    book.save()
    # return HttpResponse('ok') 
    # �ض�����ת����ҳ
    return redirect('/index/')

# ����ͼ��idɾ��һ�������ͼ����
def delBook(request,bid):
    # ��ѯ��ͼ��
    b=BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index/')

```

### ����url
   ��test03/urls.py�ļ�������url���£�
```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # ���óɹ�֮��ȥbooktest��urls�ļ����Ҷ�Ӧ����ͼ����
    url(r'^',include('booktest.urls'))
]
```

   ��booktestӦ���´���url.py, �������£�
```
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/$',views.delBook)
]
```

### ����ģ��
   ��test03/settings.py������ģ�����Ŀ¼TEMPLATES��DIRS.
```
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
    ��booktestĿ¼����ģ��Ŀ¼��templates
    ��booktest/templates/booktest/Ŀ¼�½���ģ���ļ�index.html(���booktestĿ¼�����ڣ��ͽ���֮)���������£�
```
<html>
<head>
    <title>Python-���ɵ�ͼ����վ</title>
</head>
<body>
<a href="/addBook/">����</a>
<ul>
{%for book in books%}

<li>{{book.btitle}}--<a href="/delBook{{book.id}}/">ɾ��</a></li>

{%endfor%}
</ul>
</body>
</html>
```