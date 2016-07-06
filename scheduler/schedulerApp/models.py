from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkSheet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return u'%s'%(self.name);
class WorkTime(models.Model):
    name = models.CharField(max_length=30)#, verbose_name='sas')
    start = models.DateTimeField()
    end = models.DateTimeField( blank=True,null = True)
    workSheet = models.ForeignKey(WorkSheet)

    def duration(self):
        return self.end - self.start
    def __unicode__(self):
        return u"%s %s %s" % (self.name, self.start, self.end)
    class Meta:
        ordering = ['start']
class Profile(models.Model):
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    user = models.OneToOneField(User)
