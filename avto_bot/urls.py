from django.urls import path
from .views import BotUsersApiView, FeedbackApiView

urlpatterns = [
    path('bot-users',BotUsersApiView.as_view(),name='bot-users'),
    path('feedbacks',FeedbackApiView.as_view(),name='feedbacks'),
]
