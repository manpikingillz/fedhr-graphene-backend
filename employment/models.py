from django.db import models

# Create your models here.
class Employee(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender =  models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        middle_name = self.middle_name if self.middle_name else ''
        full_name = f'{self.first_name} {middle_name} {self.last_name}'
        return ' '.join(full_name.split())