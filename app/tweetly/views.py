import logging
from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from nbio.django.shortcuts import render_response


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
