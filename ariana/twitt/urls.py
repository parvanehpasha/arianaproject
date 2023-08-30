from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = 'twitt'
router = routers.DefaultRouter()

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('follow/<int:pk>', views.FollowUser),
    path('timeline/', views.TimeLineGetView),
    path('reply/post/<int:pk>', views.ReplyPostGetView)

]
