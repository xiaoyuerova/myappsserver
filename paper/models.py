from django.db import models

# Create your models here.


class Paper(models.Model):
    """
    Model representing an author.
    """
    Uid = models.CharField(max_length=100, null=False)
    Title = models.CharField(max_length=500, null=False)
    Author = models.CharField(max_length=200)
    Abstract = models.CharField(max_length=4000)
    Title_CN = models.CharField(max_length=500)
    Abstract_CN = models.CharField(max_length=4000)
    Link = models.CharField(max_length=100)
    Meeting = models.CharField(max_length=50)
    Complete = models.BooleanField(default=False)
    Locked = models.BooleanField(default=False)
    Select1 = models.BooleanField(default=False)
    Select2 = models.BooleanField(default=False)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.Uid, self.Title)

