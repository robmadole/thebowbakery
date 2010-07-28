from django.template import RequestContext
from django.shortcuts import render_to_response


def list(request):
    return render_to_response('inventory/list.html',
        {},
        RequestContext(request))


def components(request):
    return render_to_response('inventory/components.html',
        {},
        RequestContext(request))
