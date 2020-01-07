from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import News
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import NewsSerializer
from .pagination import CustomPagination

class get_delete_update_news(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return news

    # Get a news
    def get(self, request, pk):
        news = self.get_queryset(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a news
    def put(self, request, pk):
        news = self.get_queryset(pk)

        if(request.user == news.creator): # If creator is who makes request
            serializer = NewsSerializer(news, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a news
    def delete(self, request, pk):
        news = self.get_queryset(pk)

        if(request.user == news.creator): # If creator is who makes request
            news.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_news(ListCreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       news = News.objects.all()
       return news

    # Get all news
    def get(self, request):
        news = self.get_queryset()
        paginate_queryset = self.paginate_queryset(news)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new news
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

