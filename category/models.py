from django.db import models
import uuid

 # Create News Model
class category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    status = models.BooleanField()
    parentId = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    creator = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)





