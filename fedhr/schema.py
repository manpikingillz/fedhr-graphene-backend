import graphene
from graphene_django import DjangoObjectType

from employment.models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'

class Query(graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)

    def resolve_all_employees(root, info):
        return Employee.objects.all()

schema = graphene.Schema(query=Query)