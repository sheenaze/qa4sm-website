from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.models import Text
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from django.forms.models import ModelForm
from django import forms

TEXT_CKEDITOR_CONFIGURATION = getattr(settings, 'TEXT_CKEDITOR_CONFIGURATION', None)

class TextForm(ModelForm):
    body = forms.CheckboxInput
    # body = forms.CharField()

    class Meta:
        model = Text
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )

@plugin_pool.register_plugin
class NewsPlugin(TextPlugin):
    name = _('News Plugin')
    form = TextForm
    render_template = "news_text_plugin.html"
    cache = False

print('Monika', TEXT_CKEDITOR_CONFIGURATION)