from .settings import *

from django import template
from django.conf import settings
from django.utils.html import mark_safe, format_html

register = template.Library()


@register.simple_tag
def djfrontend_h5bp_html(language=None):
    """
    Returns HTML tag according to chosen language.
    Included in HTML5 Boilerplate.
    """
    if language is None:
        language = getattr(settings, 'DJFRONTEND_H5BP_HTML', DJFRONTEND_H5BP_HTML_DEFAULT)

    return format_html('<html class="no-js" lang="{0}">', language)


_static_url = settings.STATIC_URL
if getattr(settings, 'TEMPLATE_DEBUG', False):
    _min = ''
else:
    _min = '.min'
    if getattr(settings, 'DJFRONTEND_STATIC_URL', None):
        _static_url = settings.DJFRONTEND_STATIC_URL


@register.simple_tag
def djfrontend_h5bp_css(version=None):
    """
    Returns HTML5 Boilerplate CSS file.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_H5BP_CSS', DJFRONTEND_H5BP_CSS_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="{0}djfrontend/css/h5bp/{1}/h5bp.css">',
        _static_url, version)


@register.simple_tag
def djfrontend_normalize(version=None):
    """
    Returns Normalize CSS file.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_NORMALIZE', DJFRONTEND_NORMALIZE_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="{0}djfrontend/css/normalize/{1}/normalize.css">',
        _static_url, version)


@register.simple_tag
def djfrontend_fontawesome(version=None):
    """
    Returns Font Awesome CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_FONTAWESOME', DJFRONTEND_FONTAWESOME_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="{0}djfrontend/css/fontawesome/{1}/font-awesome{2}.css">',
        _static_url, version, _min)


@register.simple_tag
def djfrontend_modernizr(version=None):
    """
    Returns Modernizr JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_MODERNIZR', DJFRONTEND_MODERNIZR_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/modernizr/{v}/modernizr.js"></script>'
    else:
        template = (
            '<script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/{v}/modernizr.min.js"></script>\n'
            '<script>window.Modernizr || document.write(\'<script src="{static}djfrontend/js/modernizr/{v}/modernizr.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery(version=None):
    """
    Returns jQuery JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY', DJFRONTEND_JQUERY_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/jquery/{v}/jquery.js"></script>'
    else:
        template = (
            '<script src="//ajax.googleapis.com/ajax/libs/jquery/{v}/jquery.min.js"></script>'
            '<script>window.jQuery || document.write(\'<script src="{static}djfrontend/js/jquery/{v}/jquery.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_jqueryui(version=None):
    """
    Returns the jQuery UI plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERYUI', DJFRONTEND_JQUERYUI_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return format_html(
            '<script src="{0}djfrontend/js/jquery/jqueryui/{1}/jquery-ui.js"></script>',
            settings.STATIC_URL, version)
    else:
        return format_html(
            '<script src="//ajax.googleapis.com/ajax/libs/jqueryui/{v}/jquery-ui.min.js"></script>'
            '<script>window.jQuery.ui || document.write(\'<script src="{static}djfrontend/js/jquery/jqueryui/{v}/jquery-ui.min.js"><\/script>\')</script>',
            static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery_datatables(version=None):
    """
    Returns the jQuery DataTables plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES', False):
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_VERSION', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        else:
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/jquery/jquery.dataTables/{v}/jquery.dataTables.js"></script>'
    else:
        template = (
            '<script src="//cdnjs.cloudflare.com/ajax/libs/datatables/{v}/jquery.dataTables.min.js"></script>'
            '<script>window.jQuery.fn.DataTable || document.write(\'<script src="{static}djfrontend/js/jquery/jquery.dataTables/{v}/jquery.dataTables.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery_datatables_css(version=None):
    """
    Returns the jQuery DataTables CSS file according to version number.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_CSS', False):
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_VERSION', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        else:
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_CSS', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)


    return format_html(
        '<link rel="stylesheet" href="{static}djfrontend/css/jquery/jquery.dataTables/{v}/jquery.dataTables{min}.css">',
        static=_static_url, v=version, min=_min)


@register.simple_tag
def djfrontend_jquery_datatables_themeroller(version=None):
    """
    Returns the jQuery DataTables ThemeRoller CSS file according to version number.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_THEMEROLLER', False):
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_VERSION', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)
        else:
            version = getattr(settings, 'DJFRONTEND_JQUERY_DATATABLES_THEMEROLLER', DJFRONTEND_JQUERY_DATATABLES_VERSION_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="href="{static}djfrontend/css/jquery/jquery.dataTables/{v}/jquery.dataTables_themeroller.min.css">',
        static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery_formset(version=None):
    """
    Returns the jQuery Dynamic Formset plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_FORMSET', DJFRONTEND_JQUERY_FORMSET_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/jquery/jquery.formset/{v}/jquery.formset.js"></script>'
    else:
        template = (
            '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery.formset/{v}/jquery.formset.min.js"></script>\n'
            '<script>window.jQuery.fn.formset || document.write(\'<script src="{static}djfrontend/js/jquery/jquery.formset/{v}/jquery.formset.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery_scrollto(version=None):
    """
    Returns the jQuery ScrollTo plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_SCROLLTO', DJFRONTEND_JQUERY_SCROLLTO_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/jquery/jquery.scrollTo/{v}/jquery.scrollTo.js"></script>'
    else:
        template = (
            '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/{v}/jquery.scrollTo.min.js"></script>'
            '<script>window.jQuery.fn.scrollTo || document.write(\'<script src="{static}djfrontend/js/jquery/jquery.scrollTo/{v}/jquery.scrollTo.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_jquery_smoothscroll(version=None):
    """
    Returns the jQuery Smooth Scroll plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_SMOOTHSCROLL', DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        template = '<script src="{static}djfrontend/js/jquery/jquery.smooth-scroll/{v}/jquery.smooth-scroll.js"></script>'
    else:
        template = (
            '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-smooth-scroll/{v}/jquery.smooth-scroll.min.js"></script>'
            '<script>window.jQuery.fn.smoothScroll || document.write(\'<script src="{static}djfrontend/js/jquery/jquery.smooth-scroll/{v}/jquery.smooth-scroll.min.js"><\/script>\')</script>')
    return format_html(template, static=_static_url, v=version)


@register.simple_tag
def djfrontend_twbs_css(version=None):
    """
    Returns Twitter Bootstrap CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_TWBS_CSS', False):
            version = getattr(settings, 'DJFRONTEND_TWBS_VERSION', DJFRONTEND_TWBS_VERSION_DEFAULT)
        else:
             version = getattr(settings, 'DJFRONTEND_TWBS_CSS', DJFRONTEND_TWBS_VERSION_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="{static}djfrontend/css/twbs/{v}/bootstrap{min}.css">',
        static=_static_url, v=version, min=_min)


@register.simple_tag
def djfrontend_twbs_theme_css(version=None):
    """
    Returns Twitter Bootstrap Theme CSS file.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_TWBS_THEME_CSS', False):
            version = getattr(settings, 'DJFRONTEND_TWBS_VERSION', DJFRONTEND_TWBS_VERSION_DEFAULT)
        else:
             version = getattr(settings, 'DJFRONTEND_TWBS_THEME_CSS', DJFRONTEND_TWBS_VERSION_DEFAULT)

    return format_html(
        '<link rel="stylesheet" href="{static}djfrontend/css/twbs/{v}/bootstrap-theme{min}.css">',
        static=_static_url, v=version, min=_min)


@register.simple_tag
def djfrontend_twbs_js(version=None, files=None):
    """
    Returns Twitter Bootstrap JavaScript file(s).
    all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise.

    Other choice are:
        affix,
        alert,
        button,
        carousel,
        collapse,
        dropdown,
        modal,
        popover (adds tooltip if not included),
        scrollspy,
        tab,
        tooltip,
        transition.

    Individual files are not minified.
    """
    if version is None:
        if not getattr(settings, 'DJFRONTEND_TWBS_JS_VERSION', False):
            version = getattr(settings, 'DJFRONTEND_TWBS_VERSION', DJFRONTEND_TWBS_VERSION_DEFAULT)
        else:
            version = getattr(settings, 'DJFRONTEND_TWBS_JS_VERSION', DJFRONTEND_TWBS_VERSION_DEFAULT)

    if files:
        if files != 'all':
            files = files.split(' ')
    elif getattr(settings, 'DJFRONTEND_TWBS_JS_FILES', False) and settings.DJFRONTEND_TWBS_JS_FILES != 'all':
        files = settings.DJFRONTEND_TWBS_JS_FILES.split(' ')
    else:
        files = 'all'

    if files == 'all':
        return format_html(
            '<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/{v}/js/bootstrap.min.js"></script>\n'
            '<script>window.jQuery.fn.scrollspy || document.write(\'<script src="{static}djfrontend/js/twbs/{v}/bootstrap.min.js"><\/script>\')</script>',
            v=version, static=_static_url)
    else:
        if 'popover' in files and 'tooltip' not in files:
            files.append('tooltip')
        for file in files:
            file = ['<script src="%sdjfrontend/js/twbs/%s/%s.js"></script>' %
                    (_static_url, version, file) for file in files]
        return mark_safe('\n'.join(file))


@register.simple_tag
def djfrontend_ga(account=None):
    """
    Returns Google Analytics asynchronous snippet.
    Use DJFRONTEND_GA_SETDOMAINNAME to set domain for multiple, or cross-domain tracking.
    Set DJFRONTEND_GA_SETALLOWLINKER to use _setAllowLinker method on target site for cross-domain tracking.
    Included in HTML5 Boilerplate.
    """
    if account is None:
        account = getattr(settings, 'DJFRONTEND_GA', False)

    if account:
        if getattr(settings, 'TEMPLATE_DEBUG', False):
            return ''
        else:
            if getattr(settings, 'DJFRONTEND_GA_SETDOMAINNAME', False):
                if getattr(settings, 'DJFRONTEND_GA_SETALLOWLINKER', False):
                    return mark_safe(
                        '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("require", "linker");ga("linker:autoLink", ["%s"]);ga("create", "%s", "auto", {"allowLinker": true});ga("send", "pageview");</script>' %
                        (settings.DJFRONTEND_GA_SETDOMAINNAME, account))
                else:
                    return mark_safe(
                        '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "%s", "%s");ga("send", "pageview");</script>' %
                        (account, settings.DJFRONTEND_GA_SETDOMAINNAME))
            else:
                return mark_safe(
                    '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "%s", "auto");ga("send", "pageview");</script>' % account)
    else:
        return ''
