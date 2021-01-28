from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.models import Text
from news_cms_integration.models import NewsTextModel
from cms.plugin_base import CMSPluginBase

@plugin_pool.register_plugin
class NewsPlugin(TextPlugin):
    name = _('News Plugin')
    model = NewsTextModel
    render_template = "news_text_plugin.html"
    cache = False


    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context