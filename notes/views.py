from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Note, NoteVersion
from .serializers import NoteSerializer, NoteVersionSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

class SignUpView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        user = User.objects.create(username=username, password=make_password(password))
        user.save()
        return Response({'message': 'User created successfully'})



class CustomLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    

class NoteCreateView(APIView):

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        # user = request.data.get('user')
        if serializer.is_valid():
            # serializer.save(user=user)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class NoteDetailView(APIView):

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

class NoteShareView(APIView):

    def post(self, request):
        note_id = request.data.get('note_id')
        user_names = request.data.get('user_names')
        note = get_object_or_404(Note, pk=note_id)
        for user_name in user_names:
            user = get_object_or_404(User, username=user_name)
            note.shared_with.add(user)
        return Response({'message': 'Note shared successfully'})

class NoteUpdateView(APIView):

    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class NoteVersionHistoryView(APIView):

    def get(self, request, pk):
        versions = NoteVersion.objects.filter(note_id=pk)
        serializer = NoteVersionSerializer(versions, many=True)
        return Response(serializer.data)
