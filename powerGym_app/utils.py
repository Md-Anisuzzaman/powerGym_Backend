from django.http import JsonResponse
from django.conf import settings
from functools import wraps
from rest_framework.response import Response

def global_response(data=None, msg=None, status=None, errors=None):
    response_data = {}
    if msg:
        response_data["msg"] = msg
    if data:
        response_data["data"] = data
    if errors:
        response_data["errors"] = errors

    return Response(response_data, status=status)



