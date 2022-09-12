from django.db import models


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
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    dob = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    previous_positions = models.ManyToManyField(Position, related_name='previous_positions')
    vacations = models.ManyToManyField(Vacation, related_name='vacations')

    def __str__(self):
        return self.name