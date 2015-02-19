from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    passwd = models.CharField(max_length=100)
    user_id = models.AutoField(primary_key=True)

    def __unicode__(self):
	return unicode(self.user_id)
