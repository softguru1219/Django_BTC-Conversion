
from django.shortcuts import ( render_to_response )
from django.template import RequestContext




# HTTP Error 500
def bad_request(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response


# HTTP Error 500
def page_not_found(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

    