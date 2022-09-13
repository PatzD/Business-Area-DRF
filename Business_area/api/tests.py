from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Department, Position, Employee, Vacation
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, VacationSerializer

"""
crud tests for department
"""
class CRUDDepartmentTest(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name='IT', abbreviation='IT1')
        self.department_serializer = DepartmentSerializer(self.department)
        self.department_data = self.department_serializer.data

    def test_get_department(self):
        response = self.client.get(reverse('department'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.department_data])

    def test_post_department(self):
        #create a new department and POST it
        new_department = Department.objects.create(name='IT2', abbreviation='IT2')
        new_department_serializer = DepartmentSerializer(new_department)
        new_department_data = new_department_serializer.data
        response = self.client.post(reverse('department'), new_department_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_department_detail(self): #test to get department by id
        response = self.client.get(reverse('department_detail', kwargs={'id': self.department.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.department_data)

    def test_delete_department_detail(self): #test to delete department
        response = self.client.delete(reverse('department_detail', kwargs={'id': self.department.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_department_detail(self):
        #create new department
        new_department = Department.objects.create(name='IT3', abbreviation='IT3')
        new_department_serializer = DepartmentSerializer(new_department)
        new_department_data = new_department_serializer.data
        #update department
        response = self.client.put(reverse('department_detail', kwargs={'id': self.department.id}), new_department_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, new_department_data)
    
    def tast_add_employee_to_department(self):
        #create new employee
        new_employee = Employee.objects.create(name='John', position="Developer", salary=1000, dob='1990-01-01')
        new_employee_serializer = EmployeeSerializer(new_employee)
        new_employee_data = new_employee_serializer.data
        #add employee to department
        response = self.client.put(reverse('add_employee_to_department'), new_employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

"""
crud tests for position
"""
class CRUDPositionTest(APITestCase):
    def setUp(self):
        self.position = Position.objects.create(name='Developer', salary=1000, vacation_days=20) 
        self.position_serializer = PositionSerializer(self.position)
        self.position_data = self.position_serializer.data

    def test_get_position(self):
        response = self.client.get(reverse('position'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.position_data])
    
    def test_post_position(self):
        #create a new position and POST it
        new_position = Position.objects.create(name='Developer2', salary=2000, vacation_days=30)
        new_position_serializer = PositionSerializer(new_position)
        new_position_data = new_position_serializer.data
        response = self.client.post(reverse('position'), new_position_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_position_detail(self): #test to get position by id
        response = self.client.get(reverse('position_detail', kwargs={'id': self.position.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_position_detail(self): #test to delete position
        response = self.client.delete(reverse('position_detail', kwargs={'id': self.position.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_put_position_detail(self):
        #create new position
        new_position = Position.objects.create(name='Developer3', salary=3000, vacation_days=40)
        new_position_serializer = PositionSerializer(new_position)
        new_position_data = new_position_serializer.data
        #update position
        response = self.client.put(reverse('position_detail', kwargs={'id': self.position.id}), new_position_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, new_position_data)

"""
crud tests for employee
"""
class CRUDEmployeeTest(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John', position="Developer", salary=1000, dob='1990-01-01')
        self.employee_serializer = EmployeeSerializer(self.employee)
        self.employee_data = self.employee_serializer.data
    
    def test_get_employee(self):
        response = self.client.get(reverse('employee'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.employee_data])
    
    def test_post_employee(self):
        #create a new employee and POST it
        new_employee = Employee.objects.create(first_name='John2', last_name='Smith2', position="Developer2", salary=2000, dob='1990-01-01')
        new_employee_serializer = EmployeeSerializer(new_employee)
        new_employee_data = new_employee_serializer.data
        response = self.client.post(reverse('employee'), new_employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_employee_detail(self): #test to get employee by id
        response = self.client.get(reverse('employee_detail', kwargs={'id': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee_detail(self): #test to delete employee
        response = self.client.delete(reverse('employee_detail', kwargs={'id': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_put_employee_detail(self):
        #create new employee
        new_employee = Employee.objects.create(first_name='John3', last_name='Smith3', position="Developer3", salary=3000, dob='1990-01-01')
        new_employee_serializer = EmployeeSerializer(new_employee)
        new_employee_data = new_employee_serializer.data
        #update employee
        response = self.client.put(reverse('employee_detail', kwargs={'id': self.employee.id}), new_employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, new_employee_data)
    
    def test_give_employee_vacation(self):
        #create new vacation
        new_vacation = Vacation.objects.create(start_date='2018-01-01', end_date='2018-01-02')
        new_vacation_serializer = VacationSerializer(new_vacation)
        new_vacation_data = new_vacation_serializer.data
        #give employee vacation
        response = self.client.put(reverse('give_vacation', kwargs={"id":self.employee.id}), new_vacation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_give_employee_raise(self):
        #give employee raise
        response = self.client.put(reverse('give_raise', kwargs={"id":self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
