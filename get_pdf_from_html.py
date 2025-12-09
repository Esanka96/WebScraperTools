import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import json
import urllib.parse

def get_soup(url):
    response = requests.post(url, headers=headers,json=payload)
    return response.json()


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

payload = {
"html":
""""
<style>#pf-content img, #pf-content figure { margin: 1em auto !important; clear: both !important; display: block !important; float: none !important; }</style>

<html lang="it-IT" itemscope="" itemtype="http://schema.org/WebSite" prefix="og: http://ogp.me/ns#" class="csstransforms csstransforms3d csstransitions skrollr skrollr-desktop"><!--<![endif]--><head>
        <meta charset="UTF-8">
        <title>URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY | Urbanities is an open-access peer-reviewed international academic journal launched in 2011</title>

        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
            <script src="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/assets/js/html5shiv.js"></script>
        <![endif]-->
        <!--[if IE 8]>
            <link rel="stylesheet" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/assets/css/ie8.css">
        <![endif]-->
        <!--[if IE 7]>
            <link rel="stylesheet" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/framework/Pagebuilder/css/font-awesome-ie7.min.css">
        <![endif]-->

        <link rel="shortcut icon" href="https://www.anthrojournal-urbanities.com/wp-content/uploads/2015/11/favicon-u.png"><meta name="viewport" content="width=device-width, initial-scale=1.0"><div class="fit-vids-style" id="fit-vids-style" style="display: none;">­<style>                 .fluid-width-video-wrapper {                   width: 100%;                                position: relative;                         padding: 0;                              }                                                                                       .fluid-width-video-wrapper iframe,          .fluid-width-video-wrapper object,          .fluid-width-video-wrapper embed {             position: absolute;                         top: 0;                                     left: 0;                                    width: 100%;                                height: 100%;                            }                                         </style></div><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-PF265TCPCH&amp;cx=c&amp;_slc=1"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://ssl.google-analytics.com/ga.js"></script><script>var footer = false, colorful_footer = false, non_sticky_menu = false; responsive = true;</script>
<!-- All in One SEO Pack 2.2.7.4 by Michael Torbert of Semper Fi Web Design[684,831] -->
<link rel="canonical" href="https://www.anthrojournal-urbanities.com/">
<meta property="og:title" content="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.anthrojournal-urbanities.com/">
<meta property="og:image" content="https://www.anthrojournal-urbanities.com/wp-content/plugins/all-in-one-seo-pack/images/default-user-image.png">
<meta property="og:site_name" content="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY">
<meta property="fb:admins" content="621150871266331">
<meta property="og:description" content="Urbanities is an open-access peer-reviewed international academic journal launched in 2011">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY">
<meta name="twitter:description" content="Urbanities is an open-access peer-reviewed international academic journal launched in 2011">
<meta name="twitter:image" content="https://www.anthrojournal-urbanities.com/wp-content/plugins/all-in-one-seo-pack/images/default-user-image.png">
<meta itemprop="image" content="https://www.anthrojournal-urbanities.com/wp-content/plugins/all-in-one-seo-pack/images/default-user-image.png">
<script type="application/ld+json">
{ "@context" : "http://schema.org",
  "@type" : "Organization",
  "name" : "",
  "url" : "https://www.anthrojournal-urbanities.com",
  "sameAs" : ["https://www.facebook.com/anthrojournal.urbanities/"] 
}
</script>
		<script type="text/javascript">
		  var _gaq = _gaq || [];
		  _gaq.push(['_setAccount', 'UA-64939589-1']);
		  _gaq.push(['_setAllowLinker', true]);
		  _gaq.push(['_setDomainName', 'anthrojournal-urbanities']);
		  _gaq.push(['_trackPageview']);
		  (function() {
		    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		  })();
		</script>
		<script type="text/javascript">
		function recordOutboundLink(link, category, action) {
					_gat._getTrackerByName()._trackEvent(category, action);
					if ( link.target == '_blank' ) return true;
			setTimeout('document.location = "' + link.href + '"', 100);
			return false;
		}
			/* use regular Javascript for this */
			function getAttr(ele, attr) {
				var result = (ele.getAttribute && ele.getAttribute(attr)) || null;
				if( !result ) {
					var attrs = ele.attributes;
					var length = attrs.length;
					for(var i = 0; i < length; i++)
					if(attr[i].nodeName === attr) result = attr[i].nodeValue;
				}
				return result;
			}
			
			function aiosp_addLoadEvent(func) {
			  var oldonload = window.onload;
			  if (typeof window.onload != 'function') {
			    window.onload = func;
			  } else {
			    window.onload = function() {
			      if (oldonload) {
			        oldonload();
			      }
			      func();
			    }
			  }
			}
			
			function aiosp_addEvent(element, evnt, funct){
			  if (element.attachEvent)
			   return element.attachEvent('on'+evnt, funct);
			  else
			   return element.addEventListener(evnt, funct, false);
			}

			aiosp_addLoadEvent(function () {
				var links = document.getElementsByTagName('a');
				for (var x=0; x < links.length; x++) {
					if (typeof links[x] == 'undefined') continue;
					aiosp_addEvent( links[x], 'onclick', function () {
						var mydomain = new RegExp(document.domain, 'i');
						href = getAttr(this, 'href');
						if (href && href.toLowerCase().indexOf('http') === 0 && !mydomain.test(href)) {
							recordOutboundLink(this, 'Outbound Links', href);
						}
					});
				}
			});
		</script>
<!-- /all in one seo pack -->
<link rel="alternate" type="application/rss+xml" title="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY » Feed" href="https://www.anthrojournal-urbanities.com/feed/">
<link rel="alternate" type="application/rss+xml" title="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY » Feed dei commenti" href="https://www.anthrojournal-urbanities.com/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY » Home Feed dei commenti" href="https://www.anthrojournal-urbanities.com/home/feed/">
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/72x72\/","ext":".png","source":{"concatemoji":"https:\/\/www.anthrojournal-urbanities.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.5.32"}};
			!function(e,o,t){var a,n,r;function i(e){var t=o.createElement("script");t.src=e,t.type="text/javascript",o.getElementsByTagName("head")[0].appendChild(t)}for(r=Array("simple","flag","unicode8","diversity"),t.supports={everything:!0,everythingExceptFlag:!0},n=0;n<r.length;n++)t.supports[r[n]]=function(e){var t,a,n=o.createElement("canvas"),r=n.getContext&&n.getContext("2d"),i=String.fromCharCode;if(!r||!r.fillText)return!1;switch(r.textBaseline="top",r.font="600 32px Arial",e){case"flag":return r.fillText(i(55356,56806,55356,56826),0,0),3e3<n.toDataURL().length;case"diversity":return r.fillText(i(55356,57221),0,0),a=(t=r.getImageData(16,16,1,1).data)[0]+","+t[1]+","+t[2]+","+t[3],r.fillText(i(55356,57221,55356,57343),0,0),a!=(t=r.getImageData(16,16,1,1).data)[0]+","+t[1]+","+t[2]+","+t[3];case"simple":return r.fillText(i(55357,56835),0,0),0!==r.getImageData(16,16,1,1).data[0];case"unicode8":return r.fillText(i(55356,57135),0,0),0!==r.getImageData(16,16,1,1).data[0]}return!1}(r[n]),t.supports.everything=t.supports.everything&&t.supports[r[n]],"flag"!==r[n]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[r[n]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(a=function(){t.readyCallback()},o.addEventListener?(o.addEventListener("DOMContentLoaded",a,!1),e.addEventListener("load",a,!1)):(e.attachEvent("onload",a),o.attachEvent("onreadystatechange",function(){"complete"===o.readyState&&t.readyCallback()})),(a=t.source||{}).concatemoji?i(a.concatemoji):a.wpemoji&&a.twemoji&&(i(a.twemoji),i(a.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel="stylesheet" id="layerslider-css" href="https://www.anthrojournal-urbanities.com/wp-content/plugins/LayerSlider/static/css/layerslider.css?ver=5.1.1" type="text/css" media="all">
<link rel="stylesheet" id="ls-google-fonts-css" href="https://fonts.googleapis.com/css?family=Lato:100,300,regular,700,900|Open+Sans:300|Indie+Flower:regular|Oswald:300,regular,700&amp;subset=latin,latin-ext" type="text/css" media="all">
<link rel="stylesheet" id="contact-form-7-css" href="https://www.anthrojournal-urbanities.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=4.3" type="text/css" media="all">
<link rel="stylesheet" id="rs-plugin-settings-css" href="https://www.anthrojournal-urbanities.com/wp-content/plugins/revslider/rs-plugin/css/settings.css?rev=4.3.6&amp;ver=4.5.32" type="text/css" media="all">
<style id="rs-plugin-settings-inline-css" type="text/css">
.tp-caption a {
color:#ff7302;
text-shadow:none;
-webkit-transition:all 0.2s ease-out;
-moz-transition:all 0.2s ease-out;
-o-transition:all 0.2s ease-out;
-ms-transition:all 0.2s ease-out;
}

.tp-caption a:hover {
color:#ffa902;
}
</style>
<link rel="stylesheet" id="rs-plugin-captions-css" href="https://www.anthrojournal-urbanities.com/wp-content/plugins/revslider/rs-plugin/css/captions.php?rev=4.3.6&amp;ver=4.5.32" type="text/css" media="all">
<link rel="stylesheet" id="blox-style-css" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/framework/Pagebuilder/css/?ver=4.5.32" type="text/css" media="all">
<link rel="stylesheet" id="themeton-google-font-menu-css" href="https://fonts.googleapis.com/css?family=Montserrat%3A300%2C400%2C700%2C800&amp;ver=4.5.32" type="text/css" media="all">
<link rel="stylesheet" id="themeton-css-grid-css" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/assets/css/bootstrap.css?ver=4.5.32" type="text/css" media="all">
<link rel="stylesheet" id="mana-style-css" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/style.css?ver=4.5.32" type="text/css" media="all">
<link rel="stylesheet" id="themeton-css-responsive-css" href="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/assets/css/responsive.css?ver=4.5.32" type="text/css" media="all">
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-includes/js/jquery/jquery.js?ver=1.12.4"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/LayerSlider/static/js/layerslider.kreaturamedia.jquery.js?ver=5.1.1"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/LayerSlider/static/js/greensock.js?ver=1.11.2"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/LayerSlider/static/js/layerslider.transitions.js?ver=5.1.1"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/revslider/rs-plugin/js/jquery.themepunch.plugins.min.js?rev=4.3.6&amp;ver=4.5.32"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/revslider/rs-plugin/js/jquery.themepunch.revolution.min.js?rev=4.3.6&amp;ver=4.5.32"></script>
<link rel="https://api.w.org/" href="https://www.anthrojournal-urbanities.com/wp-json/">
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.anthrojournal-urbanities.com/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.anthrojournal-urbanities.com/wp-includes/wlwmanifest.xml"> 
<meta name="generator" content="WordPress 4.5.32">
<link rel="shortlink" href="https://www.anthrojournal-urbanities.com/">
<link rel="alternate" type="application/json+oembed" href="https://www.anthrojournal-urbanities.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.anthrojournal-urbanities.com%2F">
<link rel="alternate" type="text/xml+oembed" href="https://www.anthrojournal-urbanities.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.anthrojournal-urbanities.com%2F&amp;format=xml">
<script type="text/javascript">
			var metro_frontend_ajax = "https://www.anthrojournal-urbanities.com/wp-admin/admin-ajax.php";
		  </script><script>
                var blox_plugin_path = "https://www.anthrojournal-urbanities.com/wp-content/themes/mana/framework/Pagebuilder/";
            </script>		<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>
		<link rel="icon" href="https://www.anthrojournal-urbanities.com/wp-content/uploads/2022/04/cropped-WebImage-32x32.png" sizes="32x32">
<link rel="icon" href="https://www.anthrojournal-urbanities.com/wp-content/uploads/2022/04/cropped-WebImage-192x192.png" sizes="192x192">
<link rel="apple-touch-icon-precomposed" href="https://www.anthrojournal-urbanities.com/wp-content/uploads/2022/04/cropped-WebImage-180x180.png">
<meta name="msapplication-TileImage" content="https://www.anthrojournal-urbanities.com/wp-content/uploads/2022/04/cropped-WebImage-270x270.png">
<!-- CSS from Theme Options Panel -->
<style type="text/css">
body{background-color:#ffffff;}
#message_bar{background-color:#53a67b;}
#header{background-color:#ffffff;}
.wide_menu{background-color:#ffffff}.wide_menu #searchform div#s_input:after{border-left-color:#ffffff}.wide_menu #searchform div#s_input:before{border-left-color:rgba(0,0,0,.2)}
#top_bar,#top_bar ul.social_icon li a::after{background-color:#293076;}
#sub_footer,#sub_footer ul.social_icon li a::after{background-color:#1a1f20;}
#footer{background-color:#2e3739;}
body{font-size:13px}
body{font-family:arial}
body{font-style:normal}
.menu{font-family:'Montserrat'}
h1,h2,h3,h4,h5,h6{font-family:'Montserrat'}
body{font-family:'Montserrat'}
    /*woocommerce*/
    footer.cart_buttons a.button,
    /*elements*/
    .post-filter > span a,
    .post-filter > span:hover a::before {
        color: #293076;
    }
    /*style*/
    ul.menu ul .menu_item .new:after,
    #feature, #error-404 input[type="submit"], 
    input[type="button"], input[type="reset"], input[type="submit"],
    .tt_widget_thumb,
    .tagcloud a,
    .widget_social ul li a, ul.social_icon li a,
    .widget_pages ul li.current_page_item, .widget ul.menu li.menu.current_menu_item,
    .widget_archive ul li span, .widget_categories ul li span, .widget_product_categories ul li span,
    /*woocommere custom*/
    .woocommerce span.onsale,
    .woocommerce-page span.onsale,

    .woocommerce ul.products li.product .entry_product:hover,
    .woocommerce-page ul.products li.product .entry_product:hover,
    .woocommerce-page .entry_product:hover,

    footer.cart_buttons a.button,

    .woocommerce a.button,
    .woocommerce-page a.button,
    .woocommerce button.button,
    .woocommerce-page button.button,
    .woocommerce input.button,
    .woocommerce-page input.button,
    .woocommerce #respond input#submit,
    .woocommerce-page #respond input#submit,
    .woocommerce #content input.button,
    .woocommerce-page #content input.button,

    .woocommerce a.button.alt,
    .woocommerce-page a.button.alt,
    .woocommerce button.button.alt,
    .woocommerce-page button.button.alt,
    .woocommerce input.button.alt,
    .woocommerce-page input.button.alt,
    .woocommerce #respond input#submit.alt,
    .woocommerce-page #respond input#submit.alt,
    .woocommerce #content input.button.alt,
    .woocommerce-page #content input.button.alt,

    .woocommerce .addresses .title .edit,
    .woocommerce-page .addresses .title .edit,

    .price_slider_wrapper .ui-slider-handle,

    .woocommerce span.onsale,
    .woocommerce-page span.onsale,

    /*elements*/
    .jp-play-bar,
    .blox_elem_button_default,
    .blox_elem_divider.style7,
    .blox_elem_divider.style8{
        background-color: #293076;
    }
    /*style*/
    #error-404 input[type="text"], article.portfolio,
    /*woocommerce*/
    .woocommerce nav.woocommerce-pagination ul,
    .woocommerce-page nav.woocommerce-pagination ul,
    .woocommerce #content nav.woocommerce-pagination ul,
    .woocommerce-page #content nav.woocommerce-pagination ul,

    .woocommerce ul.products li.product .entry_product:hover,
    .woocommerce-page ul.products li.product .entry_product:hover,
    .woocommerce-page .entry_product:hover,
    /*elements*/
    .blog_big .entry_content_big_container,
    .blog_big.blog_list_view,
    .blog_medium,
    .grid_entry article.entry:hover,
    .grid_entry .centered_portfolio article.entry,
    .format_quote blockquote,
    .grid_pager .tt-pager-pagination,
    .metro .tt-pager-pagination,
    .post-filter,
    .blox_gallery.gallery_layout_slider .gallery_pager span.cycle-pager-active{
        border-color: #293076;
    }
    .blox_elem_image_frame:hover .blox_elem_image_frame_hover,
    .blox_gallery .gallery_preview .preview_panel .hover, .blox_gallery .gallery_thumbs .hover,
    .entry_media:hover .entry_hover{background-color:rgba(41,48,118,0.9)}
    #feature h1.page_title, #feature a, #feature{ color:#FFFFFF !important; }#feature{ background-color:#293076; }.wide_menu ul.menu li a,nav.mainmenu a{color:#293076}
.wide_menu ul.menu li a:hover,nav.mainmenu ul.menu li a:hover,ul.menu li a:hover,.icon_menu ul.menu li a:hover, ul.menu li a.active{color:#293076}
a{color:#293076}
a:hover{color:#293076}
h1,h2,h3,h4,h5,h6{color:#666666} h3.widget_title{color:#666666} #footer h3.widget_title{color:#00b4cc} .widget_social ul li a::after, ul.social_icon li a::after {
    font-size: 19px;
}

.wide_menu ul.menu li a {
    padding: 20px 8px;
}

.wide_menu ul.menu li a {
    font-size: 11px !important;
}

.blog_big .entry_meta ul, ul.top_meta, .medium_left_image .entry_meta ul, .medium_right_image .entry_meta ul {
display: none;
}

.grid_entry article.entry .entry_meta {
display: none;
}

.blox_elem_image_frame:hover .blox_elem_image_frame_hover, .blox_gallery .gallery_preview .preview_panel .hover, .blox_gallery .gallery_thumbs .hover, .entry_media:hover .entry_hover {
display: none !important;
}


.mainmenu ul.menu li ul li:last-child a {
border: 0px;
color: #333;
font-weight: 100;
}

.mainmenu ul.menu .megamenu .menu_column h3 {
display: none;
}


input[type="submit"] {
border: none;
}


.mainmenu ul.menu li ul li a, .icon_menu ul.menu li ul li a, .default_menu ul.menu li ul li a, .metro_menu ul.menu li ul li a {
height: auto;
margin: 0px;
padding: 0px;
line-height: 1em;
font-size: 11px;
font-weight: normal;
text-transform: none;
text-align: left;
color: #999;
background-color: transparent;
border: 0px;
font-size: 14px;
}





.blox_elem_button_default:hover {
color: #FFF;
border-color: rgba(0,0,0,.15);
background-color: #000;
text-shadow: 0 1px 1px rgba(0, 0, 0, .1);
}

p
{
font-size:16px;
}

.default_menu .page_item_has_children .menu_text:after, .wide_menu .page_item_has_children .menu_text:after {
content: "f078";
font-family: fontawesome;
font-size: .5em;
position: relative;
top: -.3em;
margin-left: 1em;
display: none !important;
}

#feature {
background-color: #293076;
}

h1
{
color: #293076 ;
}



.tt_breadcrumb > span {
font-size: 11px;
line-height: 11px;
text-transform: uppercase;
display: inline;
color: #fff;
}


.dark_sub_menu .mainmenu ul.menu li ul > li .menu_arrow {
background-color: transparent;
border: transparent;
border-left-color: transparent;
border-top-color: transparent;
}

span.wpcf7-list-item {
margin-right: 30px;
margin-left: 0;
}

.wpcf7 form.wpcf7-form p {
font-weight: 600;
margin: 0 0 10px 0 !important;
}

.wide_menu ul.menu li a {

border-left: 1px solid rgba(0,0,0,0.1);
display: block;
text-transform: none;
font-size: 15px;
line-height: 15px;
font-weight: 300;
}

.form-all {
margin: inherit !important;
padding-top: 20px 16px;
width: 650px;
color: #293076 !important;
font-family: 'Trebuchet MS';
font-size: 14px;
}

.dark_sub_menu .mainmenu ul.menu li ul li {
background-color: #fff;
padding: 10px 18px;
font-size:14px !important;
text-transform: none !important;
}

.menu li a:hover
{
color: #293076!important;
}


h3
{
color: #333 !important;
}

body
{
font-size:15px;}

.spedizionedue
{
	height:0;
	overflow:hidden;
	}
	
.spedizione:hover spedizionedue
{
	height:auto;
	overflow:visible;
	}
</style>
    </head>
    <body class="home page page-id-2 page-template-default" style="">
        <div class="wrapper">
                <!-- Start Top Bar -->
    <div id="top_bar" class="light">
        <div class="container">
            <div class="row">
                <div class="col-lg-6 col-sm-6 col-xs-12 col-md-6">
                    <div class="top_left">
                                            </div><!-- end top_left -->
                </div>
                <div class="col-lg-6 col-sm-6 col-xs-12 col-md-6">
                    <div class="top_right">
                        <ul class="social_icon"><li><a class="facebook" href="https://www.facebook.com/anthrojournal.urbanities" data-attr="" target="_blank"></a></li><li><a class="googleplus" href="https://plus.google.com/114651015280079020901/about" data-attr="" target="_blank"></a></li></ul>                    </div><!-- end top_right -->
                </div>
            </div><!-- end row -->
        </div><!-- end container -->
    </div><!-- End Top Bar -->
        <!-- Start Header -->
    <header id="header">

        <!-- Start Container -->
        <div class="container">
            <div class="row">
                <div class="col-xs-12 col-md-12 col-lg-3 col-sm-4">
                    <div id="logo"><a href="https://www.anthrojournal-urbanities.com"><img src="https://www.anthrojournal-urbanities.com/wp-content/uploads/2018/04/urbanities-logo.png" alt="URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY" class="normal"></a><h1 style="display:none"><a href="https://www.anthrojournal-urbanities.com">URBANITIES - JOURNAL OF URBAN ETHNOGRAPHY</a></h1></div>                </div>
                                    <div class="col-xs-12 col-md-12 col-lg-9 col-sm-8">
                        <div class="custom_box hidden-xs hidden-sm visible-md visible-lg align_right">
                                                    </div>
                    </div>
                                            <a id="mobile-menu-expand-collapse" href="#" class="show-mobile-menu hidden-md hidden-lg"></a></div>
        </div>
        <!-- End Container -->

    </header><nav class="" id="tt-mobile-menu" style="display: none;"><ul class="menu" style=""><li id="menu-item-62" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item menu-item-home menu-item-62" style="">
                        <a href="https://www.anthrojournal-urbanities.com/" style="">
                        	<span class=""></span>
                            <span class="menu_text">HOME</span>
                            
                        </a>
                        
                      </li><li id="menu-item-52" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52 has-children" style="">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/" style="">
                        	<span class=""></span>
                            <span class="menu_text">ABOUT THE JOURNAL</span>
                            
                        </a>
                        <ul style="" class="sub-menu"><li id="menu-item-53" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-53" style="">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/abstracting-indexing-information/">
                        	<span class=""></span>
                            Abstracting &amp; Indexing information
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li><li id="menu-item-54" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-54" style="">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/aims-and-scope/">
                        	<span class=""></span>
                            Aims and Scope
                            
                        </a>
                        
                      </li><li id="menu-item-55" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-55" style="">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/editorial-board/">
                        	<span class=""></span>
                            Editorial Board
                            
                        </a>
                        
                      </li><li id="menu-item-56" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-56" style="">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/publication-ethics-and-malpractice-statement/">
                        	<span class=""></span>
                            Publication Ethics and Malpractice Statement
                            
                        </a>
                        
                      </li></ul><span class="collapse">&nbsp;</span>
                      </li><li id="menu-item-70" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-70 has-children" style="">
                        <a href="https://www.anthrojournal-urbanities.com/journal-issues/" style="">
                        	<span class=""></span>
                            <span class="menu_text">JOURNAL ISSUES</span>
                            
                        </a>
                        <ul style="" class="sub-menu"><li id="menu-item-71" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71" style="">
                        <a href="https://www.anthrojournal-urbanities.com/journal-issues/all-volumes-issues-and-supplements/">
                        	<span class=""></span>
                            All Volumes: Issues &amp; Supplements
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li></ul><span class="collapse">&nbsp;</span>
                      </li><li id="menu-item-1203" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1203" style="">
                        <a href="https://www.anthrojournal-urbanities.com/the-ius-supplements/" style="">
                        	<span class=""></span>
                            <span class="menu_text">The IUS SUPPLEMENTS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-63" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-63 has-children" style="">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/" style="">
                        	<span class=""></span>
                            <span class="menu_text">INFORMATION &amp; GUIDELINES</span>
                            
                        </a>
                        <ul style="" class="sub-menu"><li id="menu-item-64" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-64" style="">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/contacts/">
                        	<span class=""></span>
                            Contacts
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li><li id="menu-item-66" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-66" style="">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/contributors-guidelines/">
                        	<span class=""></span>
                            Contributors Guidelines
                            
                        </a>
                        
                      </li><li id="menu-item-67" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-67" style="">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/how-to-submit/">
                        	<span class=""></span>
                            How to Submit
                            
                        </a>
                        
                      </li><li id="menu-item-69" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-69" style="">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/publication-agreement/">
                        	<span class=""></span>
                            Authors Copyright – First Publisher Agreement
                            
                        </a>
                        
                      </li></ul><span class="collapse">&nbsp;</span>
                      </li><li id="menu-item-68" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-68" style="">
                        <a href="https://www.anthrojournal-urbanities.com/permissions/" style="">
                        	<span class=""></span>
                            <span class="menu_text">PERMISSIONS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1210" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1210" style="">
                        <a href="https://www.anthrojournal-urbanities.com/useful-linksresources/" style="">
                        	<span class=""></span>
                            <span class="menu_text">LINKS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-57" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-57" style="">
                        <a href="https://www.anthrojournal-urbanities.com/advertise/" style="">
                        	<span class=""></span>
                            <span class="menu_text">ADVERTISE</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1207" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1207" style="">
                        <a href="https://www.anthrojournal-urbanities.com/recommend-to-libraries/" style="">
                        	<span class=""></span>
                            <span class="menu_text">RECOMMEND TO LIBRARIES</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1592" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1592" style="">
                        <a href="https://www.anthrojournal-urbanities.com/donations/" style="">
                        	<span class=""></span>
                            <span class="menu_text">DONATIONS</span>
                            
                        </a>
                        
                      </li></ul></nav>

    <!-- Start Wide Menu -->
    <div class="sticky-wrapper" style=""><div class="wide_menu">
        <!-- Start Container -->
        <div class="container">
            <div class="row">
                                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
                    <nav class="mainmenu hidden-xs hidden-sm visible-md visible-lg"><ul class="menu"><li id="menu-item-62" class="  menu-item menu-item-type-post_type menu-item-object-page current-menu-item menu-item-home menu-item-62">
                        <a href="https://www.anthrojournal-urbanities.com/" style="">
                        	<span class=""></span>
                            <span class="menu_text">HOME</span>
                            
                        </a>
                        
                      </li><li id="menu-item-52" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52 page_item_has_children">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/" style="">
                        	<span class=""></span>
                            <span class="menu_text">ABOUT THE JOURNAL</span>
                            
                        </a>
                        <ul><li id="menu-item-53" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-53">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/abstracting-indexing-information/">
                        	<span class=""></span>
                            Abstracting &amp; Indexing information
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li><li id="menu-item-54" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-54">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/aims-and-scope/">
                        	<span class=""></span>
                            Aims and Scope
                            
                        </a>
                        
                      </li><li id="menu-item-55" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-55">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/editorial-board/">
                        	<span class=""></span>
                            Editorial Board
                            
                        </a>
                        
                      </li><li id="menu-item-56" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-56">
                        <a href="https://www.anthrojournal-urbanities.com/about-the-journal/publication-ethics-and-malpractice-statement/">
                        	<span class=""></span>
                            Publication Ethics and Malpractice Statement
                            
                        </a>
                        
                      </li></ul>
                      </li><li id="menu-item-70" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-70 page_item_has_children">
                        <a href="https://www.anthrojournal-urbanities.com/journal-issues/" style="">
                        	<span class=""></span>
                            <span class="menu_text">JOURNAL ISSUES</span>
                            
                        </a>
                        <ul><li id="menu-item-71" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-71">
                        <a href="https://www.anthrojournal-urbanities.com/journal-issues/all-volumes-issues-and-supplements/">
                        	<span class=""></span>
                            All Volumes: Issues &amp; Supplements
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li></ul>
                      </li><li id="menu-item-1203" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-1203">
                        <a href="https://www.anthrojournal-urbanities.com/the-ius-supplements/" style="">
                        	<span class=""></span>
                            <span class="menu_text">The IUS SUPPLEMENTS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-63" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-63 page_item_has_children">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/" style="">
                        	<span class=""></span>
                            <span class="menu_text">INFORMATION &amp; GUIDELINES</span>
                            
                        </a>
                        <ul><li id="menu-item-64" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-64">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/contacts/">
                        	<span class=""></span>
                            Contacts
                            
                        </a>
                        
                      <span class="menu_arrow"></span></li><li id="menu-item-66" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-66">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/contributors-guidelines/">
                        	<span class=""></span>
                            Contributors Guidelines
                            
                        </a>
                        
                      </li><li id="menu-item-67" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-67">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/how-to-submit/">
                        	<span class=""></span>
                            How to Submit
                            
                        </a>
                        
                      </li><li id="menu-item-69" class=" menu-item menu-item-type-post_type menu-item-object-page menu-item-69">
                        <a href="https://www.anthrojournal-urbanities.com/information-guidelines/publication-agreement/">
                        	<span class=""></span>
                            Authors Copyright – First Publisher Agreement
                            
                        </a>
                        
                      </li></ul>
                      </li><li id="menu-item-68" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-68">
                        <a href="https://www.anthrojournal-urbanities.com/permissions/" style="">
                        	<span class=""></span>
                            <span class="menu_text">PERMISSIONS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1210" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-1210">
                        <a href="https://www.anthrojournal-urbanities.com/useful-linksresources/" style="">
                        	<span class=""></span>
                            <span class="menu_text">LINKS</span>
                            
                        </a>
                        
                      </li><li id="menu-item-57" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-57">
                        <a href="https://www.anthrojournal-urbanities.com/advertise/" style="">
                        	<span class=""></span>
                            <span class="menu_text">ADVERTISE</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1207" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-1207">
                        <a href="https://www.anthrojournal-urbanities.com/recommend-to-libraries/" style="">
                        	<span class=""></span>
                            <span class="menu_text">RECOMMEND TO LIBRARIES</span>
                            
                        </a>
                        
                      </li><li id="menu-item-1592" class="  menu-item menu-item-type-post_type menu-item-object-page menu-item-1592">
                        <a href="https://www.anthrojournal-urbanities.com/donations/" style="">
                        	<span class=""></span>
                            <span class="menu_text">DONATIONS</span>
                            
                        </a>
                        
                      </li></ul></nav>                </div>
                            </div>
        </div>
        <!-- End Container -->
    </div></div>
    <!-- End Wide Menu -->
    <!-- Start Content -->
<section id="content" permalink="https://www.anthrojournal-urbanities.com/" class="section-2  ">
    <!-- Start Container -->
    <div class="container">
        <div class="row">

            <div class="col-xs-12 col-md-9 col-lg-9 col-sm-8">
                <div id="primary" class="content">
                    <article>
                        <div class="entry_content">
                            <div class="wrapper  " style="">
				<div class="row "><div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><div class="blox_element tt_text_content  ">
<h1>Urbanities – Journal of &nbsp;Urban Ethnography</h1>
<p>&nbsp;</p>
<p><strong>Urbanities</strong> is an open-access peer-reviewed international academic journal founded in 2010 on the initiative of Professor Italo Pardo, and launched online in 2011.</p>
<p><strong>Urbanities</strong><em><strong>&nbsp;</strong></em>is totally free of charge. Authors do not pay to publish and all content of the journal is available without charge to the users and their institutions. Users can read, download or print the full texts of all contributions without prior permission from&nbsp;<strong>Urbanities</strong>.</p>
<p><strong>Urbanities&nbsp;</strong>is published on-line twice a year, in May and in November, in association with and the support of the <span style="color: #666262;"><em><strong><a style="color: #666262;" href="https://www.internationalurbansymposium.com/">International Urban Symposium-IUS</a></strong></em>, and is endorsed by the Commission on Urban Anthropology (CUA).</span></p>
<p><strong>Urbanities</strong> publishes original ethnographically-based studies at the forefront of anthropology, sociology and other social sciences and the humanities. Urbanities aims at exploring new trends and debates in Urban Ethnography that promote high-quality critical scholarship and at highlighting the contribution of urban research to the broader society.</p>
<p><strong>Urbanities</strong>&nbsp;also publishes <em>Special Issues</em> and&nbsp;<span style="text-decoration: underline;"><em><a style="color: #666262; text-decoration: underline;" href="https://www.anthrojournal-urbanities.com/the-ius-supplements/">IUS Supplements</a></em></span>&nbsp;to volumes. The IUS Supplements are edited collections included in the main journal volume and published accordingly on the website. Special Issues and IUS Supplements are peer-reviewed to the same editorial standards as the journal’s regular issues, are indexed and citable in the same way as all articles published in regular journal issues and are open-access; they, too, can be read and downloaded free of charge.</p>
<p><strong>Urbanities</strong> welcomes contributions from new and established scholars, researchers and practitioners who can make a valuable contribution to the subject matter and to international scholarship.</p>
<p><strong>Urbanities</strong> publishes full-length articles, review articles, comments, book reviews, film and video reviews, obituaries and news on research done and in-progress. In order to stimulate debate, Urbanities encourages publication of letters and comments. It also publishes brief announcements of forthcoming conferences and other relevant events, conference reports, university courses and jobs; announcements from Publishing Houses.</p>
<p><strong>ISSN: 2239-5725</strong></p>
<p>&nbsp;</p></div></div></div>
			</div>
                                                    </div>

                        
                        
                    </article>
                                    </div><!-- end #primary -->
            </div><!-- end grid -->

            <div class="col-xs-12 col-md-3 col-lg-3 col-sm-4"><div id="sidebar" class="sidebar_area right_sidebar" style="height: 1357px;"><div id="search-3" class="widget widget_search"><form role="search" method="get" id="searchform" action="https://www.anthrojournal-urbanities.com/">
    <div>
    <input type="submit" id="searchsubmit" value="">
    <input type="text" value="" name="s" id="s" placeholder="Search">    
    </div>
    </form></div><div id="text-2" class="widget widget_text">			<div class="textwidget"><p style="color: rgb(0,111,201); font-size:11px;     line-height: 12px;">THIS  TITLE  IS  INDEXED  IN:<br>
</p><p style="color: rgb(0,111,201); font-size:10px;     line-height: 12px;">SCOPUS<br>
Thomson Reuters Master Journal List<br>
ERIH PLUS<br>
ROAD<br>
Academic Keys Journal Database<br>
International Journal Guide-AJE;<br>
openaccessarticles.com<br>
InfoBase Index<br>
ASA Publishing Options Database<br>
SHERPA/RoMEO</p>
<p style="color: rgb(0,111,201); font-size:10px;     line-height: 12px;"> 
The Association of Social Anthropologists of the UK &amp; the Commonwealth,<br>
and the American Sociological Association<br>
 recommend Urbanities for article submissions</p>

<h4>Support the Journal</h4>

<p><img src="https://www.anthrojournal-urbanities.com/new/wp-content/uploads/2015/11/urbanities.png"></p>
<p>&nbsp;</p>
<h2 style="color:#293074"><a href="https://www.anthrojournal-urbanities.com/new/donations/">DONATE</a></h2>


<p style="color: #808080; font-size:12px;     line-height: 12px;">Urbanities provides readers with free and open access to excellent new scholarship. There are no processing or publication fees for authors. Urbanities relies on donations to fund its operations. If you wish to support Urbanities, click the Donate button above and follow the simple instructions. 
Thank you.</p>

<p>&nbsp;</p>
<h5><a href="https://www.facebook.com/anthrojournal.urbanities"><strong>FOLLOW US ON FACEBOOK<h5><span style="color: #6363e6;"><h1><strong>f<strong></strong></strong></h1><strong><strong>

</strong></strong></span></h5></strong></a></h5></div><a href="https://www.facebook.com/anthrojournal.urbanities"><strong><strong><strong>
		</strong></strong></strong></a></div></div></div><a href="https://www.facebook.com/anthrojournal.urbanities"><strong><strong><strong>
        </strong></strong></strong></a></div><!-- end row --><a href="https://www.facebook.com/anthrojournal.urbanities"><strong><strong><strong>
    </strong></strong></strong></a></div><!-- end container --><a href="https://www.facebook.com/anthrojournal.urbanities"><strong><strong><strong>
</strong></strong></strong></a></section><a href="https://www.facebook.com/anthrojournal.urbanities"><strong><strong><strong>
<!-- End Section -->

    <!-- Start sub footer -->
    </strong></strong></strong></a><strong><strong><strong><div id="sub_footer" class="sub_footer light"><a href="https://www.facebook.com/anthrojournal.urbanities">
        </a><div class="container"><a href="https://www.facebook.com/anthrojournal.urbanities">
            </a><div class="row"><a href="https://www.facebook.com/anthrojournal.urbanities">
                </a><div class="col-xs-12 col-md-12 col-lg-6 col-sm-6"><a href="https://www.facebook.com/anthrojournal.urbanities">
                    </a><p><a href="https://www.facebook.com/anthrojournal.urbanities">Copyright © 2011  </a><a href="&lt;/div">
                </a></p><div class="col-xs-12 col-md-12 col-lg-6 col-sm-6 align_right"><a href="&lt;/div">
                    <span style="&lt;/div">
            </span></a></div><!-- End row --><a href="&lt;/div">
        </a></div><!-- End container --><a href="&lt;/div">
    </a></div><a href="&lt;/div">
    <!-- End sub footer -->
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-includes/js/comment-reply.min.js?ver=4.5.32"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/contact-form-7/includes/js/jquery.form.min.js?ver=3.51.0-2014.06.20"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _wpcf7 = {"loaderUrl":"https:\/\/www.anthrojournal-urbanities.com\/wp-content\/plugins\/contact-form-7\/images\/ajax-loader.gif","sending":"Invio..."};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/plugins/contact-form-7/includes/js/scripts.js?ver=4.3"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/framework/Pagebuilder/js/?ver=4.5.32"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-content/themes/mana/assets/js/?ver=4.5.32"></script>
<script type="text/javascript" src="https://www.anthrojournal-urbanities.com/wp-includes/js/wp-embed.min.js?ver=4.5.32"></script>

    </a></div><!-- end .wrapper --><a href="&lt;/div">

    <span class="gototop_footer gototop">
        <i class="icon-angle-up"></i>
    </span>


<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-56210201-1', 'auto');
  ga('send', 'pageview');

</script>

</a></div></strong></strong></strong></div></body></html>

""",
    "page_size": "A4",
    "title": "Title",
    "dir": "ltr",
    "hostname": "www.printfriendly.com",
    "platform": "Win32",
    "css_url": ""
}


url='https://api.printfriendly.com/v2/pdf/create?api_key=chrome-extension-4caede54-370b-4018-a8b7-86b825930d91'

soup = get_soup(url)

print(soup)





