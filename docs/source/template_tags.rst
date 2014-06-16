Template tags
==============
Use the included djfrontend template tags to suit your needs.

djfrontend
-----------
Loads all the Django Frontend template tags.
::

    {% load djfrontend %}

**Each template tag now has a default value. You only need to include an argument if you wish to change the default.**

djfrontend_h5bp_html
---------------------
Returns HTML tag according to chosen language. The default, 'en' is used if another language is not set.
::

    {% djfrontend_h5bp_html %}

renders:

::

    <html class="no-js" lang="en">

djfrontend_h5bp_css
---------------------
Returns HTML5 Boilerplate CSS file according to version number. The default version is the included '4.3.0'.
::

    {% djfrontend_h5bp_css %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/h5bp/4.3.0/h5bp.css">

djfrontend_normalize
---------------------
Returns Normalize CSS file according to version number. The default version is the included '3.0.1'.
::

    {% djfrontend_normalize %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/normalize/3.0.1/normalize.css">

djfrontend_fontawesome
------------------------
Returns Font Awesome CSS file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The default version is the included '4.1.0'.
::

    {% djfrontend_fontawesome %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/4.1.0/font-awesome.css">

Or without TEMPLATE_DEBUG:

::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/4.1.0/font-awesome.min.css">

djfrontend_modernizr
---------------------
Returns Modernizr JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local callback. The default version is the included '2.8.2'.
::

    {% djfrontend_modernizr %}

renders:

::

    <script src="/static/djfrontend/js/modernizr/2.8.2/modernizr.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.2/modernizr.min.js"></script>' % v,
    <script>window.Modernizr || document.write(\'<script src="static/djfrontend/js/modernizr/2.8.2/modernizr.min.js"><\/script>\')</script>

djfrontend_jquery
------------------
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The default version is the included '1.11.1'.
::

    {% djfrontend_jquery %}

renders:

::

    <script src="/static/djfrontend/js/jquery/1.11.1/jquery.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/djfrontend/js/jquery/1.11.1/jquery.min.js"><\/script>')</script>

djfrontend_jqueryui
---------------------
Returns jQuery UI plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The default version is the included '1.10.4'.
::

    {% djfrontend_jqueryui %}

renders:

::

    <script src="/static/djfrontend/js/jquery/jqueryui/1.10.4/jquery-ui.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>' % v,
    <script>window.jQuery.ui || document.write(\'<script src="/static/djfrontend/js/jquery/jqueryui/1.10.4/jquery-ui.min.js"><\/script>\')</script>

djfrontend_jquery_datatables
-----------------------------
Returns the jQuery DataTables plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback. The default version is the included '1.9.4'.
::

    {% djfrontend_jquery_datatables %}

renders:

::

    <script src="/static/djfrontend/js/jquery/jquery.dataTables/1.10.0/jquery.dataTables.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/datatables/1.10.0/jquery.dataTables.min.js"></script>
    <script>window.jQuery.fn.DataTable || document.write('<script src="/static/djfrontend/js/jquery/jquery.dataTables/1.10.0/jquery.dataTables.min.js"><\/script>')</script>

djfrontend_jquery_datatables_css
----------------------------------
Returns the jQuery DataTables CSS file according to version number. The default version is the included '1.10.0'.
::

    {% djfrontend_jquery_datatables_css %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/jquery/jquery.dataTables/1.10.0/jquery.dataTables.css">

djfrontend_jquery_formset
---------------------------
Returns the jQuery Dynamic Formset plugin JavaScript file according to version number. TTEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback. The default version is the included '1.2'.
::

    {% djfrontend_jquery_formset %}

renders:

::

    <script src="/static/djfrontend/js/jquery/jquery.formset/1.2/jquery.formset.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery.formset/1.2/jquery.formset.min.js"></script>
    <script>window.jQuery.fn.formset || document.write('<script src="/static/djfrontend/js/jquery/jquery.formset/1.2/jquery.formset.min.js"><\/script>')</script>

djfrontend_jquery_scrollto
--------------------------------
Returns the jQuery ScrollTo plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback. The default version is the included '1.4.12'.
::

    {% djfrontend_jquery_scrollto %}

renders:

::

    <script src="/static/djfrontend/js/jquery/jquery.scrollTo/1.4.12/jquery.scrollTo.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/1.4.12/jquery.scrollTo.min.js"></script>
    <script>window.jQuery.fn.scrollTo || document.write('<script src="/static/djfrontend/js/jquery/jquery.scrollTo/1.4.12/jquery.scrollTo.min.js"><\/script>')</script>

djfrontend_jquery_smoothscroll
--------------------------------
Returns the jQuery Smooth Scroll plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback. The default version is the included '1.4.13'.
::

    {% djfrontend_jquery_smoothscroll %}

renders:

::

    <script src="/static/djfrontend/js/jquery/jquery.smooth-scroll/1.4.13/jquery.smooth-scroll.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-smooth-scroll/1.4.13/jquery.smooth-scroll.min.js"></script>
    <script>window.jQuery.fn.smoothScroll || document.write('<script src="/static/djfrontend/js/jquery/jquery.smooth-scroll/1.4.13/jquery.smooth-scroll.min.js"><\/script>')</script>

djfrontend_twbs_css
--------------------
Returns Twitter Bootstrap CSS file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The default version is the included '3.1.1'.
::

    {% djfrontend_twbs_css %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.1.1/bootstrap.css">

Or without TEMPLATE_DEBUG:

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.1.1/bootstrap.min.css">

djfrontend_twbs_theme_css
--------------------------------
Returns Twitter Bootstrap Theme CSS file according to version number. The default version is the included '3.1.1'.
::

    {% djfrontend_twbs_theme_css %}

renders:

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.1.1/bootstrap-theme.css">

Or without TEMPLATE_DEBUG:

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.1.1/bootstrap-theme.min.css">

djfrontend_twbs_js
--------------------
Returns Twitter Bootstrap JavaScript file(s) according to version number and file name(s). The default 'all' returns a concatenated file; full file for TEMPLATE_DEBUG, otherwise returns minified file from cdnjs with local fallback. The default version is the included '3.1.1'.


* affix
* alert
* button
* carousel
* collapse
* dropdown
* modal
* popover (adds tooltip if not included)
* scrollspy
* tab
* tooltip
* transition

Individual files are not minified.
::

    {% djfrontend_twbs_js %}

renders:

::

    <script src="/static/djfrontend/js/twbs/3.1.1/bootstrap.js"></script>

Or without TEMPLATE_DEBUG:

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <script>window.jQuery.fn.scrollspy || document.write('<script src="/static/djfrontend/js/twbs/3.1.1/bootstrap.min.js"><\/script>')</script>

::

    {% bootstrap_js files='alert affix' %}

renders:

::

    <script src="/static/djfrontend/js/twbs/3.1.1/bootstrap-affix.js"></script>
    <script src="/static/djfrontend/js/twbs/3.1.1/bootstrap-alert.js"></script>

Shout out to Ryan Brady and his `Django Bootstrapped <https://github.com/rbrady/django-bootstrapped>`_ for inspiration and initial code.

djfrontend_ga
--------------
Returns Google Analytics Universal Analytics snippet if TEMPLATE_DEBUG is not set. Use DJFRONTEND_GA_SETDOMAINNAME to set domain for multiple, or cross-domain tracking. Set DJFRONTEND_GA_SETALLOWLINKER to use _setAllowLinker method on target site for cross-domain tracking.
::

    <script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "UA-XXXXX-X", "auto");ga("send", "pageview");</script>

Or with DJFRONTEND_GA_SETDOMAINNAME set:

::

    <script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "UA-XXXXX-X", "example.com");ga("send", "pageview");</script>

Or with DJFRONTEND_GA_SETDOMAINNAME and DJFRONTEND_GA_SETALLOWLINKER set:

::

    <script>(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("require", "linker");ga("linker:autoLink", ["example.com"]);ga("create", "UA-XXXXX-X", "auto", {"allowLinker": true});ga("send", "pageview");</script>

djfrontend_ios_fix
--------------------
Returns the iOS-Orientationchange-Fix.
::

    <script>/*! A fix for the iOS orientationchange zoom bug. Script by @scottjehl, rebound by @wilto.MIT / GPLv2 License.*/(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this);</script>
