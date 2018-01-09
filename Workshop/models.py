from django.db import models
from multiselectfield import MultiSelectField
class Details(models.Model):
    WORKSHOPS = (

        ('workshop 1', 'Workshop 1'),
        ('workshop 2', 'Workshop 2'),
        ('workshop 3', 'Workshop 3'),
        ('workshop 4', 'Workshop 4')
    )

    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=250)
    Mobile = models.IntegerField(max_length=10)
    Workshop = MultiSelectField(choices=WORKSHOPS)

    def __str__(self):
        return self.Name + ' - ' + self.Email
