from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from v1_backend.models import Rental
from v1_backend.serializers import RentalSerializer

def index(request):
    return HttpResponse("Hello, world. This is api/v1")

@csrf_exempt
def rental_list(request):
    """
    List all rentals, or create a new rental
    """
    if request.method == 'GET':
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return JsonResponse({'rentals': serializer.data}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RentalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def rental_detail(request, pk):
    """
    Retrieve, update, or delete a rental
    """
    try:
        rental = Rental.objects.get(pk=pk)
    except Rental.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RentalSerializer(rental)
        return JsonResponse({'rental': serializer.data})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RentalSerializer(rental, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rental.delete()
        return HttpResponse(status=204)
