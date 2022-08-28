from dataclasses import fields
from rest_framework import serializers
from .models import Counter


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        # fields = ("id", "my_counter")
        fields = "__all__"
