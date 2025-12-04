from rest_framework import serializers
from inference.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'chat_id',
            'text',
            'created_at',
            'class_0_probability',
            'class_1_probability',
            'class_2_probability'
        ]
