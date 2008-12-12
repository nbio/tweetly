from django.conf.urls.defaults import *
from django.conf import settings
from nbio.django.views import auto
import tweetly.views as views

HOST = 'host'
PATH = 'path'
LOCATION = 'location'
TEMPLATE = 'template'
APP_HOST = settings.HOSTS['app']
STATIC_HOST = settings.HOSTS['static']
DOMAIN_NAME = settings.DOMAIN_NAME


handler404 = "nbio.django.views.page_not_found"
handler500 = "nbio.django.views.server_error"


urlpatterns = patterns('',
    (r'^$', views.home, {HOST: APP_HOST}, 'home'),
    
    # (r'^sitemap.xml$', views.sitemap_xml, {HOST: APP_HOST}, 'sitemap_xml'),
    (r'^(noexist_|google)[a-z0-9]+.html$', handler404),
    
    # (r'^api/site/search/?$', api.site_search, {HOST: APP_HOST}),
    # (r'^api/site/info/?$', api.site_info, {HOST: APP_HOST}),
    
    # (r'^api/opensearch/suggest/?$', api.opensearch_suggest, {HOST: APP_HOST}),
    # (r'^api/opensearch.osd$', api.opensearch_osd, {HOST: APP_HOST}),
    
    (r'^home/?$', auto, {HOST: APP_HOST, PATH: '/'}, 'about'),
    (r'^about/blog/?$', auto, {LOCATION: 'http://blog.' + DOMAIN_NAME + '/'}, 'blog'),
    # (r'^about/twitter/?$', auto, {LOCATION: 'http://twitter.com/tweetly'}, 'twitter'),
    # (r'^about/help/?$', auto, {LOCATION: 'http://getsatisfaction.com/domainr'}, 'help'),
    # (r'^about/feedback/?$', auto, {LOCATION: 'http://getsatisfaction.com/domainr'}, 'feedback'),
    
    # (r'^([^/]+)/?$', views.search, {HOST: APP_HOST}, 'search'),
    # (r'^([^/]+)/www/?$', views.domain_www, {HOST: APP_HOST}, 'domain_www'),
    # (r'^([^/]+)/whois/?$', views.domain_whois, {HOST: APP_HOST}, 'domain_whois'),
    # (r'^([^/]+)/register/?$', views.domain_register, {HOST: APP_HOST}, 'domain_register'),
    # (r'^([^/]+)/register/([^/]+)/?$', views.domain_register, {HOST: APP_HOST}, 'domain_register_specific'),
    
    # (r'^([^/]+)/(atom|rss)/?$', feeds.search, {HOST: APP_HOST}, 'feeds_search'),
    
    # (r'^_admin/status/?$', admin.status, {HOST: APP_HOST}, 'admin_status'),
    
    (r'.*', auto, {HOST: APP_HOST}),
)
