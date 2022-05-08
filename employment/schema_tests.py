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


@pytest.mark.django_db
def test_create_employee_mutation():
    mutation = '''
        mutation employeeCreateMutation {
            createEmployee(
                firstName:"Test fn 1",
                middleName: "Test mn 1",
                lastName: "Test ln 1") {
                employee {
                    firstName
                    lastName
                }
            }
        }
    '''

    result = client.execute(mutation)
    assert result == {
        "data": {
            "createEmployee": {
                "employee": {
                    "firstName": "Test fn 1",
                    "lastName": "Test ln 1"
                }
            }
        }
    }
    assert 'errors' not in result


@pytest.mark.django_db
def test_update_employee_mutation():
    Employee.objects.create(first_name='Test fn 1', last_name='Test ln 1')
    mutation = '''
        mutation employeeUpdateMutation {
            updateEmployee(
                firstName: "Test fn 1"
                lastName:"Test ln 1 - updated"
            ){
                employee {
                    lastName
                    firstName
                }
            }
        }
    '''

    result = client.execute(mutation)
    assert result == {
        "data": {
            "updateEmployee": {
            "employee": {
                "lastName": "Test ln 1 - updated",
                "firstName": "Test fn 1"
            }
            }
        }
    }
    assert 'errors' not in result


@pytest.mark.django_db
def test_delete_employee_mutation():
    Employee.objects.create(first_name='John', last_name='Doe')
    mutation = '''
        mutation deleteMutation {
            deleteEmployee(firstName: "John") {
                employee {
                    firstName
                    lastName
                }
            }
        }
    '''

    result = client.execute(mutation)
    assert result == {
        "data": {
            "deleteEmployee": {
                "employee": {
                    "firstName": "John",
                    "lastName": "Doe"
                }
            }
        }
    }
    assert 'errors' not in result
