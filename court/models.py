from django.db import models

class Case(models.Model):
    case_number = models.CharField(max_length=100)
    case_title = models.CharField(max_length=200)
    case_description = models.TextField()
    date_filed = models.DateField()

    def __str__(self):
        return self.case_title

class Judge(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    current_cases = models.ManyToManyField(Case, related_name='judges')

    def __str__(self):
        return self.name

class Witness(models.Model):
    name = models.CharField(max_length=100)
    statement = models.TextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='witnesses')

    def __str__(self):
        return self.name

