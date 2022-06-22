from employment.models import Employee

# TODO: How do we handle functions with very many attributes.
def create_employment(
    first_name: str,
    middle_name: str,
    last_name: str,
    date_of_birth: str,
    gender: int,
) -> Employee:
    employee = Employee(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender
    )

    employee.full_clean()
    employee.save()

    return employee