from .managers import UserManager, SupportManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import uuid


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    admin = models.BooleanField(default=False, null=True)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    support = models.BooleanField(default=False)
    faculty = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, null=True)
    picture = models.ImageField(upload_to='image/', default='image/avatar.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return str(f"Name: {self.first_name} {self.last_name}, Email: {self.email}")

    @property
    def is_support(self):
        return self.support

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_student(self):
        return self.student

    @property
    def is_faculty(self):
        return self.faculty


class StudentModel(CustomUser):
    student_phone = models.CharField(max_length=11, null=True, db_index=True)
    student_grade = models.CharField(max_length=255, null=False)
    student_school = models.CharField(max_length=100, null=False, default="N/A")
    student_college = models.CharField(max_length=100, null=False, default="N/A")
    student_city = models.CharField(max_length=100, null=True)
    student_state = models.CharField(max_length=100, null=True)
    student_country = models.CharField(max_length=100, null=True)
    student_parent_name = models.CharField(max_length=100, null=True)
    student_parent_email = models.EmailField(max_length=100, null=True)
    student_parent_phone = models.CharField(max_length=15, null=True)
    student_date_joined = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_phone', 'student_grade', 'student_school', 'student_college']

    objects = UserManager()

    def __str__(self):
        return str(f"Name: {self.first_name} {self.last_name}, Email: {self.email}")

    class Meta:
        db_table = "student_model"


class FacultyModel(CustomUser):
    faculty_phone = models.CharField(max_length=11, null=True, db_index=True)
    faculty_qualification = models.CharField(max_length=255, null=False)
    faculty_college = models.CharField(max_length=100, null=False)
    faculty_designation = models.CharField(max_length=100, null=True)
    faculty_expertise = models.CharField(max_length=100, null=True)
    faculty_introduction = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['faculty_qualification', 'faculty_college']

    objects = UserManager()

    def __str__(self):
        return str(f"Name: {self.first_name} {self.last_name}, Email: {self.email}")

    class Meta:
        db_table = "faculty_model"
