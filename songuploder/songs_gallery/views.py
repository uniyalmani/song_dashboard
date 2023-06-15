from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UploadedSongs, Audio, ProtectedFileAccess
from auth_app.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
import random
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
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
        audio_access = request.data.get('audioAccess')
        emails = request.data.getlist('emails')

        
        print(emails, "these are emails ", audio_access)
        print("//////////////////////////")
        for audio_file in uploaded_files:
            user = request.info["user"]
            audio = Audio(user=user, audio_file=audio_file, access_type=audio_access)
            audio.save()
            
            if audio_access == "Protected":
                for email in emails:
                    other_user = get_object_or_404(User, email=email)
                    protected_access = ProtectedFileAccess(audio = audio, user = other_user)
                    protected_access.save()
                    
            

        

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
        # Filter Audio objects
        public_audios = Audio.objects.filter(access_type='Public')
        private_audios = Audio.objects.filter(access_type='Private', user=user)
        protected_upload_audios = Audio.objects.filter(access_type='Protected', user=user)
        protected_audios  = Audio.objects.filter(access_type='Protected',protectedfileaccess__user=user)
        print("//////////////////////")
        print("protected_audios", protected_audios, "////////////////////")
        print("//////////////////////")
        audio_files = public_audios | private_audios | protected_audios | protected_upload_audios
        print(audio_files)
        context = {"audio_files": audio_files}
        return render(request, template_name="song_list.html", context=context)
    




def home(request):

    return render(request, template_name="home.html")
    

def profile(request):
    return render(request, template_name="profile.html")


def check_email(request):
    email = request.GET["email"]

    # Check if the email address already exists in the database
    
    
    try:

        User.objects.get(email=email)
        res = JsonResponse({"exists": True}, status = 200)

        return res
    except User.DoesNotExist:
        res = JsonResponse({"exists": False}, status = 400)
        return res

        

  