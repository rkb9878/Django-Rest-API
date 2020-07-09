from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.models import snippet
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """ Test API view"""

    serializer_class = serializers.helloSerializer
    """serializer_class this word is a keyword so write it same """

    def get(self, request, format=None):
        """Return a list of APIview features"""
        an_apiView = [
            'using Http method as function(get,post,patch,put,delete)',
            'is similar to tradinitial Django view',
            'Give you the most control over the appliction logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiView': an_apiView})

    def post(self, request,format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mobile=serializer.validated_data.get('mobile')

            message = f"Hello {name} and mobile no is {mobile}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handel updating an object"""
        return Response({'Method':'PUT'})
    def patch(self,request,pk=None):
        """Handling partial update of an object"""
        return Response({'Method':'patch'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api viewSet"""

    serializer_class = serializers.helloSerializer

    def list(self,request):
        """Return hello message"""
        a_viewSet=[
            'using Action (list, create, retrive, update, partial_update, destroy',
            'Automatically maps to urls using routing',
            'Providing more Functionality with less code',
        ]

        return Response({'message':"Hello !!!!",'a_viewset':a_viewSet})

    def create(self,request):
        """Create a new Hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            mobile=serializer.validated_data.get('mobile')

            message=f"hello {name} and mobile number is {mobile}"

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handling getting an object by its ID"""
        return Response({'Http_method':'GET'})

    def update(self,request,pk=None):
        """Handling update and object by its ID"""
        return Response({"Http_methot": 'PUT'})

    def partial_update(self,request,pk=None):
        """Handling partial update of an object"""
        return Response({'Http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handling remove an object"""
        return Response({'Http_method':'Delete'})


class snippetView(APIView):
    serializer_class=serializers.SnippetSerializer
    """serializer_class this word is a keyword so write it same """
    def get(self,request,format=None):
        snippets = snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)