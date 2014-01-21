from djfrontend.templatetags.settings import *

from django.conf import settings
from django.test import TestCase
from django.template import Template, Context

class DjfrontendDefaultTestCase(TestCase):
    
    """
    Ensure the default values are being returned.
    """
    
    def test_djfrontend_h5bp_html(self):
        attr = 'lang="%s"' % DJFRONTEND_H5BP_HTML_DEFAULT
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_html %}"
        ).render(Context())
        
        self.assertTrue(attr in t)
    
    def test_djfrontend_h5bp_css(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_css %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_H5BP_CSS_DEFAULT in t)
        
    def test_djfrontend_normalize(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_normalize %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_NORMALIZE_DEFAULT in t)
        
    def test_djfrontend_fontawesome(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_fontawesome %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_FONTAWESOME_DEFAULT in t)

    def test_djfrontend_modernizr(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_modernizr %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_MODERNIZR_DEFAULT in t)
        
    def test_djfrontend_jquery(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_DEFAULT in t)
        
    def test_djfrontend_jqueryui(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jqueryui %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERYUI_DEFAULT in t)
        
    def test_djfrontend_jquery_datatables(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
        
    def test_djfrontend_jquery_datatables_css(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables_css %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
        
    def test_djfrontend_jquery_formset(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_formset %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_FORMSET_DEFAULT in t)
        
    def test_djfrontend_jquery_scrollto(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_scrollto %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_SCROLLTO_DEFAULT in t)
        
    def test_djfrontend_jquery_smoothscroll(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_smoothscroll %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT in t)
        
    def test_djfrontend_twbs_css(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_css %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
        
    def test_djfrontend_twbs_theme_css(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_theme_css %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
        
    def test_djfrontend_twbs_js(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_js %}"
        ).render(Context())
        
        self.assertTrue(DJFRONTEND_TWBS_VERSION_DEFAULT in t)