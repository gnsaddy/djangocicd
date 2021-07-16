from django.http.response import JsonResponse
from django.shortcuts import render


def Home(request):
    data = {
        "user_url": "http://localhost:8000/api/user/",
        "status": "success "+"API route"
    }
    return JsonResponse(data)
