from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile,User



# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    def post(self,request):
        renderer_classes = [UserRenderer]
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"token":token,'msg':"registation success"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request):
        renderer_classes= [UserRenderer]
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None :
                token = get_tokens_for_user(user)
                return Response({"token":token,"msg":"login success"},status=status.HTTP_200_OK)
            return Response({"errors":{"non_field_erros":['password and email is not valid']}},status=status.HTTP_404_NOT_FOUND)
        
class UserProfileView(APIView):
    renderer_classes= [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = request.user
        serializer = UserProfileSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserChangePassword(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = UserChangePasswordSerializer(data = request.data,context = {"user":request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password changed'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class SendPasswordResetView(APIView) :
    renderer_classes = [UserRenderer]
    def post(self, request, format = None) :
        serializer = SendPasswordResetEmailSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True) :
            return Response({"Message" : "Password reset link send to your email. Please check your email"}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView) :
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format = None) :
        serializer = UserPasswordResetSerializer(data = request.data, context = {"uid" : uid, "token" : token})
        if serializer.is_valid() :
            return Response({"Message" : "Password Reset Successfully"}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UserProfileUpdate(APIView):
    renderer_classes = [UserRenderer]
    def put(self,request,pk):
        data = request.FILES['image']
        if update := UserProfile.objects.filter(user_id=pk).first():
            update.image = data
            update.save()
            return Response({'msg':'updated'})
        return Response({'msg':'error'})   
    
# class UserskillView(APIView):
#     def put(self,request,pk):
        





    