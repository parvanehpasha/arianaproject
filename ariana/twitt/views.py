from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ariana.twitt.exception import FollowException, TimeLineException
from ariana.twitt.models import FollowUser, Post, ReplyPost
from ariana.twitt.serializer import PostSerializer, ReplyPostSerializer


class FollowUserGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = FollowUser.objects.filter(follower=request.user.id, following=pk).first()
            if user and user.follow == True:
                raise FollowException('this user follow with you')
            elif user and user.follow == False:
                user.follow = True
                user.save()
                raise FollowException('this user is followed by you')
            else:
                follow_user = FollowUser(following=pk, follower=request.user.id, follow=True)
                follow_user.save()
                raise FollowException('following this user')
        except FollowException as exc:
            return Response({'message': str(exc)})


class TimeLineGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            all_follower = FollowUser.objects.filter(follower=request.user.id).values('follower')
            if all_follower:
                posts = Post.objects.filter(user__in=all_follower).all()
                all_post = PostSerializer(posts, many=True)
                return Response(data=all_post.data, status=status.HTTP_200_OK)
            else:
                raise TimeLineException('you are not any follower')

        except TimeLineException as exc:
            return Response({'message': str(exc)})


class ReplyPostGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            all_reply = ReplyPost.objects.get(post=pk).all()
            replys = ReplyPostSerializer(all_reply, many=True)
            return Response(data=replys.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
