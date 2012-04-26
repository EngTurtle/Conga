from django.contrib.auth.models import User
from django.db import models
from settings import MIN_STORAGE_QUOTA

class Student(models.Model):
    user = models.OneToOneField(User)
    student_number = models.SmallIntegerField(verbose_name = 'student number',
                                              unique = True)
    storage_quota = models.SmallIntegerField(verbose_name = 'Storage Space',
                                             default = MIN_STORAGE_QUOTA)

    def __unicode__(self):
        return self.user.username