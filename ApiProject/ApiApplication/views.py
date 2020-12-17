from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

#views here for APIView.
class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )

        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})
    
   
#views here for ModelViewSet.    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer   