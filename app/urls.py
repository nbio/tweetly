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
    (r'api/dogears/?$', views.dogears, {HOST: APP_HOST}, 'dogears'),
    (r'api/dogears/set?$', views.dogears_set, {HOST: APP_HOST}, 'dogears_set'),
    (r'api/dogears/get?$', views.dogears_get, {HOST: APP_HOST}, 'dogears_get'),
    
    # (r'^sitemap.xml$', views.sitemap_xml, {HOST: APP_HOST}, 'sitemap_xml'),
    (r'^(noexist_|google)[a-z0-9]+.html$', handler404),
    
    (r'^home/?$', auto, {HOST: APP_HOST, PATH: '/'}, 'about'),
    (r'^about/blog/?$', auto, {LOCATION: 'http://blog.' + DOMAIN_NAME + '/'}, 'blog'),
    # (r'^about/twitter/?$', auto, {LOCATION: 'http://twitter.com/tweetly'}, 'twitter'),
    # (r'^about/help/?$', auto, {LOCATION: 'http://getsatisfaction.com/domainr'}, 'help'),
    # (r'^about/feedback/?$', auto, {LOCATION: 'http://getsatisfaction.com/domainr'}, 'feedback'),
    
    (r'.*', auto, {HOST: APP_HOST}),
)
