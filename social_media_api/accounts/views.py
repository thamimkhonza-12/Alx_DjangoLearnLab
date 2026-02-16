from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import CustomUser


class FollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = CustomUser.objects.all()

    def post(self, request, user_id):

        user_to_follow = get_object_or_404(
            CustomUser.objects.all(),
            id=user_id
        )

        if user_to_follow == request.user:
            return Response(
                {"error": "You cannot follow yourself"},
                status=400
            )

        request.user.following.add(user_to_follow)

        return Response({
            "message": f"You are now following {user_to_follow.username}"
        })


class UnfollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = CustomUser.objects.all()

    def post(self, request, user_id):

        user_to_unfollow = get_object_or_404(
            CustomUser.objects.all(),
            id=user_id
        )

        request.user.following.remove(user_to_unfollow)

        return Response({
            "message": f"You unfollowed {user_to_unfollow.username}"
        })
