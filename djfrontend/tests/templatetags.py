from djfrontend.templatetags.settings import *

from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
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


class DjfrontendSettingsTestCase(TestCase):
    
    """
    Ensure the settings override the defaults.
    """
    
    def test_djfrontend_h5bp_html(self):
        attr = 'lang="%s"' % DJFRONTEND_H5BP_HTML_DEFAULT
        settings.DJFRONTEND_H5BP_HTML = 'fr'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_html %}"
        ).render(Context())
        
        self.assertFalse(attr in t)
        
    def test_djfrontend_h5bp_css(self):
        settings.DJFRONTEND_H5BP_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_css %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_H5BP_CSS_DEFAULT in t)
        
    def test_djfrontend_normalize(self):
        settings.DJFRONTEND_NORMALIZE = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_normalize %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_NORMALIZE_DEFAULT in t)
        
    def test_djfrontend_fontawesome(self):
        settings.DJFRONTEND_FONTAWESOME = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_fontawesome %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_FONTAWESOME_DEFAULT in t)

    def test_djfrontend_modernizr(self):
        settings.DJFRONTEND_MODERNIZR = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_modernizr %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_MODERNIZR_DEFAULT in t)
    
    def test_djfrontend_jquery(self):
        settings.DJFRONTEND_JQUERY = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_DEFAULT in t)
    
    def test_djfrontend_jqueryui(self):
        settings.DJFRONTEND_JQUERYUI = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jqueryui %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERYUI_DEFAULT in t)
    
    def test_djfrontend_jquery_datatables(self):
        settings.DJFRONTEND_JQUERY_DATATABLES = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
    
    def test_djfrontend_jquery_datatables_css(self):
        settings.DJFRONTEND_JQUERY_DATATABLES_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables_css %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
    
    def test_djfrontend_jquery_formset(self):
        settings.DJFRONTEND_JQUERY_FORMSET = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_formset %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_FORMSET_DEFAULT in t)
    
    def test_djfrontend_jquery_scrollto(self):
        settings.DJFRONTEND_JQUERY_SCROLLTO = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_scrollto %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_SCROLLTO_DEFAULT in t)
    
    def test_djfrontend_jquery_smoothscroll(self):
        settings.DJFRONTEND_JQUERY_SMOOTHSCROLL = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_smoothscroll %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT in t)
    
    def test_djfrontend_twbs_css(self):
        settings.DJFRONTEND_TWBS_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_css %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
    
    def test_djfrontend_twbs_theme_css(self):
        settings.DJFRONTEND_TWBS_THEME_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_theme_css %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
    
    def test_djfrontend_twbs_js(self):
        settings.DJFRONTEND_TWBS_JS_VERSION = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_js %}"
        ).render(Context())
    
        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)


class DjfrontendSettingsGranularityTestCase(TestCase):
    
    """
    Ensure the template tag argument is the final override.
    """
    
    def test_djfrontend_h5bp_html(self):
        attr_default = 'lang="%s"' % DJFRONTEND_H5BP_HTML_DEFAULT
        attr = 'lang="de"'
        settings.DJFRONTEND_H5BP_HTML = 'fr'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_html 'de' %}"
        ).render(Context())
        
        self.assertFalse(attr_default in t)
        self.assertTrue(attr in t)
        
    def test_djfrontend_h5bp_css(self):
        settings.DJFRONTEND_H5BP_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_h5bp_css 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_H5BP_CSS_DEFAULT in t)
        self.assertTrue('x.x.x' in t)
        
    def test_djfrontend_normalize(self):
        settings.DJFRONTEND_NORMALIZE = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_normalize 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_NORMALIZE_DEFAULT in t)
        self.assertTrue('x.x.x' in t)
    
    def test_djfrontend_fontawesome(self):
        settings.DJFRONTEND_FONTAWESOME = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_fontawesome 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_FONTAWESOME_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_modernizr(self):
        settings.DJFRONTEND_MODERNIZR = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_modernizr 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_MODERNIZR_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery(self):
        settings.DJFRONTEND_JQUERY = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jqueryui(self):
        settings.DJFRONTEND_JQUERYUI = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jqueryui 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERYUI_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery_datatables(self):
        settings.DJFRONTEND_JQUERY_DATATABLES = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery_datatables_css(self):
        settings.DJFRONTEND_JQUERY_DATATABLES_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_datatables_css 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery_formset(self):
        settings.DJFRONTEND_JQUERY_FORMSET = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_formset 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_FORMSET_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery_scrollto(self):
        settings.DJFRONTEND_JQUERY_SCROLLTO = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_scrollto 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_SCROLLTO_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_jquery_smoothscroll(self):
        settings.DJFRONTEND_JQUERY_SMOOTHSCROLL = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_jquery_smoothscroll 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_twbs_css(self):
        settings.DJFRONTEND_TWBS_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_css 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_twbs_theme_css(self):
        settings.DJFRONTEND_TWBS_THEME_CSS = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_theme_css 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
        self.assertTrue('x.x.x' in t)

    def test_djfrontend_twbs_js(self):
        settings.DJFRONTEND_TWBS_JS_VERSION = '0.0.0'
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_js 'x.x.x' %}"
        ).render(Context())

        self.assertFalse(DJFRONTEND_TWBS_VERSION_DEFAULT in t)
        self.assertTrue('x.x.x' in t)