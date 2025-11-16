from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.class_group.name})"

class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.class_group.name} | {self.subject.name} | {self.time}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} — {self.subject.name}: {self.value}"