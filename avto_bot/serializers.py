from rest_framework.serializers import ModelSerializer
from .models import BotUser, Feedback

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name', 'username', 'user_id', 'phone_number', 'created_dt')
        
class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('name', 'user_id', 'created_dt', 'body')