from django.contrib import admin
from .models import Formone, Education, UploadingDocument

# Register your models here.
@admin.register(Formone)
class FormoneAdmin(admin.ModelAdmin):
    list_display=['name','lastname','date_of_birth','email','father_name',
                  'fathernamelast','mother_name','mothernamelast','gender','nationality',
                  'home_Address','city','country','telephone_home','telephone_mobile']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=['HSC_Institute_name','HSC_Board','score_in_HSC','SSC_Institute_name','SSC_board','score_SSC','Currently_pursuing','Current_education_institution_name','Overall_percentage','current_backlog']


@admin.register(UploadingDocument)
class UploadingDocumentAdmin(admin.ModelAdmin):
    list_display=['photo','HSC_mark_sheet','SSC_mark_sheet','all_semesters_mark_sheet']