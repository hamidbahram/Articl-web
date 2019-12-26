# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
#ckeditor
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.

class Article(models.Model):
    title            =  models.CharField(max_length=100)
    slug             =  models.SlugField()
    body             =  RichTextUploadingField(('content'), config_name = 'default')
    date             =  models.DateTimeField(_('create date'), auto_now_add=True, auto_now=False)
    updatedatetime   =  models.DateTimeField(_('update date'), auto_now_add=False, auto_now=True)
    # pip install pillow
    thumb            =  models.ImageField(default='default.png', blank=True)
    author           =  models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                default=None,
                                blank = True,
                                null = True,
                                verbose_name = _('Owner'),
                                help_text = _('choose owner'))

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        #return self.title
        return "{}".format(self.title)

    def snippet(self):
        #return self.body[:50]
        return "{}".format(self.body[:50]) + " ..."

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"id": self.id})

    # def get_absolute_url(self):
    #     return reverse("articles:detail", kwargs={"slug": self.slug})
    