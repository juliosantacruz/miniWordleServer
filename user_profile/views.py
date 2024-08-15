from django.shortcuts import render
from .serializer import UserSerializer, UserScoreSerializer
from .models import UserScore, UserProfile

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuario registrado exitosamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["name"] = user.first_name
        token["username"] = user.username
        token["email"] = user.email
        user_profile = user.user_profile if hasattr(user, "user_profile") else None
        # Add custom claims from UserProfile model
        if user_profile:
            token["company"] = user_profile.company
            token["phone"] = user_profile.phone
            token["isAdmin"] = user_profile.isAdmin
        return token


class MyTokenObteainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @permission_classes([IsAuthenticated])
# class UserScoreAPI(APIView):
#     authentication_classes=[]
#     permission_classes=[]

#     def get(self, request):
#         # user_profile = UserProfile.objects.get(request.user)
#         print('user ',request._user )
#         score = UserScore.objects.all()
#         serializer= UserScoreSerializer(score, many=True)

#         return Response(serializer.data)


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def UserScoreAPI(request, score_id=None):
    user = request.user
    profile_user = UserProfile.objects.get(user=user)
    # print(dir(request ))
    # print(score_id)
    if request.method == "GET":
        score = UserScore.objects.filter(profile=profile_user)
        serializer = UserScoreSerializer(score, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        score_id = request.data['score_id']
        try:
            score = UserScore.objects.get(id=score_id, profile=profile_user)
        except UserScore.DoesNotExist:
            return Response(
                {"error": "Score no encontrada"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        score_id = request.data['score_id']
        try:
            score = UserScore.objects.get(id=score_id)
        except UserScore.DoesNotExist:
            return Response(
                {"error": "Score no encontrada"}, status=status.HTTP_404_NOT_FOUND
            )
        score.delete()
        response_data = {
            "details": "Score Eliminada",
            "ok": True,
            "status": status.HTTP_200_OK,
        }
        return Response(response_data)
    return Response(status=status.HTTP_204_NO_CONTENT)
