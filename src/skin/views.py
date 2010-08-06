from django.template import RequestContext
from django.shortcuts import render_to_response


def list(request):
    return render_to_response('skin/components.html',
        {},
        RequestContext(request))
