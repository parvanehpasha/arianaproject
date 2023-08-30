from rest_framework import serializers

from ariana.twitt.models import Post, ReplyPost


class SubReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyPost
        fields = ('reply', 'user')


class ReplyPostSerializer(serializers.ModelSerializer):
    parent_reply = serializers.PrimaryKeyRelatedField()
    subreply = serializers.SubReplySerializer()

    class Meta:
        model = ReplyPost
        fields = ('parent_reply', 'post', 'user', 'reply', 'subreply')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']

