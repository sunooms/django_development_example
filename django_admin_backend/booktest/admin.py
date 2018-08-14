# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import BookInfo, HeroInfo

# Register your models here.
# 自定义bookinfo管理页面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

# 自定义英雄管理页面
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','hgender','hcontent','hbook']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
