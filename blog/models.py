#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class About(models.Model):
    body = models.TextField('内容')
    name = models.CharField('标题', max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.TextField('摘要', max_length=140, blank=True, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name


class Recommend(models.Model):

    title = models.CharField('标题', max_length=70)
    abstract = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    category = models.ForeignKey('Category_rc', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category_rc(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name
