from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UploadedSongs, Audio
from auth_app.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.



class UploadSongs(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    def post(self, request):

        if not request.info["valid"]:
            messages.error(request, 'Invalid token. for uploading images please loging')
            return redirect('/auth/login')
        
    
       
        
        # file = request.FILES['audio']
        uploaded_files = request.FILES.getlist('files')
        for audio_file in uploaded_files:
            user = request.info["user"]
            audio = Audio(user=user, audio_file=audio_file)
            audio.save()

        data = {'message': 'success full'}
        response = JsonResponse(data)
        response.status_code = 200
        return response
        

    def get(self, request):
        response = render(request, template_name="upload_song.html")
        return response 
    

class Songs(APIView):

    # permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    # parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def get(self, request):
        
        if not request.info["valid"]:
            messages.error(request, 'Invalid token. for viewing images please loging')
            return redirect('/auth/login')
        user_email = request.info["user"].email
        user = User.objects.get(email=user_email)
        audio_files = Audio.objects.filter(user=user)
        context = {"audio_files": audio_files}
        return render(request, template_name="song_list.html", context=context)
    


def home(request):

    return render(request, template_name="home.html")
    

def profile(request):
    return render(request, template_name="profile.html")