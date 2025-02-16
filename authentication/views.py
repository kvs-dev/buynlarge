from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import login as django_login
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    
    if request.method == 'POST':
        password = request.data.get('password')
        email = request.data.get('email')
        username = request.data.get('username')
        if not User.objects.filter(email=email).exists():
            return JsonResponse({"message": "User does not exist"}, status=401)
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request._request, user)
            return JsonResponse({"message": "Login successful", "user": user.id})
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    print(request.data, "soy request")
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "User already exists"}, status=400)
        user = User.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.save()
        return JsonResponse({"message": "User created successfully", "user": user.id})
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)
