from .settings import *

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def djfrontend_h5bp_html(language=None):
    """
    Returns HTML tag according to chosen language.
    Included in HTML5 Boilerplate.
    """
    if language is None:
        language = getattr(settings, 'DJFRONTEND_H5BP_HTML', DJFRONTEND_H5BP_HTML_DEFAULT)

    return '<html class="no-js" lang="%s">' % language


@register.simple_tag
def djfrontend_h5bp_css(version=None):
    """
    Returns HTML5 Boilerplate CSS file.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_H5BP_CSS', DJFRONTEND_H5BP_CSS_DEFAULT)

    if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/h5bp/%s/h5bp.css">' % (settings.DJFRONTEND_STATIC_URL, version)
    return '<link rel="stylesheet" href="%sdjfrontend/css/h5bp/%s/h5bp.css">' % (settings.STATIC_URL, version)


@register.simple_tag
def djfrontend_normalize(version=None):
    """
    Returns Normalize CSS file.
    Included in HTML5 Boilerplate.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_NORMALIZE', DJFRONTEND_NORMALIZE_DEFAULT)

    if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/normalize/%s/normalize.css">' % (settings.DJFRONTEND_STATIC_URL, version)
    return '<link rel="stylesheet" href="%sdjfrontend/css/normalize/%s/normalize.css">' % (settings.STATIC_URL, version)


@register.simple_tag
def djfrontend_fontawesome(version=None):
    """
    Returns Font Awesome CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_FONTAWESOME', DJFRONTEND_FONTAWESOME_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/fontawesome/%s/font-awesome.css">' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            return '<link rel="stylesheet" href="%sdjfrontend/css/fontawesome/%s/font-awesome.min.css">' % (settings.DJFRONTEND_STATIC_URL, version)
        else:
            return '<link rel="stylesheet" href="%sdjfrontend/css/fontawesome/%s/font-awesome.min.css">' % (settings.STATIC_URL, version)


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
        return '<script src="%sdjfrontend/js/modernizr/%s/modernizr.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/%s/modernizr.min.js"></script>' % version,
                '<script>window.Modernizr || document.write(\'<script src="%sdjfrontend/js/modernizr/%s/modernizr.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/%s/modernizr.min.js"></script>' % version,
                '<script>window.Modernizr || document.write(\'<script src="%sdjfrontend/js/modernizr/%s/modernizr.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
            ]
        return '\n'.join(output)


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
        return '<script src="%sdjfrontend/js/jquery/%s/jquery.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % version,
                '<script>window.jQuery || document.write(\'<script src="%sdjfrontend/js/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % version,
                '<script>window.jQuery || document.write(\'<script src="%sdjfrontend/js/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
            ]
        return '\n'.join(output)


@register.simple_tag
def djfrontend_jqueryui(version=None):
    """
    Returns the jQuery UI plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERYUI', DJFRONTEND_JQUERYUI_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<script src="%sdjfrontend/js/jquery/jqueryui/%s/jquery-ui.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js"></script>' % version,
                '<script>window.jQuery.ui || document.write(\'<script src="%sdjfrontend/js/jquery/jqueryui/%s/jquery-ui.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js"></script>' % version,
                '<script>window.jQuery.ui || document.write(\'<script src="%sdjfrontend/js/jquery/jqueryui/%s/jquery-ui.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
            ]
        return '\n'.join(output)


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
        return '<script src="%sdjfrontend/js/jquery/jquery.dataTables/%s/jquery.dataTables.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/datatables/%s/jquery.dataTables.min.js"></script>' % version,
                '<script>window.jQuery.fn.DataTable || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.dataTables/%s/jquery.dataTables.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/datatables/%s/jquery.dataTables.min.js"></script>' % version,
                '<script>window.jQuery.fn.DataTable || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.dataTables/%s/jquery.dataTables.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
            ]
        return '\n'.join(output)


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


    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables.css">' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
            return '<link rel="stylesheet" href="%sdjfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables.min.css">' % (settings.DJFRONTEND_STATIC_URL, version)
        return '<link rel="stylesheet" href="%sdjfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables.min.css">' % (settings.STATIC_URL, version)


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

    if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables_themeroller.min.css">' % (settings.DJFRONTEND_STATIC_URL, version)
    return '<link rel="stylesheet" href="href="%sdjfrontend/css/jquery/jquery.dataTables/%s/jquery.dataTables_themeroller.min.css">' % (settings.STATIC_URL, version)


@register.simple_tag
def djfrontend_jquery_formset(version=None):
    """
    Returns the jQuery Dynamic Formset plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_FORMSET', DJFRONTEND_JQUERY_FORMSET_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<script src="%sdjfrontend/js/jquery/jquery.formset/%s/jquery.formset.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery.formset/%s/jquery.formset.min.js"></script>' % version,
                '<script>window.jQuery.fn.formset || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.formset/%s/jquery.formset.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
                ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery.formset/%s/jquery.formset.min.js"></script>' % version,
                '<script>window.jQuery.fn.formset || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.formset/%s/jquery.formset.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
                ]
        return '\n'.join(output)


@register.simple_tag
def djfrontend_jquery_scrollto(version=None):
    """
    Returns the jQuery ScrollTo plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_SCROLLTO', DJFRONTEND_JQUERY_SCROLLTO_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<script src="%sdjfrontend/js/jquery/jquery.scrollTo/%s/jquery.scrollTo.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/%s/jquery.scrollTo.min.js"></script>' % version,
                '<script>window.jQuery.fn.scrollTo || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.scrollTo/%s/jquery.scrollTo.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
                ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/%s/jquery.scrollTo.min.js"></script>' % version,
                '<script>window.jQuery.fn.scrollTo || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.scrollTo/%s/jquery.scrollTo.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
                ]
        return '\n'.join(output)


@register.simple_tag
def djfrontend_jquery_smoothscroll(version=None):
    """
    Returns the jQuery Smooth Scroll plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if version is None:
        version = getattr(settings, 'DJFRONTEND_JQUERY_SMOOTHSCROLL', DJFRONTEND_JQUERY_SMOOTHSCROLL_DEFAULT)

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<script src="%sdjfrontend/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.js"></script>' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-smooth-scroll/%s/jquery.smooth-scroll.min.js"></script>' % version,
                '<script>window.jQuery.fn.smoothScroll || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-smooth-scroll/%s/jquery.smooth-scroll.min.js"></script>' % version,
                '<script>window.jQuery.fn.smoothScroll || document.write(\'<script src="%sdjfrontend/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
                ]
        return '\n'.join(output)


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

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap.css">' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap.min.css">' % (settings.DJFRONTEND_STATIC_URL, version)
        else:
            return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap.min.css">' % (settings.STATIC_URL, version)


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

    if getattr(settings, 'TEMPLATE_DEBUG', False):
        return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap-theme.css">' % (settings.STATIC_URL, version)
    else:
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False):
            return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap-theme.min.css">' % (settings.DJFRONTEND_STATIC_URL, version)
        else:
            return '<link rel="stylesheet" href="%sdjfrontend/css/twbs/%s/bootstrap-theme.min.css">' % (settings.STATIC_URL, version)


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
        if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.min.js"></script>' % version,
                '<script>window.jQuery.fn.scrollspy || document.write(\'<script src="%sdjfrontend/js/twbs/%s/bootstrap.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, version)
            ]
        else:
            output=[
                '<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.min.js"></script>' % version,
                '<script>window.jQuery.fn.scrollspy || document.write(\'<script src="%sdjfrontend/js/twbs/%s/bootstrap.min.js"><\/script>\')</script>' % (settings.STATIC_URL, version)
            ]
        return '\n'.join(output)
    else:
        if 'popover' in files and 'tooltip' not in files:
            files.append('tooltip')
        for file in files:
            if getattr(settings, 'DJFRONTEND_STATIC_URL', False) and not getattr(settings, 'TEMPLATE_DEBUG', False):
                file = ['<script src="%sdjfrontend/js/twbs/%s/%s.js"></script>' % (settings.DJFRONTEND_STATIC_URL, version, file) for file in files]
            else:
                file = ['<script src="%sdjfrontend/js/twbs/%s/%s.js"></script>' % (settings.STATIC_URL, version, file) for file in files]
        return '\n'.join(file)


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
                    return '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("require", "linker");ga("linker:autoLink", ["%s"]);ga("create", "%s", "auto", {"allowLinker": true});ga("send", "pageview");</script>' % (settings.DJFRONTEND_GA_SETDOMAINNAME, account)
                else:
                    return '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "%s", "%s");ga("send", "pageview");</script>' % (account, settings.DJFRONTEND_GA_SETDOMAINNAME)
            else:
                return '<script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "%s", "auto");ga("send", "pageview");</script>' % account
    else:
        return ''


@register.simple_tag
def djfrontend_ios_fix():
    """
    Returns the iOS-Orientationchange-Fix.
    """
    return '<script>/*! A fix for the iOS orientationchange zoom bug. Script by @scottjehl, rebound by @wilto.MIT / GPLv2 License.*/(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this);</script>'
