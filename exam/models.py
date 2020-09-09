from django.db import models
from django_mysql.models import ListCharField
import uuid
from django.utils import timezone

from json import JSONEncoder
from uuid import UUID

JSONEncoder_olddefault = JSONEncoder.default

def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return o.toString
    return JSONEncoder_olddefault(self, o)

JSONEncoder.default = JSONEncoder_newdefault

# Create your models here.
class QuestionTr(models.Model):

    class Meta:
        app_label = 'exam'

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text            = models.TextField(null=False)
    exam_class      = models.CharField(max_length=128, null=False)
    year            = models.DateField(null=False)
    select1         = models.CharField(max_length=128, null=False)
    select2         = models.CharField(max_length=128, null=False)
    select3         = models.CharField(max_length=128, null=False)
    select4         = models.CharField(max_length=128, null=False)
    select5         = models.CharField(max_length=128, null=True)
    select6         = models.CharField(max_length=128, null=True)
    select7         = models.CharField(max_length=128, null=True)
    select8         = models.CharField(max_length=128, null=True)
    select9         = models.CharField(max_length=128, null=True)
    select10        = models.CharField(max_length=128, null=True)
    explanation     = models.TextField(null=False)
    created_at      = models.DateTimeField(default=timezone.now, null=False)
    last_update     = models.DateTimeField(default=timezone.now, null=False)


class ExamTr(models.Model):

    class Meta:
        app_label = 'exam'

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    volume          = models.IntegerField(null=False)
    scope           = models.CharField(max_length=128, null=False)
    year            = models.DateField(null=False)
    questions       = ListCharField(
        base_field=models.CharField(max_length=32, null=True),
        max_length=5120,
    )
    answers         = ListCharField(
        base_field=models.CharField(max_length=4, null=True),
        max_length=512,
    )

