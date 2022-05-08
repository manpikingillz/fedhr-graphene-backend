import graphene
from graphene_django import DjangoObjectType

from employment.models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')


class EmployeeQueries(graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)
    employee_by_first_name = graphene.Field(EmployeeType, first_name=graphene.String())

    def resolve_all_employees(root, info):
        return Employee.objects.all()

    def resolve_employee_by_first_name(root, info, first_name):
        return Employee.objects.get(first_name=first_name)


class CreateEmployee(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        middle_name = graphene.String(required=False)
        last_name = graphene.String(required=True)

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


class UpdateEmployee(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name):
        employee = Employee.objects.get(first_name=first_name)
        employee.last_name = last_name
        employee.save()
        return UpdateEmployee(employee=employee)


class DeleteEmployee(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, first_name):
        employee = Employee.objects.get(first_name=first_name)
        employee.delete()
        return DeleteEmployee(employee=employee)


class EmployeeMutations(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()


schema = graphene.Schema(query=EmployeeQueries, mutation=EmployeeMutations)
