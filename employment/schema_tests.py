import pytest
from employment.models import Employee
from graphene.test import Client
from fedhr.schema import schema

client = Client(schema)

@pytest.mark.django_db
def test_resolve_all_employees():
    Employee.objects.create(first_name='Gilbert', last_name='Twesigomwe')
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
    assert result == {
        "data": {
            "allEmployees": [
            {
                "firstName": "Gilbert",
                "lastName": "Twesigomwe"
            },
            {
                "firstName": "Ambrose",
                "lastName": "Tumwijukye"
            }
            ]
        }
    }
    assert 'errors' not in result


@pytest.mark.django_db
def test_resolve_employee_by_first_name():
    Employee.objects.create(first_name='Ambrose', last_name='Tumwijukye')
    query = '''
        query {
            employeeByFirstName(firstName: "Ambrose") {
                firstName
                lastName
            }
        }
    '''

    result = client.execute(query)
    assert result == {
        "data": {
            "employeeByFirstName": {
            "firstName": "Ambrose",
            "lastName": "Tumwijukye"
            }
        }
    }
    assert 'errors' not in result
