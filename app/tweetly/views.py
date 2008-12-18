import logging
from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from nbio.django.utils import reverse_slash
from nbio.django.shortcuts import render_response
from nbio.django.http import JSONHttpResponse
from google.appengine.ext import db
from models import Dogear, Delegate, Client


def request_title(request, query=None, info_result=None):
    title = [settings.DEFAULT_TITLE]
    if info_result:
        if info_result.is_tld:
            title.insert(0, u'.%s (TLD)' % info_result.domain )
        else:
            title.insert(0, info_result.domain)
    elif query:
        title.insert(0, query)
    return u' - '.join(title)

def home(request, **kwargs):
    title = request_title(request)
    return render_response(request, 'home.html', locals())

def dogears(request, **kwargs):
    """This is a debug method for listing all the dogears"""
    if not settings.DEBUG:
        return HttpResponseRedirect(reverse_slash('home'))
    title = request_title(request)
    dogears = Dogear.all().order('item_time').fetch(10)
    return render_response(request, 'dogears.html', locals())

def dogears_set(request, **kwargs):
    delegate_key = request.REQUEST.get('delegate_key', None)
    item_id = request.REQUEST.get('item_id', None)
    item_time = request.REQUEST.get('item_time', None)
    client = Client.all().fetch(1)[0]
    
    response_data = {
        'status': 200,
        'status_msg': '',
    }
    return JSONHttpResponse(response_data)

def dogears_get(request, **kwargs):
    delegate_key = request.REQUEST.get('delegate_key', None)
    # client = Client.all().fetch(1)[0]
    if delegate_key:
        query = Dogear.all().filter('delegate =', db.Key(delegate_key)).order('-item_time')
        last_dogear = query.fetch(1)[0]
        # dogear = query.filter('client =', client).fetch(1)[0]
    
    response_data = {
        'status': 200,
        'status_msg': '',
        # 'item_id': dogear.item_id,
        # 'item_time': dogear.item_time,
        'last_item_id': last_dogear.item_id,
        'last_item_time': str(last_dogear.item_time),
    }
    return JSONHttpResponse(response_data)
