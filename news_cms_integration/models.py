from django.db import models

from djangocms_text_ckeditor.models import AbstractText, Text
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin


class NewsTextModel(AbstractText):
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    introduction = HTMLField(blank=True, verbose_name='News introduction')
    body = models.TextField(verbose_name='News full text')
    # intro = HTMLField(blank=True)

