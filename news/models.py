from django.db import models
import uuid

 # Create News Model
class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    status = models.BooleanField()
    tracking_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)





