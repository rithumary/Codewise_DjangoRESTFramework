from django.db import models

# Create your models here.

class QuestionDb(models.Model):
    title=models.CharField(max_length=200)

    LANGUAGE_CHOICES=(
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript")
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)

    DIFFICULTY_LEVEL=(
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )

    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_LEVEL)
    note=models.TextField()
    publish_date=models.DateTimeField(auto_now_add=True)
    topic=models.CharField(max_length=200)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)