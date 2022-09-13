from django.urls import path
from . views import department, department_detail, position, position_detail, employee, employee_detail, add_employee_to_department, give_raise, give_vacation, change_position

urlpatterns = [
    path('department/', department, name='department'),
    path('department/<int:id>/', department_detail, name='department_detail'),
    path('position/', position, name='position'),
    path('position/<int:id>/', position_detail, name='position_detail'),
    path('employee/', employee, name="employee"),
    path('employee/<int:id>/', employee_detail, name="employee_detail"),
    path('add_employee_to_department/', add_employee_to_department, name="add_employee_to_department"),
    path('give_raise/<int:id>/', give_raise, name="give_raise"),
    path('give_vacation/<int:id>/', give_vacation, name="give_vacation"),
    path('change_position/', change_position, name="change_position"),
]