from django.contrib import admin
from api.models import School,Student,Gallery
from django.utils.html import format_html
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportMixin
# Register your models here.

class StudentResource(resources.ModelResource):
    school = fields.Field(
        column_name='school',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name'))
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id']
        exclude = ('is_active', 'created_at', 'updated_at')
    def before_import_row(self, row, **kwargs):
        school_name = row.get('school')
        if school_name:
            school, created = School.objects.get_or_create(name=school_name)
            row['school'] = school

class StudentImportForm(ImportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ('name', 'address', 'phone', 'school')
            

@admin.register(School)
class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'district', 'phone', 'pincode')

@admin.register(Student)
class StudentModelAdmin(StudentImportForm):
    list_display = ('name', 'address', 'phone', 'school')

@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')
    def display_image(self, obj):
        if obj.id:
            return format_html('<a href="{}"><img src="{}" width="120" height="80" /></a>', obj.image.url,obj.image.url)
        else:
            return "Not Saved Yet"
    display_image.short_description = 'Image'




    

  

