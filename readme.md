-------------------------------
Business Area Project
-------------------------------

The purpose of the project is as follows:
The information system is designed to record personal data of the company's employees. 
The company is divided into departments, each of which has a name, an abbreviation and a manager. No more than 20 employees can work in each department. 
Each employee is characterized by his/her identification number, surname, first name, patronymic, passport data, date and place of birth, home address. 
An employee works in a certain position, for which he receives a salary. 
For each year worked at the company, the employee's salary increases by 1.2%. An employee can change positions, 
the information system must store the history of the employee's previous positions. An employee has a vacation every year, 
the duration of which depends on the position and is measured in days per calendar year of work. The system must store data on all employee vacations. 
No more than 5 employees of one department can be on vacation at the same time.

The system should issue reports:
1. A list of employees of the department (department - parameter)
2. A list of employees with an indication of the periods of vacations used with a summary of the days spent on vacations for each employee
3. Report of the employee indicating the position and salary
4. A list of departments with indication of the manager and the number of employees


To run the project:
    -create a local virtual envoirnment and execute the command "pip install -r requirements.txt" to install any dependancies
    -go into the "Business_area" directory
    -create a local database with postgres
    -update settings to work with database
    -run local server using "python manage.py runserver" command

To do and expected time for each objective, actual time taken for completion will be updates as tasks are completed:  expected|taken
    -Basic setup with postgres and admin                                                                                    1h|45m
    -Setup of models as well as serializers                                                                                 3h|1.5h
    -Setup methods for models and recording of history of previous vacations and positions                                  4h|2h
    -Api endpoints to access information and create new entries                                                             7h|4h
    -Tests                                                                                                                  5h|4h

Api enpoints are as follows:
    -department/ - returns all departments
    -department/<int:id>/ - works with GET, PUT, DELETE methods, returns department with id
    -position/ - returns all positions
    -position/<int:id>/ - works with GET, PUT, DELETE methods, returns position with id
    -employee/ - returns all employees
    -employee/<int:id>/ - works with GET, PUT, DELETE methods, returns employee with id
    -add_employee_to_department/ - works with POST method, adds employee to department
    -give_raise/<int:id>/ - works with POST method, gives raise to employee with id, if working for more than 1 year
    -give_vacation/<int:id>/ - works with POST method, gives vacation to employee with id, if working for more than 1 year
    -change_position/ - works with POST method, changes position of employee with id, if working for more than 1 year




