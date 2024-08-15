from django.shortcuts import render
from .serializer import UserSerializer, UserScoreSerializer, UserWordsSerializar
from .models import UserScore, UserProfile
from word.models import Word
from word.serializer import WordSerializer
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


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def UserScoreAPI(request, score_id=None):
    user = request.user
    profile_user = UserProfile.objects.get(user=user)

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


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def UserWordsAPI(request):
    user = request.user
    profile_user = UserProfile.objects.get(user=user)
    if request.method == "GET":
        score = UserScore.objects.filter(profile=profile_user)
        words_list = []
        for le_score in score:
            element = Word.objects.get(id = le_score.word_id)
            words_list.append(element)

        serializer = WordSerializer(words_list, many=True)
        return Response(serializer.data)
    else:
        response_data = {
            "details": "Metodo no Autorizado",
            "ok": True,
            "status": status.HTTP_405_METHOD_NOT_ALLOWED,
        }
        return Response(response_data)