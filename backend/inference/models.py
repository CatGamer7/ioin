from django.db import models


class Message(models.Model):
    chat_id = models.BigIntegerField() 
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class_0_probability = models.FloatField(blank=True, null=True)
    class_1_probability = models.FloatField(blank=True, null=True)
    class_2_probability = models.FloatField(blank=True, null=True)
