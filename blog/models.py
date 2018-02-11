from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):#python 类
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()#主体采用textfield储蓄大段文本
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()#最后一次修改时间
    excerot = models.CharField(max_length=200,blank=True)#文章摘要，置顶blank=True才可为空，否则不可以
    category = models.ForeignKey(Category)#ForeignKey 一对多关联关系
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time','title']


