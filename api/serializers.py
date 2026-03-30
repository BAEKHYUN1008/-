from rest_framework import serializers
from core.models import Law, Subscription

class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = '__all__'   # 返回所有字段，你也可以指定需要的字段列表

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'scene', 'created_at']