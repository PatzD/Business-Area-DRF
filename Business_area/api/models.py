from django.db import models
from datetime import datetime, timedelta


#department model 
class Department(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='manager', null=True, blank=True)

    def __str__(self):
        return self.name


#position model for employees
class Position(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    vacation_days = models.IntegerField()

    def __str__(self):
        return self.name


#vacation model to keep track of employee vacation days
class Vacation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.employee


#employe model to keep track of employee information
class Employee(models.Model):
    id_mum = models.IntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    salary = models.IntegerField()
    dob = models.DateField()
    position = models.CharField(max_length=50)
    previous_positions = models.ManyToManyField(Position, related_name='previous_positions')
    vacation_days = models.IntegerField()
    vacations = models.ManyToManyField(Vacation, related_name='vacations')
    last_raise = models.DateField(default=datetime.now)

    #method to give employee raise if they have been with the company for 1 year or has been 1 year since last raise, gives raise of 1.2%
    def give_raise(self):
        if self.last_raise < datetime() - timedelta(days=365):
            self.salary = self.salary * 1.012
            self.last_raise = datetime.now()
            self.save() 
    
    #method to create vacation for employee and store it in vacations of employee model, also checks if employee has enough vacation days to take vacation
    def create_vacation(self, start_date, end_date):
        if self.vacation_days > (end_date - start_date).days:
            vacation = Vacation(start_date=start_date, end_date=end_date)
            vacation.save()
            self.vacations.add(vacation)
            self.vacation_days -= (end_date - start_date).days
            self.save()
        else:
            return("Not enough vacation days")
    
    #method to change employee position, changes vacation days and salary of employee to that of position, stores previous position in previous_positions of employee model
    def change_position(self, position):
        self.previous_positions.add(self.position)
        self.position = position
        self.vacation_days = position.vacation_days
        self.salary = position.salary
        self.save()


    def __str__(self):
        return self.name