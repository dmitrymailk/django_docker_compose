from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Counter
from .serializers import CounterSerializer
from rest_framework import status


class CounterView(APIView):
    def get(self, request, format=None):
        amount = Counter.objects.count()
        if amount == 0:
            data = {"my_counter": 0}
            serializer = CounterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            counter = Counter.objects.get(pk=1)
            counter.my_count += 1
            counter.save()
            serializer = CounterSerializer(counter)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print(request)
        return Response(status=status.HTTP_200_OK)
