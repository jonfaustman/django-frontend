from djfrontend.templatetags.settings import *

from django.conf import settings
from django.test import TestCase, LiveServerTestCase
from django.template import Template, Context


class DjfrontendStaticTest(LiveServerTestCase):

    """
    Ensure the files actually exist.
    """

    # Change settings until StaticLiveServerCase in 1.7!
    settings.DEBUG = True

    def test_djfrontend_h5bp_css(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/h5bp/%s/h5bp.css' % DJFRONTEND_H5BP_CSS_DEFAULT)
        self.assertEqual(file.status_code, 200)

    def test_djfrontend_normalize(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/normalize/%s/normalize.css' % DJFRONTEND_NORMALIZE_DEFAULT)
        self.assertEqual(file.status_code, 200)

    def test_djfrontend_fontawesome(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/fontawesome/%s/font-awesome.css' % DJFRONTEND_FONTAWESOME_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/css/fontawesome/%s/font-awesome.min.css' % DJFRONTEND_FONTAWESOME_DEFAULT)
        file_font_eot = self.client.get(self.live_server_url + '/static/djfrontend/fonts/fontawesome/%s/fontawesome-webfont.eot' % DJFRONTEND_FONTAWESOME_DEFAULT)
        file_font_svg = self.client.get(self.live_server_url + '/static/djfrontend/fonts/fontawesome/%s/fontawesome-webfont.svg' % DJFRONTEND_FONTAWESOME_DEFAULT)
        file_font_ttf = self.client.get(self.live_server_url + '/static/djfrontend/fonts/fontawesome/%s/fontawesome-webfont.ttf' % DJFRONTEND_FONTAWESOME_DEFAULT)
        file_font_woff = self.client.get(self.live_server_url + '/static/djfrontend/fonts/fontawesome/%s/fontawesome-webfont.woff' % DJFRONTEND_FONTAWESOME_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)
        self.assertEqual(file_font_eot.status_code, 200)
        self.assertEqual(file_font_svg.status_code, 200)
        self.assertEqual(file_font_ttf.status_code, 200)
        self.assertEqual(file_font_woff.status_code, 200)

    def test_djfrontend_modernizr(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/modernizr/%s/modernizr.js' % DJFRONTEND_MODERNIZR_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/modernizr/%s/modernizr.min.js' % DJFRONTEND_MODERNIZR_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jquery(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/%s/jquery.js' % DJFRONTEND_JQUERY_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/%s/jquery.min.js' % DJFRONTEND_JQUERY_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jqueryui(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jqueryui/%s/jquery-ui.js' % DJFRONTEND_JQUERYUI_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jqueryui/%s/jquery-ui.min.js' % DJFRONTEND_JQUERYUI_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jquery_datatables(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.dataTables/%s/jquery.dataTables.js' % DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.dataTables/%s/jquery.dataTables.min.js' % DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jquery_datatables_css(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables.css' % DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables.min.css' % DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file.status_code, 200)

    def test_djfrontend_jquery_datatables_themeroller(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables_themeroller.css' % DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)

    def test_djfrontend_jquery_formset(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.formset/%s/jquery.formset.js' % DJFRONTEND_JQUERY_FORMSET_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.formset/%s/jquery.formset.min.js' % DJFRONTEND_JQUERY_FORMSET_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jquery_scrollto(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.scrollTo/%s/jquery.scrollTo.js' % DJFRONTEND_JQUERY_SCROLLTO_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.scrollTo/%s/jquery.scrollTo.min.js' % DJFRONTEND_JQUERY_SCROLLTO_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_jquery_smoothscroll(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.js' % DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.min.js' % DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_twbs_css(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/twbs/%s/bootstrap.css' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/css/twbs/%s/bootstrap.min.css' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_font_eot = self.client.get(self.live_server_url + '/static/djfrontend/fonts/twbs/%s/glyphicons-halflings-regular.eot' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_font_svg = self.client.get(self.live_server_url + '/static/djfrontend/fonts/twbs/%s/glyphicons-halflings-regular.svg' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_font_ttf = self.client.get(self.live_server_url + '/static/djfrontend/fonts/twbs/%s/glyphicons-halflings-regular.ttf' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_font_woff = self.client.get(self.live_server_url + '/static/djfrontend/fonts/twbs/%s/glyphicons-halflings-regular.woff' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)
        self.assertEqual(file_font_eot.status_code, 200)
        self.assertEqual(file_font_svg.status_code, 200)
        self.assertEqual(file_font_ttf.status_code, 200)
        self.assertEqual(file_font_woff.status_code, 200)

    def test_djfrontend_twbs_theme_css(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/css/twbs/%s/bootstrap-theme.css' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/css/twbs/%s/bootstrap-theme.min.css' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)

    def test_djfrontend_twbs_js(self):
        file = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/bootstrap.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_min = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/bootstrap.min.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_affix = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/affix.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_alert = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/alert.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_button = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/button.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_carousel = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/carousel.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_collapse = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/collapse.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_dropdown = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/dropdown.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_modal = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/modal.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_popover = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/popover.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_scrollspy = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/scrollspy.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_tab = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/tab.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_tooltip = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/tooltip.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        file_transition = self.client.get(self.live_server_url + '/static/djfrontend/js/twbs/%s/transition.js' % DJFRONTEND_TWBS_VERSION_DEFAULT)
        self.assertEqual(file.status_code, 200)
        self.assertEqual(file_min.status_code, 200)
        self.assertEqual(file_affix.status_code, 200)
        self.assertEqual(file_alert.status_code, 200)
        self.assertEqual(file_button.status_code, 200)
        self.assertEqual(file_carousel.status_code, 200)
        self.assertEqual(file_collapse.status_code, 200)
        self.assertEqual(file_dropdown.status_code, 200)
        self.assertEqual(file_modal.status_code, 200)
        self.assertEqual(file_popover.status_code, 200)
        self.assertEqual(file_scrollspy.status_code, 200)
        self.assertEqual(file_tab.status_code, 200)
        self.assertEqual(file_tooltip.status_code, 200)
        self.assertEqual(file_transition.status_code, 200)


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

    def test_djfrontend_twbs_js_popover(self):
        t = Template(
            "{% load djfrontend %}"
            "{% djfrontend_twbs_js files='popover' %}"
        ).render(Context())
        self.assertTrue('popover.js' in t)
        self.assertTrue('tooltip.js' in t)


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

    def test_djfrontend_jquery_datatables_themeroller(self):
        settings.DJFRONTEND_JQUERY_DATATABLES_THEMEROLLER = '0.0.0'
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
