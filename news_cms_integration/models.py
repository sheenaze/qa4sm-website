from django.db import models

from djangocms_text_ckeditor.models import AbstractText, Text
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin

CKEDITOR_SETTINGS_MODEL1 = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
    ]
}

class NewsTextModel(AbstractText):
    # text = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL1')
    guest_name = models.CharField(max_length=50, default='Guest')
