from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, timedelta

# Create your models here.

class BaseModel(models.Model):
    # TODO: find out difference between using auto_now_add and default=timezone.now
    # Find out more on db_index=True
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(BaseModel):
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

    '''
        1. If we need a simple derived value, based on non-relational model fields,
        add @property for that.
        2. If the calculation of the derived value is simple enough.

        Don't use a property;
        - If you need to span multiple relations or fetch additional data.
        - If the calculation is more complex.
    '''
    def full_name(self) -> str:
        middle_name = self.middle_name or ''
        full_name = f'{self.first_name} {middle_name} {self.last_name}'
        return ' '.join(full_name.split())

    '''
    Validation added to clean if;
        1. We're validating based on multiple, non-relational fields, of the model
        2. the validation itself is simple enough

    Validation moved to service layer if:
        1. THe validation logic is more complex
        2. Spanning relations and fetching additional data is required
    Can also use validation constrains https://github.com/hacksoftware/django-styleguide#validation---constraints,
    but because we get Integrity error, it's a downside to the approach that handles ValidationError
    '''
    def clean(self):
        if not isinstance(self.gender, int):
            raise ValidationError("Gender value not correct")

    '''
        This is a model method. It can't be a property because it takes an argument.

        We can use a method;
        1. If we need a simple derived value, that requires arguments, based on non-relational model fields.
        2. If the calculation of the derived value is simple enough.
        3. If setting one attribute always requires setting values to other attribute.
    '''
    def is_teenager(self, age: int) -> bool:
        employee_age = (date.today() - self.birth_date) // timedelta(days=365.2425)
        return employee_age < 20