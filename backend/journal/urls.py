from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, MyTokenObtainPairView, MyTokenRefreshView

router = DefaultRouter()
router.register(r'entries', JournalEntryViewSet)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
