# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
