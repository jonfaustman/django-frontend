Granularity
-------------

Version 1.0.0 introduced a new level of granularity by including template tags with a default value, which can be overriden in settings, which in turn can be overridden by passing the template tag an argument. This allows you to change default values within settings, while giving a template tag final word.

If you use an optional value other than the ones listed, you will have to add the files into the same directory structure as djfrontend.

+-----------------------------------+---------------------------------------+---------------+-------------------+
|Template tag                       |Setting                                |Default Value  |Optional Value(s)  |
+===================================+=======================================+===============+===================+
|                                   |DJFRONTEND_STATIC_URL                  |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_h5bp_html               |DJFRONTEND_H5BP_HTML                   |en             |ISO 639-1 codes    |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_h5bp_css                |DJFRONTEND_H5BP_CSS                    |5.3.0          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_normalize               |DJFRONTEND_NORMALIZE                   |4.2.0          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_fontawesome             |DJFRONTEND_FONTAWESOME                 |4.6.3          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_modernizr               |DJFRONTEND_MODERNIZR                   |2.8.3          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery                  |DJFRONTEND_JQUERY                      |1.12.4         |2.2.4, 3.1.0       |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jqueryui                |DJFRONTEND_JQUERYUI                    |1.11.4         |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|                                   |DJFRONTEND_JQUERY_DATATABLES_VERSION   |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery_datatables       |DJFRONTEND_JQUERY_DATATABLES           |1.10.12        |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery_datatables_css   |DJFRONTEND_JQUERY_DATATABLES_CSS       |1.10.12        |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery_formset          |DJFRONTEND_JQUERY_FORMSET              |1.2.2          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery_scrollto         |DJFRONTEND_JQUERY_SCROLLTO             |2.1.2          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_jquery_smoothscroll     |DJFRONTEND_JQUERY_SMOOTHSCROLL         |1.7.2          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|                                   |DJFRONTEND_TWBS_VERSION                |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_twbs_css                |DJFRONTEND_TWBS_CSS                    |3.3.7          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_twbs_theme_css          |DJFRONTEND_TWBS_THEME_CSS              |3.3.7          |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_twbs_js                 |DJFRONTEND_TWBS_JS_VERSION             |3.3.7          |                   |
|                                   |DJFRONTEND_TWBS_JS_FILES               |all            |* affix            |
|                                   |                                       |               |* alert            |
|                                   |                                       |               |* button           |
|                                   |                                       |               |* carousel         |
|                                   |                                       |               |* collapse         |
|                                   |                                       |               |* dropdown         |
|                                   |                                       |               |* modal            |
|                                   |                                       |               |* popover          |
|                                   |                                       |               |* scrollspy        |
|                                   |                                       |               |* tab              |
|                                   |                                       |               |* tooltip          |
|                                   |                                       |               |* transition       |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|djfrontend_ga                      |DJFRONTEND_GA                          |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|                                   |DJFRONTEND_GA_SETDOMAINNAME            |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
|                                   |DJFRONTEND_GA_SETALLOWLINKER           |               |                   |
+-----------------------------------+---------------------------------------+---------------+-------------------+
