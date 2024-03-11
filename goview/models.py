import datetime
import uuid

from django.db import models


# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    state = models.IntegerField(blank=False, default=-1, db_index=True)
    createTime = models.DateTimeField(auto_now_add=True, db_index=True)
    updateTime = models.DateTimeField(auto_now=True, db_index=True)
    createUserId = models.CharField(max_length=255, null=True, blank=False)
    deletedTime = models.DateTimeField(null=True, blank=True, db_index=True)
    cover = models.TextField(null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    content = models.JSONField(null=True, blank=True)

    @property
    def is_delete(self):
        if self.deletedTime is None:
            return -1
        else:
            return 1

    def save(self, *args, **kwargs):
        if not self.id:
            self.createTime = datetime.datetime.now()
        super(Project, self).save(*args, **kwargs)

    def serialize(self, with_content: bool = False):
        res = {
            "id": str(self.id),
            "projectName": self.name,
            "state": self.state,
            "createTime": self.createTime.strftime("%Y-%m-%d %H:%M:%S"),
            "createUserId": self.createUserId,
            "isDelete": self.is_delete,
            "indexImage": self.cover,
            "remarks": self.remarks
        }
        if with_content:
            res["content"] = self.content
        return res
