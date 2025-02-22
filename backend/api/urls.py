from django.urls import path
from .views import CreateUserView,NoteCreateView,NoteDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/', NoteCreateView.as_view(), name='note-list-create'),
    path('notes/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]
