from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Post
from .serializers import PostSerializer,CommentSerializer

class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self,request):
        print(request.auth)
        print(request.user)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    def get_post(self,repust, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False
        
    def get(self,requset,post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    def get_post(self,repust, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False
        
    def get(self,requset,post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        likes = Post.likes.filter(is_liked=True).count()
        return Response({'likes': likes})
    
    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

































class PostDetailView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # در ویس بهتون توضیح میدم
    permission_classes = [IsAuthenticated,IsAdminUser] # این مورد بخاطر اینه که یوزر که داره درخواست میده احراز هویت نشده
   