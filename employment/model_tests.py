
from employment.models import Employee

def test_string_representation():
    employee = Employee(first_name='Ambrose', last_name='Tumwijukye')
    assert str(employee) == 'Ambrose Tumwijukye'

def test_employee_full_name_with_all_three_names():
    employee = Employee(first_name='Ambrose', middle_name='Savimbi', last_name='Tumwijukye')
    assert employee.full_name() == 'Ambrose Savimbi Tumwijukye'

def test_employee_full_name_with_only_two_names():
    employee = Employee(first_name='Ambrose', last_name='Tumwijukye')
    assert employee.full_name() == 'Ambrose Tumwijuky'
