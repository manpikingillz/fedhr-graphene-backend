
import json
import pytest
from graphene_django.utils.testing import graphql_query
from fedhr.schema import schema
from employment.models import Employee
from graphene.test import Client

# https://github.com/graphql-python/graphene/blob/master/examples/starwars/tests/test_query.py
# https://www.velotio.com/engineering-blog/use-pytest-fixtures-with-django-models
# https://fithis2001.medium.com/testing-graphql-for-the-beginner-pythonistas-79cdda9b722c
# https://www.programcreek.com/python/example/104864/graphene.Schema
# https://pytest-django.readthedocs.io/en/latest/helpers.html#assertions
# https://github.com/graphql-python/graphene-django/blob/main/examples/starwars/tests/test_connections.py

# Make video when the test is successful

# https://stackoverflow.com/questions/9574810/writing-test-cases-for-django-models
# 1. Testing that the model has the fields it should have

# 2. Test Queries

# 3. Test Mutations

# @pytest.fixture
# def employee(db) -> Employee:
#     employee = Employee.objects.create(first_name="Barnabas", last_name="Tumwekwase")
#     # print(f'employee: {employee}')
#     assert employee.first_name == "Barnabas"
    
# def test_filter_employee(employee):
#     assert Employee.objects.filter(first_name='Barnabas').exists()
    
# def test_update_employee(employee):
#     print(f'employee: {employee}')
    # employee.first_name = "Gilbert"
    # employee.save()
    # updated_employee = Employee.objects.get(first_name="Gilbert")
    # assert updated_employee.first_name == "Gilbert"
    

client = Client(schema)

@pytest.mark.django_db
def test_all_employees_query():
    Employee.objects.create(first_name='Ambrose', last_name='Tumwijukye')
    query = '''
        query {
            allEmployees {
                firstName
                lastName
            }
        }

        '''
    result = client.execute(query)
    # result = schema.execute(query)
    print(f'result: {result}')
    assert 'errors' not in result
    
# def test_create_employee()


