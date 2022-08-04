from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.db import models
from django.shortcuts import get_object_or_404
from app.models import Contributor

class IsContrubutorOrIsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'POST']:
            return True
        return request.user.id == obj.author.id

