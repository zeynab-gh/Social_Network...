from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializer import UserListSerializer
from .models import Friendship

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        Friendship.objects.get_or_create(request_from=request.user, request_to=user)
        return Response({'detial':'Request sent'}, status=status.HTTP_201_CREATED)


class RequestListView(APIView):

    permission_classes = [IsAuthenticated]

    def get (self,request):
        friendship = Friendship.objects.filter(request_to=request.user, is_accepted=False)
        users=[fr.request_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
    

class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
            friendship = Friendship.objects.get(request_from=user, request_to=request.user, is_accepted=False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

        friendship.is_accepted=True
        friendship.save()
        return Response({'detial':'Conected'})



class FrindListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship = Friendship.objects.filter(
            Q(friendship_from=request.user) | Q(friendship_to=request.user),
            is_accepted=True
        )
        users = [fr.request_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)