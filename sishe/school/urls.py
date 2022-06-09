from django.urls import path
from . import views as my_views

app_name = "school"

urlpatterns = [
    # # ClassShift
    # path('class_shift/add', my_views.ClassShiftCreate.as_view(), name='class_shift_create'),
    # path('class_shift/edit/<int:pk>', my_views.ClassShiftUpdate.as_view(), name='class_shift_update'),
    # path('class_shift/delete/<int:pk>', my_views.ClassShiftDelete.as_view(), name='class_shift_delete'),

    # # TimeTable
    # path('time_table/add/<int:class_shift_pk>', my_views.TimeTableCreate.as_view(), name='time_table_create'),
    # path('time_table/edit/<int:class_shift_pk>/<int:pk>', my_views.TimeTableUpdate.as_view(), name='time_table_update'),
    # path('time_table/delete/<int:class_shift_pk>/<int:pk>', my_views.TimeTableDelete.as_view(), name='time_table_delete'),

    # Course
    path('course/add', my_views.CourseCreate.as_view(), name='course_create'),
    path('course/edit/<int:pk>', my_views.CourseUpdate.as_view(), name='course_update'),
    path('course/delete/<int:pk>', my_views.CourseDelete.as_view(), name='course_delete'),
    path('course/course_autocomplete/', my_views.CourseAutocomplete.as_view(), name='course_autocomplete'),

    # Semester
    path('semester/add', my_views.SemesterCreate.as_view(), name='semester_create'),
    path('semester/edit/<int:pk>', my_views.SemesterUpdate.as_view(), name='semester_update'),
    path('semester/delete/<int:pk>', my_views.SemesterDelete.as_view(), name='semester_delete'),

    # Grade
    path('grade/add/<int:semester_pk>', my_views.GradeCreate.as_view(), name='grade_create'),
    path('grade/edit/<int:semester_pk>/<int:pk>', my_views.GradeUpdate.as_view(), name='grade_update'),
    path('grade/delete/<int:semester_pk>/<int:pk>', my_views.GradeDelete.as_view(), name='grade_delete'),

    # CurricularComponent
    path('curricular_component/add/<int:grade_pk>', my_views.CurricularComponentCreate.as_view(), name='curricular_component_create'),
    path('curricular_component/edit/<int:grade_pk>/<int:pk>', my_views.CurricularComponentUpdate.as_view(), name='curricular_component_update'),
    path('curricular_component/delete/<int:grade_pk>/<int:pk>', my_views.CurricularComponentDelete.as_view(), name='curricular_component_delete'),

    # Schedule
    path('schedule/semester', my_views.ScheduleSemester.as_view(), name='schedule_semester'),
    path('schedule/grade/<int:semester_pk>', my_views.ScheduleSemesterGrade.as_view(), name='schedule_semester_grade'),
    path('schedule/curricular_component/<int:grade_pk>', my_views.ScheduleCurricularComponent.as_view(), name='schedule_curricular_component'),
    path('schedule/create', my_views.ScheduleCreate, name='schedule_create'),
    
] 


