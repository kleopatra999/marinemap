from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from lingcod.common import mimetypes
from lingcod.common.utils import KmlWrap, LargestPolyFromMulti

from lingcod.manipulators.manipulators import * 
from manipulators import *
from django.contrib.gis.geos import *

from django.conf import settings
#from cjson import encode as json_encode
from django.utils import simplejson

import models

def mlpaManipulators(request, template_name='common/mlpa-manipulators.html'):
    return render_to_response(template_name, RequestContext(request,{'api_key':settings.GOOGLE_API_KEY}))
 

