from django.shortcuts import render
from rest_framework import viewsets
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Create your views here.


class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)


class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass
