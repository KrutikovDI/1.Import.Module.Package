from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(calculate_salary(55000))
    print(get_employees(2))
    print(datetime.now().date())