from django.contrib import admin

from .models import Post, ReplyPost, LikePost, FollowUser


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'body']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'reply', 'parent_reply']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'like']
    list_filter = ['like']


class FollowAdmin(admin.ModelAdmin):
    list_display = ['following', 'follower', 'follow']


admin.site.register(Post, PostAdmin)
admin.site.register(ReplyPost, ReplyAdmin)
admin.site.register(LikePost, LikeAdmin)
admin.site.register(FollowUser, FollowAdmin)
