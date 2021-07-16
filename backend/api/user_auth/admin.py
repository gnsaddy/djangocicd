from django.contrib import admin
from .models import CustomUser, FacultyModel, StudentModel


class StudentModelList(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'gender', 'student_phone', 'student_grade',
        'student_city', 'student_parent_name', 'student_parent_email', 'student_parent_phone', 'last_login')

    list_display_links = ('email', 'id', 'student_phone')
    search_fields = (
        'email', 'first_name', 'last_name', 'student_city', 'student_state', 'student_school', 'student_college')
    list_per_page = 50
    date_hierarchy = 'created_at'
    readonly_fields = ('id', 'sid', 'created_at', 'updated_at',)

    fields = (
        'id', 'sid', 'first_name', 'last_name', 'email', 'password', 'gender', 'picture', 'student', 'active',
        'student_phone', 'student_grade', 'student_school', 'student_college', 'student_city', 'student_state',
        'student_country', 'student_parent_name', 'student_parent_email', 'student_parent_phone', 'student_date_joined',
        'created_at', 'last_login')
    actions = ('set_student_to_unavailable', 'set_student_to_available')

    def get_ordering(self, request):
        if request.user.is_superuser:
            return 'first_name', 'created_at'
        return 'first_name', 'created_at'

    def set_student_to_unavailable(self, request, queryset):
        count = queryset.update(student=False)
        self.message_user(request, f'{count} student(s) is/are now unavailable')

    set_student_to_unavailable.short_description = 'Mark Student Service unavailable'

    def set_student_to_available(self, request, queryset):
        count = queryset.update(student=True)
        self.message_user(request, f'{count} student(s) is/are now available')

    set_student_to_available.short_description = 'Mark Student Service available'


class FacultyModelList(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'gender', 'faculty_phone', 'faculty_qualification',
        'faculty_college', 'faculty_designation', 'faculty_expertise', 'faculty_introduction', 'last_login')

    list_display_links = ('email', 'id', 'faculty_phone')
    search_fields = (
        'email', 'first_name', 'last_name', 'faculty_qualification', 'faculty_expertise')
    list_per_page = 50
    date_hierarchy = 'created_at'
    readonly_fields = ('id', 'sid', 'created_at', 'updated_at',)

    fields = (
        'id', 'sid', 'first_name', 'last_name', 'email', 'password', 'gender', 'picture', 'faculty', 'active',
        'faculty_phone', 'faculty_qualification', 'faculty_college', 'faculty_designation', 'faculty_expertise',
        'faculty_introduction', 'created_at', 'last_login')

    actions = ('set_faculty_to_unavailable', 'set_faculty_to_available')

    def get_ordering(self, request):
        if request.user.is_superuser:
            return 'first_name', 'created_at'
        return 'first_name', 'created_at'

    def set_faculty_to_unavailable(self, request, queryset):
        count = queryset.update(faculty=False)
        self.message_user(request, f'{count} faculty(s) is/are now unavailable')

    set_faculty_to_unavailable.short_description = 'Mark Faculty Service unavailable'

    def set_faculty_to_available(self, request, queryset):
        count = queryset.update(faculty=True)
        self.message_user(request, f'{count} faculty(s) is/are now available')

    set_faculty_to_available.short_description = 'Mark Faculty Service available'


admin.site.register(FacultyModel, FacultyModelList)
admin.site.register(StudentModel, StudentModelList)


# for custom user model
class UserList(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'active', 'student', 'faculty', 'support', 'staff', 'admin',
        'created_at')
    list_display_links = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    list_per_page = 50
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'sid', 'id')

    fields = (
        'id', 'sid', 'first_name', 'last_name', 'email', 'password', 'gender', 'picture', 'active', 'student',
        'faculty', 'support', 'staff', 'admin', 'created_at', 'updated_at', 'last_login')

    def get_ordering(self, request):
        if request.user.is_superuser:
            return 'first_name', 'created_at'
        return 'first_name', 'created_at'


admin.site.register(CustomUser, UserList)
