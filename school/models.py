from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "el_teacher"


class Student(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "el_student"


class Course(models.Model):
    name = models.CharField(max_length=255)
    tid = models.ForeignKey('Teacher', related_name='course_teachers', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "el_course"
    

class Enrolment(models.Model):
    cid = models.ForeignKey('Course', related_name='course_enrolments', on_delete=models.DO_NOTHING)
    sid = models.ForeignKey('Student', related_name='course_students', on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{sid.name} is enrolled for {cid.name}'

    class Meta:
        db_table = 'el_enrolment' 
