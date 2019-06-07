from django.shortcuts import render
from rest_framework import filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import UserSerializers
from .models import Users
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class usersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('first_name', 'age')

    def create(self,rquest,*args,**kwargs):
        data=rquest.data.get("items") if 'items' in rquest.data else rquest.data
        many=isinstance(data,list)
        serializer=self.get_serializer(data=data,many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)