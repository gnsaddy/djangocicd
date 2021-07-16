from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_active=True, is_support=False, is_superuser=False,
                    is_faculty=False, is_staff=False, is_student=False,
                    **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.admin = is_superuser
        user.staff = is_staff
        user.active = is_active
        user.support = is_support
        user.faculty = is_faculty
        user.student = is_student
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


class SupportManager(BaseUserManager):

    def create_support_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_support', True)
        extra_fields.setdefault('is_staff', True)
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        support_user = self.model(email=email, **extra_fields)
        support_user.set_password(password)
        support_user.save()
        return support_user
