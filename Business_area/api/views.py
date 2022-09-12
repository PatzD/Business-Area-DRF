from unicodedata import name
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, VacationSerializer

"""
department views
"""
@api_view(['GET', 'POST'])
def department(request):
    #GET list of all departments
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return Response(departments_serializer.data, status=status.HTTP_200_OK)

    #POST new department
    elif request.method == 'POST':
        #parsing data from request
        department_data = JSONParser().parse(request)
        #serializing data
        department_serializer = DepartmentSerializer(data=department_data)
        #checking validity
        if department_serializer.is_valid():
            #saving data
            department_serializer.save()
            #returning response
            return Response(department_serializer.data, status=status.HTTP_201_CREATED)
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def department_detail(request, id):
    #GET specific department 
    if request.method == 'GET':
        department = Department.objects.get(id=id)
        department_serializer = DepartmentSerializer(department)
        return Response(department_serializer.data, status=status.HTTP_200_OK)

    #DELETE specific department
    if request.method == 'DELETE':
        #getting department by id
        department = Department.objects.get(id=id)
        #deleting department
        department.delete()
        #returning response
        return Response(status=status.HTTP_204_NO_CONTENT)

    #PUT update specific department
    elif request.method == 'PUT':
        #getting department by id
        department = Department.objects.get(id=id)
        #parsing data from request
        department_data = JSONParser().parse(request)
        #serializing data
        department_serializer = DepartmentSerializer(department, data=department_data)
        #checking validity
        if department_serializer.is_valid():
            #saving data
            department_serializer.save()
            #returning response
            return Response(department_serializer.data, status=status.HTTP_200_OK)
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#add employee to department
@api_view(['POST'])
def add_employee_to_department(request):
    #getting department by id from request
    department = Department.objects.get(id=request.data['department_id'])
    #getting employee by id from request
    employee = Employee.objects.get(id=request.data['employee_id'])
    #adding employee to department
    department.employees.add(employee)
    return Response(status=status.HTTP_200_OK)

"""
position views
"""
@api_view(['GET', 'POST'])
def position(request):
    #GET list of all positions
    if request.method == 'GET':
        positions = Position.objects.all()
        positions_serializer = PositionSerializer(positions, many=True)
        return Response(positions_serializer.data, status=status.HTTP_200_OK)

    #POST new position
    elif request.method == 'POST':
        #parsing data from request
        position_data = JSONParser().parse(request)
        #serializing data
        position_serializer = PositionSerializer(data=position_data)
        #checking validity
        if position_serializer.is_valid():
            #saving data
            position_serializer.save()
            #returning response
            return Response(position_serializer.data, status=status.HTTP_201_CREATED)
        return Response(position_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def position_detail(request, id):
    #GET specific position
    if request.method == 'GET':
        #getting position by id
        position = Position.objects.get(id=id)
        #serializing data
        position_serializer = PositionSerializer(position)
        #returning response
        return Response(position_serializer.data, status=status.HTTP_200_OK)

    #DELETE specific position
    elif request.method == 'DELETE':
        #getting position by id
        position = Position.objects.get(id=id)
        #deleting position
        position.delete()
        #returning response
        return Response(status=status.HTTP_204_NO_CONTENT)

    #PUT update specific position
    elif request.method == 'PUT':
        #getting position by id
        position = Position.objects.get(id=id)
        #parsing data from request
        position_data = JSONParser().parse(request)
        #serializing data
        position_serializer = PositionSerializer(position, data=position_data)
        #checking validity
        if position_serializer.is_valid():
            #saving data
            position_serializer.save()
            #returning response
            return Response(position_serializer.data, status=status.HTTP_200_OK)
        return Response(position_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
employee views
"""
@api_view(['GET', 'POST'])
def employee(request):
    #GET list of all employees
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return Response(employees_serializer.data, status=status.HTTP_200_OK)

    #POST new employee
    elif request.method == 'POST':
        #parsing data from request
        employee_data = JSONParser().parse(request)
        #serializing data
        employee_serializer = EmployeeSerializer(data=employee_data)
        #checking validity
        if employee_serializer.is_valid():
            #saving data
            employee_serializer.save()
            #returning response
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def employee_detail(request, id):
    #GET specific employee
    if request.method == 'GET':
        #getting employee by id
        employee = Employee.objects.get(id=id)
        #serializing data
        employee_serializer = EmployeeSerializer(employee)
        #returning response
        return Response(employee_serializer.data, status=status.HTTP_200_OK)

    #DELETE specific employee
    elif request.method == 'DELETE':
        #getting employee by id
        employee = Employee.objects.get(id=id)
        #deleting employee
        employee.delete()
        #returning response
        return Response(status=status.HTTP_204_NO_CONTENT)

    #PUT update specific employee
    elif request.method == 'PUT':
        #getting employee by id
        employee = Employee.objects.get(id=id)
        #parsing data from request
        employee_data = JSONParser().parse(request)
        #serializing data
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        #checking validity
        if employee_serializer.is_valid():
            #saving data
            employee_serializer.save()
            #returning response
            return Response(employee_serializer.data, status=status.HTTP_200_OK)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint for giving vacation to employee
@api_view(['POST'])
def give_vacation(request, id):
    #getting employee by id
    employee = Employee.objects.get(id=id)
    #parsing data from request
    vacation_data = JSONParser().parse(request)
    #serializing data
    vacation_serializer = VacationSerializer(data=vacation_data)
    #checking validity
    if vacation_serializer.is_valid():
        employee.create_vacation(vacation_serializer.validated_data['start_date'], vacation_serializer.validated_data['end_date'])
        return Response(status=status.HTTP_201_CREATED)
    return Response(vacation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint for giving raise to employee
@api_view(['POST'])
def give_raise(request, id):
    #getting employee by id
    employee = Employee.objects.get(id=id)
    employee.give_raise()
    return Response(status=status.HTTP_200_OK)

#endpoint for changing position of employee
@api_view(['POST'])
def change_position(request):
    #getting employee by id from request
    employee = Employee.objects.get(id=request.data['employee_id'])
    #getting position by id from request
    position = Position.objects.get(id=request.data['position_id'])
    #add previous position to employee history
    employee.previous_positions.add(Position.objects.get(name=employee.position).id)
    #change position of employee
    employee.position = position.name
    #save changes
    employee.save()
    return Response(status=status.HTTP_200_OK)