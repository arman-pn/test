import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from.models import User,Project,TimeEntry
from Time.Serializers import UserSerializer, ProjectSerializer, TimeEntrySerializer, DeviceAuthSerializer

from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.views import APIView # type:ignore



class DeviceAuthView(APIView):
    def post(self, request):
        serializer = DeviceAuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        id_device = serializer.validated_data['id_device']

        # Try to find existing user with this device ID
        try:
            user = User.objects.get(id_device=id_device)
        except User.DoesNotExist:
            # Create new user if not exists
            username = f'user_{uuid.uuid4().hex[:8]}'
            user = User.objects.create(
                username=username,
                id_device=id_device
            )

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user.username,
            'id_device' : id_device,
        })
class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        # projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TimeEntiryView(APIView)    :
    def get(self, request):
        time = TimeEntry.objects.all()
        serializer = TimeEntrySerializer(time, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView) :
    def get (self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            Post=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Post.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)

class ProjectsDetail(APIView) :
    def get (self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projects,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        projects.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)


class TimeEntiryDetail(APIView) :
    def get (self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(times)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(times,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        times.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)