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

# class GenderEnum(graphene.Enum):
#     MALE = 1
#     MALE = 2

class CreateEmployee(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        middle_name = graphene.String(required=False)
        last_name = graphene.String(required=True)
        # date_of_birth = graphene.DateTime(required=False)
        # gender = graphene.Enum.from_enum(GenderEnum)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, first_name, middle_name, last_name):
        employee = Employee(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        employee.save()
        return CreateEmployee(employee=employee)

class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)