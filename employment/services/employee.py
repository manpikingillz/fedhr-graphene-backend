from employment.models import Employee
from django.db import transaction
'''
    Services are where business logic lives.
    Services can be function based, or class based.
    using class-based services is a good idea for "flows" - things that go thru multiple steps.
    
    Testing services:
    - The tests should cover the business logic in an exhausitive manner
    - The tests should hit the database - creating & updating from it
    - The tests should mock async task calls & everything that goes outside the project.
'''

class EmployeeService: 
    

    # TODO: How do we handle functions with very many attributes.
    # Naming convention: <entity>_<action>
    @transaction.atomic
    def employee_create(self, middle_name: str, last_name: str, date_of_birth: str, gender: int) -> Employee:
        employee = Employee(first_name=self, middle_name=middle_name, last_name=last_name, date_of_birth=date_of_birth, gender=gender)


        employee.full_clean()
        employee.save()

        return employee
    
    # TODO: Implement update
    @transaction.atomic
    def employee_update(self, ):
        pass