# ʹ��django���к�̨������ʵ��

[toc]

## pycharm����ҵ�棩�½�django����
  >file-->new project-->django-->������Ŀ����(django_admin_backend)

```
1 mkdir /test/django_admin_backend
2 django-admin startproject django_admin_backend
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
        'PASSWORD': '123456', #���ݿ��¼����
        'HOST': 'localhost', #���ݿ���������
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
    'booktest'
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
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False)

#����Ӣ��ģ����HeroInfo
class HeroInfo(models.Model):
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





### ��̨����Ĳ���
    >1 ������汾�ػ�
    >2 ��������Ա
    >3 ע��ģ����
    >4 �Զ������ҳ��

### ������汾�ػ�
    ���ػ��ǽ���ʾ�����ԡ�ʱ���ʹ�ñ��ص�ϰ�ߣ�����ı��ػ����ǽ����й������й���½����ʹ�ü������ģ�ʱ��ʹ������/�Ϻ�ʱ����ע�����ﲻʹ�ñ���ʱ����ʾ��

    ��django_admin_backend/settings.py�ļ����ҵ����Ա��롢ʱ��������������ݸ�Ϊ���£�
```
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# ԭ��django�е����Ժ�ʱ������
#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'

#ʹ���й����ԣ���������
LANGUAGE_CODE = 'zh-Hans'

#ʹ���й��Ϻ�ʱ��
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

### ��������Ա
    ��������Ա�Ĵ������£�������ʾ�����û��������䡢����
```
python manage.py createsuperuser



E:\xgm\git\learn_django\django_admin_backend>python manage.py createsuperuser
Username (leave blank to use 'test'):
Email address: test@126.com
Password:
Password (again):
Superuser created successfully.
```

    ������������������
```
python manage.py runserver
```
    ����������ڵ�ַ���������µ�ַ��س�
```
http://127.0.0.1:8000/admin/
```
    ����ǰ�洴�����û�����������ɵ�¼

    ��¼�ɹ��󣬲�û��ͼ�顢Ӣ�۵Ĺ�����ڣ�����������ע��ģ�������

### ע��ģ����
    ��¼��̨����Ĭ��û�����Ǵ�����Ӧ���ж����ģ���࣬��Ҫ���Լ�Ӧ���е�admin.py�ļ���ע�ᣬ�ſ����ں�̨�����п�������������ɾ�Ĳ������
    ��booktest/admin.py�ļ�����д���´��룺
```
from django.contrib import admin 
from models import BookInfo,HeroInfo 

admin.site.register(BookInfo) 
admin.site.register(HeroInfo)
```

    ���������ˢ��ҳ�棬���Կ���ģ�����BooInfo��HeroInfo�Ĺ���

    ���������"BooInfo"���Խ����б�ҳ��Ĭ��ֻ��һ�У���ʾ����str�������ص�ֵ
    �޸�BooktestĿ¼��models.py�ļ����BookInfo�࣬���� def __str__����
```
# Create your models here.
#����ͼ��ģ����BookInfo
class BookInfo(models.Model):
    #ͼ�����ƣ� Ψһ
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # python3����Ҫ���룬python2����Ҫ��һ������encode('utf-8')
        return self.btitle.encode('utf-8')

#����Ӣ��ģ����HeroInfo
class HeroInfo(models.Model):
    #Ӣ����������Ψһ��������������Ӣ��
    hname = models.CharField(max_length=50, unique=False)
    #Ӣ���Ա�Ĭ��False�����ԣ�Ҳ��������Ϊinteger���� 0����1
    hgender = models.BooleanField(default=False);
    isDelete = models.BooleanField(default=False);
    #Ӣ�۵�����
    hcontent = models.CharField(max_length=500);
    #ͼ���Ӣ�۵Ĺ�ϵ��һ�Զ�Ĺ�ϵ���������ڶ�����Ӣ�۵�ģ������
    hbook = models.ForeignKey('BookInfo');

    def __str__(self):
        return self.hname.encode('utf-8')
```

    ���б�ҳ�е�������ӡ����Խ�������ҳ��Django�����ģ����Ĳ�ͬ�����ɲ�ͬ�ı��ؼ�������ʾ��д�����ݺ��������桱��������ݴ����������ɹ��󷵻��б�ҳ��

    ���б�ҳ�е��ĳ�еĵ�һ�п��Խ����޸�ҳ��

    ɾ�������б�ҳ��ѡ��Ҫɾ���ĸ�ѡ�򣬿���ɾ�����

### �Զ������ҳ��
    ���б�ҳֻ�г���str�����ķ���ֵ��������������Բ�û���г������鿴�ǳ������㡣 Django�ṩ���Զ������ҳ��Ĺ��ܣ������б�ҳҪ��ʾ��Щֵ��
    ��booktest/admin.py�ļ����Զ����࣬�̳���admin.ModelAdmin�ࡣ
    ����list_display��ʾҪ��ʾ��Щ����
```
class BookInfoAdmin(admin.ModelAdmin):
         list_display = ['id', 'btitle', 'bpub_date']
```

    �޸�ģ����BookInfo��ע���������
```
admin.site.register(BookInfo, BookInfoAdmin)
```

    ����booktest/admin.py�ļ���������:
```
from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
# �Զ���bookinfo����ҳ��
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']

# �Զ���Ӣ�۹���ҳ��
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','hgender','hcomment','hbook']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
```
   