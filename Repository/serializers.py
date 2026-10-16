from rest_framework import serializers
from Repository.models import QuestionDb

class QuestionSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    language=serializers.ChoiceField(choices=QuestionDb.LANGUAGE_CHOICES,default="python")
    difficulty_level=serializers.ChoiceField(choices=QuestionDb.DIFFICULTY_LEVEL,default="easy")
    note=serializers.CharField(max_length=2000)
    publish_date=serializers.DateTimeField(read_only=True)
    topic=serializers.CharField(max_length=200)
    sample_input=serializers.CharField(max_length=2000)
    sample_output=serializers.CharField(max_length=2000)
    is_active=serializers.BooleanField(default=True)