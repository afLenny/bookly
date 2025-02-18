from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookView(ViewSet):
    

    def list(self, request):
        try:
            result = Book.objects.all()
            serializer = BookSerializer(result, many=True)
            return Response({
                "status": "success",
                "books": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as exc:
            raise APIException(str(exc))
    
    def retrieve(self, request, pk=None):

        try:
            result = Book.objects.get(id=pk)
            serializer = BookSerializer(result)

            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as exc:
            raise NotFound(str(exc))
    
    def create(self, request):

        try:
            book_data = request.data.copy()

            #ISBN Validation
            if 'isbn' in book_data and Book.objects.filter(isbn=book_data['isbn']).exists():
                return Response({
                    "status": "error",
                    "message": "ISBN already registered."
                }, status=status.HTTP_400_BAD_REQUEST)
                
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            raise APIException(str(exc))

        

    
    def update(self, request, pk=None):
        pass