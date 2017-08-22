from rest_framework.response import Response
from rest_framework.views import APIView

from companies.models import Stock
from companies.serializers import StockSerializer


class StockList(APIView):
    @staticmethod
    def get(request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# TODO: Delete REST API StockList and create REST API for Music Website
