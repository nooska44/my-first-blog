from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #this line defines our model (it is an object).
    #Post is the name of our model
    #models.Model django model so saves to database
    #models.ForeignKey links to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
#__str__ returns a string
    def __str__(self):
        return self.title
