from rest_framework import serializers
import numpy as np
from inference.models import Message


class MessageStatsSerializer(serializers.Serializer):
    class_0_percentiles = serializers.ListField(child=serializers.FloatField(), read_only=True)
    class_1_percentiles = serializers.ListField(child=serializers.FloatField(), read_only=True)
    class_2_percentiles = serializers.ListField(child=serializers.FloatField(), read_only=True)

    def get_percentiles(self, values):
        percentiles = [1, 25, 50, 75, 99]
        return np.percentile(values, percentiles).tolist()

    def to_representation(self, instance):
        chat_id = instance
        messages = Message.objects.filter(chat_id=chat_id)

        class_0 = list(messages.values_list('class_0_probability', flat=True))
        class_1 = list(messages.values_list('class_1_probability', flat=True))
        class_2 = list(messages.values_list('class_2_probability', flat=True))

        # Filter out None values
        class_0 = [x for x in class_0 if x is not None]
        class_1 = [x for x in class_1 if x is not None]
        class_2 = [x for x in class_2 if x is not None]

        return {
            'class_0_percentiles': self.get_percentiles(class_0),
            'class_1_percentiles': self.get_percentiles(class_1),
            'class_2_percentiles': self.get_percentiles(class_2),
        }


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
