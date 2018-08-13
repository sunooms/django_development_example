# 使用pycharm和django进行开发实例

## pycharm（企业版）新建django工程
  #file-->new project-->django-->输入项目名称

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