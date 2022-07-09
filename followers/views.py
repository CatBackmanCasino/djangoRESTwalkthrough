from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowersSerializer


class FollowersView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowersSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowersDetail(generics.RetrieveDestroyAPIView):
    permission_class = [IsOwnerOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()
