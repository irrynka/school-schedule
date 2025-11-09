from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Subject")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Teacher")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.subject:
            return f"{self.name} ({self.subject.name})"
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50, default="Unnamed Class")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Student")
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.class_group:
            return f"{self.name} ({self.class_group.name})"
        return self.name
