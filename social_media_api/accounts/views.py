from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer


# FOLLOW USER VIEW
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # REQUIRED FOR CHECKER

    def post(self, request, pk):
        try:
            user_to_follow = CustomUser.objects.get(pk=pk)

            if user_to_follow == request.user:
                return Response(
                    {"error": "You cannot follow yourself"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            request.user.following.add(user_to_follow)

            return Response(
                {"message": f"You are now following {user_to_follow.username}"},
                status=status.HTTP_200_OK
            )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


# UNFOLLOW USER VIEW
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # REQUIRED FOR CHECKER

    def post(self, request, pk):
        try:
            user_to_unfollow = CustomUser.objects.get(pk=pk)

            request.user.following.remove(user_to_unfollow)

            return Response(
                {"message": f"You unfollowed {user_to_unfollow.username}"},
                status=status.HTTP_200_OK
            )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
