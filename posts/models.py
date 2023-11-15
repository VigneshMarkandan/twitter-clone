from django.db import models
from django.forms import DateTimeField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank = False, null=False, max_length = 15, default='Anonymous', db_index = True
    )

    body = models.CharField(
        'Body', blank = True, null=True, max_length = 100, db_index = True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank = True, auto_now_add = True
    )
