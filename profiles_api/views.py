from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API view"""

    def get(self,request,format=None):
        """Return a list of APIview features"""
        an_apiView=[
            'using Http method as function(get,post,patch,put,delete)',
            'is similar to tradinitial Django view',
            'Give you the most control over the appliction logic',
            'is mapped manually to urls',
        ]

        return Response({'message':'Hello!','an_apiView':an_apiView})