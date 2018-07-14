from django.db import models

# Create your models here.
class Add(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Add #{}'.format(self.id) #this returns the objectid for each data added

    class Meta:
        verbose_name_plural = 'Added'

    