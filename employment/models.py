from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, timedelta
from users.models import ExtendUser

# Create your models here.

class BaseModel(models.Model):
    # TODO: find out difference between using auto_now_add and default=timezone.now
    # Find out more on db_index=True
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(BaseModel):
    # Options
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    
    SINGLE=1
    MARRIED=2
    SEPARATED=3
    DIVORCED=4
    WIDOWED=5
    MARITAL_STATUS_CHOICES=(
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (SEPARATED, 'Separated'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed'),
    )
    

    # Personal Details
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender =  models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.IntegerField(choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    
    # Identification Information
    nssf_number = models.CharField(max_length=50, null=True, blank=True) # National Social Security Fund (Ugandan)
    nhif_number = models.CharField(max_length=50, null=True, blank=True) # nATIONAL Hospital Insurance Fund (Kenyan)
    nin = models.CharField(max_length=50, null=True, blank=True) # National Idetinfication Number
    tin_number = models.CharField(max_length=50, null=True, blank=True) # Tax Identification Number
    
    # Contact Information
    email = models.CharField(max_length=255, null=True, blank=True)
    home_email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    work_phone = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    
    # Address Information
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    # TODO: Add Country Model
    country = models.ForeignKey(Country, ondelete=models.SET_NULL, null=True, blank=True)
    
    # Social
    linked_in = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    
    user = models.ForeignKey(ExtendUser, ondelete=models.SET_NULL, null=True, blank=True)

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