from django.db import models

class Contact(models.Model):
    subject_choices=(
        ('A','Subject'),
        ('B', 'Feedback'),
        ('C', 'Order')
    )
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=100,choices=subject_choices,default='A')
    message=models.CharField(max_length=800)

    def __str__(self):
        return self.name
