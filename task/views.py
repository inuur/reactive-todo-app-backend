from rest_framework.response import Response
from rest_framework.views import APIView

from .models import List
from .serializers import ListSerializer


class ListView(APIView):
    @staticmethod
    def get(request):
        lists = List.objects.filter(user=request.user)
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
