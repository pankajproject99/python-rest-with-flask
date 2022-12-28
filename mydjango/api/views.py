from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name': 'Pankaj', 'age': 28}
    # return Response(person)
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)