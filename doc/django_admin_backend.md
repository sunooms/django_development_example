# 使用django进行后台管理开发实例

[toc]

## pycharm（企业版）新建django工程
  >file-->new project-->django-->输入项目名称(django_admin_backend)

```
1 mkdir /test/django_admin_backend
2 django-admin startproject django_admin_backend
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
        'PASSWORD': '123456', #数据库登录密码
        'HOST': 'localhost', #数据库所在主机
        'PORT': '3306', #数据库端口
    }
```

  注： settings.py文件开头要确保utf8格式： # -*- coding: utf-8 -*-


### 手工创建mysql数据库
    打开新终端，在命令行登录mysql，创建数据库test03。
 create database test03 charset=utf8;


## 新建django的app应用booktest
  打开pycharm的terminal， 进入该工程的目录，新建一个django工程
```
python manage.py startapp booktest
```

### 修改settings.py文件，注册该工程

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest'
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
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False)

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
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





### 后台管理的步骤
    >1 管理界面本地化
    >2 创建管理员
    >3 注册模型类
    >4 自定义管理页面

### 管理界面本地化
    本地化是将显示的语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用简体中文，时区使用亚洲/上海时区，注意这里不使用北京时区表示。

    打开django_admin_backend/settings.py文件，找到语言编码、时区的设置项，将内容改为如下：
```
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 原来django中的语言和时间配置
#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'

#使用中国语言，简体中文
LANGUAGE_CODE = 'zh-Hans'

#使用中国上海时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

### 创建管理员
    创建管理员的代码如下，按照提示输入用户名、邮箱、密码
```
python manage.py createsuperuser



E:\xgm\git\learn_django\django_admin_backend>python manage.py createsuperuser
Username (leave blank to use 'test'):
Email address: test@126.com
Password:
Password (again):
Superuser created successfully.
```

    接下来启动服务器：
```
python manage.py runserver
```
    打开浏览器，在地址栏输入如下地址后回车
```
http://127.0.0.1:8000/admin/
```
    输入前面创建的用户名、密码完成登录

    登录成功后，并没有图书、英雄的管理入口，接下来进行注册模型类操作

### 注册模型类
    登录后台管理，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查操作。
    打开booktest/admin.py文件，编写如下代码：
```
from django.contrib import admin 
from models import BookInfo,HeroInfo 

admin.site.register(BookInfo) 
admin.site.register(HeroInfo)
```

    在浏览器中刷新页面，可以看到模型类的BooInfo和HeroInfo的管理

    点击类名称"BooInfo"可以进入列表页，默认只有一列，显示的是str方法返回的值
    修改Booktest目录的models.py文件里的BookInfo类，增加 def __str__方法
```
# Create your models here.
#定义图书模型类BookInfo
class BookInfo(models.Model):
    #图书名称， 唯一
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # python3不需要编码，python2则需要加一个编码encode('utf-8')
        return self.btitle.encode('utf-8')

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    #英雄姓名，不唯一，可以有重名的英雄
    hname = models.CharField(max_length=50, unique=False)
    #英雄性别，默认False是男性，也可以设置为integer类型 0或者1
    hgender = models.BooleanField(default=False);
    isDelete = models.BooleanField(default=False);
    #英雄的描述
    hcontent = models.CharField(max_length=500);
    #图书和英雄的关系是一对多的关系，所有属于定义在英雄的模型类中
    hbook = models.ForeignKey('BookInfo');

    def __str__(self):
        return self.hname.encode('utf-8')
```

    在列表页中点击”增加”可以进入增加页，Django会根据模型类的不同，生成不同的表单控件，按提示填写表单内容后点击”保存”，完成数据创建，创建成功后返回列表页。

    在列表页中点击某行的第一列可以进入修改页。

    删除：在列表页勾选想要删除的复选框，可以删除多项。

### 显示中文
    修改模型如下：
```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#定义图书模型类BookInfo
class BookInfo(models.Model):
    #图书名称， 唯一
    btitle = models.CharField(verbose_name="图书名称", max_length=50, unique=True)
    bpub_date = models.DateField(verbose_name="发布日期")
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # python3不需要编码，python2则需要加一个编码encode('utf-8')
        return self.btitle.encode('utf-8')

    class Meta:
        verbose_name = ('图书名称')
        verbose_name_plural=verbose_name

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    #英雄姓名，不唯一，可以有重名的英雄
    hname = models.CharField(verbose_name="英雄名称", max_length=50, unique=False)
    #英雄性别，默认False是男性，也可以设置为integer类型 0或者1
    hgender = models.BooleanField(verbose_name="性别", default=False);
    isDelete = models.BooleanField(default=False);
    #英雄的描述
    hcontent = models.CharField(verbose_name="英雄描述", max_length=500);
    #图书和英雄的关系是一对多的关系，所有属于定义在英雄的模型类中
    hbook = models.ForeignKey('BookInfo');

    def __str__(self):
        # python3不需要编码，python2则需要加一个编码encode('utf-8')
        return self.hname.encode('utf-8')

    class Meta:
        verbose_name=('英雄名称')
        verbose_name_plural=verbose_name
```


### 自定义管理页面
    在列表页只列出了str方法的返回值，对象的其它属性并没有列出来，查看非常不方便。 Django提供了自定义管理页面的功能，比如列表页要显示哪些值。
    打开booktest/admin.py文件，自定义类，继承自admin.ModelAdmin类。
    属性list_display表示要显示哪些属性
```
class BookInfoAdmin(admin.ModelAdmin):
         list_display = ['id', 'btitle', 'bpub_date']
```

    修改模型类BookInfo的注册代码如下
```
admin.site.register(BookInfo, BookInfoAdmin)
```

    最终booktest/admin.py文件代码如下:
```
from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
# 自定义bookinfo管理页面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']

# 自定义英雄管理页面
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','hgender','hcomment','hbook']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
```
   