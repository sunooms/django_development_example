# 使用pycharm和django进行开发实例

[toc]

## pycharm（企业版）新建django工程
  >file-->new project-->django-->输入项目名称

## 新建django的app
  打开pycharm的terminal， 进入该工程的目录，新见一个django工程
  python manage.py startapp django_web

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

### 在templates下新建一个index.html文件，把下面内容替换到改文件中
```
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The blah</title>
    <link rel="stylesheet" type="text/css" href=" new_blah.css">
</head>
<body>

<div class="header">
    <img src="images/blah.png">
    <ul class="nav">
        <li><a href="#">Home</a></li>
        <li><a href="#">Site</a></li>
        <li><a href="#">Other</a></li>
    </ul>

</div>

<div class="main-content">
    <h2>Article</h2>
    <ul class="article">

        <li>
            <img src="images/0001.jpg" width="100" height="90">
            <h3><a href="#">The blah</a></h3>
            <p>This is a dangerously delicious cake.</p>
        </li>

        <li>
            <img src="images/0002.jpg" width="100" height="90">
            <h3><a href="#">The blah</a></h3>
            <p>It's always taco night somewhere!</p>
        </li>

        <li>
            <img src="images/0003.jpg" width="100" height="90">
            <h3><a href="#">The blah</a></h3>
            <p>Omelette you in on a little secret </p>
        </li>

        <li>
            <img src="images/0004.jpg" width="100" height="90">
            <h3><a href="#">The blah</a></h3>
            <p>It's a sandwich. That's all we .</p>
        </li>
    </ul>
</div>

<div class="footer">
    <p>&copy; Mugglecoding</p>
</div>
</body>
</html>

<--!http://css3gen.com/box-shadow/-->
```

### 编写views.py文件，定义访问这个index.html文件的操作

```
def index(request): 
     return render(request, 'index.html')
```

### 编写urls.py文件，定义访问这个index.html的url路径（使用正则表达式）

```
# -*- coding: utf-8 -*-
from django.conf.urls import url 
from django.contrib import admin 
from django_web.views import index #导入views.py文件中的index函数 

urlpatterns = [ 
    url(r'^admin/', admin.site.urls), 
    url(r'^index/', index), #在url中凡是以url开头的访问都使用index函数来处理该请求 
]
```
    注意： urls.py文件的第一行，要确认是否utf-8编码，默认没有coding

### 在pycharm的Terminal中输入命令运行服务器
```
python3 manager.py runserver
```

### 在浏览器中查看
```
在浏览器中输入url：http://127.0.0.1:8000/index/ 可以看到如下的格式，接下来要做的就是添加资源
```

### 将css文件和图片都复制到first_django工程下的一个名为static的文件，工程结构如下
```
--first_django
----django_web
----first_django
----static
------css
--------new_blah.css
------images
--------0001.jpg
--------0002.jpg
--------0003.jpg
--------0004.jpg
--------bg1.jpg
--------bg2.jpg
--------bg3.png
--------bg3-dark.jpg
--------blah.png
--------fire.png
----templates
----db.sqlite3
----manage.py
```
    注意： 一定要保证与templates目录同级    

### 修改index.html如下
```
{% load static %}

<html>

<head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/new_blah.css' %}">
</head>
<body>

<div class="header">
    <img src="{% static 'images/blah.png' %}">
    <ul class="nav">
        <li><a href="#">Home</a></li>
        <li><a href="#">Site</a></li>
        <li><a href="#">Other</a></li>
    </ul>
</div>

<div class="main-content">
    <h2>Article</h2>
    <ul class="articles">

        <li>
            <img src="{% static 'images/0001.jpg' %}" width="100" height="91">

            <div class="article-info">
                <h3><a href="#">The blah</a></h3>
                <p class="meta-info">
                    <span class="meta-cate">fun</span>
                    <span class="meta-cate">Wow</span>
                </p>
                <p class="description">Just say something.</p>
            </div>

            <div class="rate">
                <span class="rate-score">4.5</span>
            </div>
        </li>

        <li>
            <img src="{% static 'images/0002.jpg' %}" width="100" height="91">
            <div class="article-info">
                <h3><a href="#">The blah</a></h3>
                <p class="meta-info">
                    <span class="meta-cate">butt</span>
                    <span class="meta-cate">NSFW</span>
                </p>
                <p class="description">Just say something.</p>
            </div>

            <div class="rate">
                <img src="{% static 'images/Fire.png' %}" width="18" height="18">
                <span class="rate-score">5.0</span>
            </div>
        </li>

        <li>
            <img src="{% static 'images/0003.jpg' %}" width="100" height="91">
            <div class="article-info">
                <h3><a href="#">The blah</a></h3>
                <p class="meta-info">
                    <span class="meta-cate">sea</span>
                </p>
                <p class="description">Just say something.</p>
            </div>

            <div class="rate">
                <span class="rate-score">3.5</span>
            </div>
        </li>

        <li>
            <img src="{% static 'images/0004.jpg' %}" width="100" height="91">
            <div class="article-info">
                <h3><a href="#">The blah</a></h3>
                <p class="meta-info">
                    <span class="meta-cate">bay</span>
                    <span class="meta-cate">boat</span>
                    <span class="meta-cate">beach</span>
                </p>
                <p class="description">Just say something.</p>
            </div>

            <div class="rate">
                <span class="rate-score">3.0</span>
            </div>
        </li>
    </ul>
</div>

<div class="footer">
    <p>&copy; Mugglecoding</p>
</div>
</body>

</html>
```   

### 修改css文件
```
body {
    padding: 0 0 0 0;
    background-color: #ffffff;
    background-image: url(../images/bg3-dark.jpg);
    background-position: top left;
    background-repeat: no-repeat;
    background-size: cover;
    font-family: Helvetica, Arial, sans-serif;
}


.main-content {
    width: 500px;
    padding: 20px 20px 20px 20px;
    border: 1px solid #dddddd;
    border-radius:15px;
    margin: 30px auto 0 auto;
    background: #fdffff;
    -webkit-box-shadow: 0 0 22px 0 rgba(50, 50, 50, 1);
    -moz-box-shadow:    0 0 22px 0 rgba(50, 50, 50, 1);
    box-shadow:         0 0 22px 0 rgba(50, 50, 50, 1);


}
.main-content p {
    line-height: 26px;
}
.main-content h2 {
    color: #585858;
}
.articles {
    list-style-type: none;
    padding: 0;
}
.articles img {
    float: left;
    padding-right: 11px;
}
.articles li {
    border-top: 1px solid #F1F1F1;
    background-color: #ffffff;
    height: 90px;
    clear: both;
}
.articles h3 {
    margin: 0;
}
.articles a {
    color:#585858;
    text-decoration: none;
}
.articles p {
    margin: 0;
}

.article-info {
    float: left;
    display: inline-block;
    margin: 8px 0 8px 0;
}

.rate {
    float: right;
    display: inline-block;
    margin:35px 20px 35px 20px;
}

.rate-score {
    font-size: 18px;
    font-weight: bold;
    color: #585858;
}

.rate-score-hot {


}

.meta-info {
}

.meta-cate {
    margin: 0 0.1em;
    padding: 0.1em 0.7em;
    color: #fff;
    background: #37a5f0;
    font-size: 20%;
    border-radius: 10px ;
}

.description {
    color: #cccccc;
}

.nav {
    padding-left: 0;
    margin: 5px 0 20px 0;
    text-align: center;
}
.nav li {
    display: inline;
    padding-right: 10px;
}
.nav li:last-child {
    padding-right: 0;
}
.header {
    padding: 10px 10px 10px 10px;

}

.header a {
    color: #ffffff;
}
.header img {
    display: block;
    margin: 0 auto 0 auto;
}
.header h1 {
    text-align: center;
}



.footer {
    margin-top: 20px;
}
.footer p {
    color: #aaaaaa;
    text-align: center;
    font-weight: bold;
    font-size: 12px;
    font-style: italic;
    text-transform: uppercase;
}
``` 

### 在settings.py文件的增加static配置
```
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
```