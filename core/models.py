# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers


class Dish(models.Model):
    id = serializers.IntegerField(read_only=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        """
        Create and return a new `Dish` instance, given the validated data.
        """
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Dish` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

