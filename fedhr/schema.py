import graphene
from graphene_django import DjangoObjectType

from employment.models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')

class Query(graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)
    employee_by_first_name = graphene.Field(EmployeeType, first_name=graphene.String())

    def resolve_all_employees(root, info):
        return Employee.objects.all()
    
    def resolve_employee_by_first_name(root, info, first_name):
        return Employee.objects.get(first_name=first_name)

schema = graphene.Schema(query=Query)