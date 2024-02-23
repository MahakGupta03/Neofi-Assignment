from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes.views import SignUpView, CustomLoginView,NoteCreateView, NoteDetailView, NoteShareView, NoteUpdateView, NoteVersionHistoryView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# router.register(r'notes/create', NoteCreateView, basename='Note')
# router.register(r'notes/version-history', NoteVersionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomLoginView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('notes/create/', NoteCreateView.as_view()),
    path('notes/<int:pk>/', NoteDetailView.as_view()),
    path('notes/share/', NoteShareView.as_view()),
    path('notes/update/<int:pk>/', NoteUpdateView.as_view()),
    path('notes/version-history/<int:pk>/', NoteVersionHistoryView.as_view()),
]
