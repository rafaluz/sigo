from django.urls import path
from . import views as my_views

app_name = "school"

urlpatterns = [
    # ClassShift
    path('class_shift/add', my_views.ClassShiftCreate.as_view(), name='class_shift_create'),
    path('class_shift/edit/<int:pk>', my_views.ClassShiftUpdate.as_view(), name='class_shift_update'),
    path('class_shift/delete/<int:pk>', my_views.ClassShiftDelete.as_view(), name='class_shift_delete'),

    # TimeTable
    path('time_table/add/<int:class_shift_pk>', my_views.TimeTableCreate.as_view(), name='time_table_create'),
    path('time_table/edit/<int:class_shift_pk>/<int:pk>', my_views.TimeTableUpdate.as_view(), name='time_table_update'),
    path('time_table/delete/<int:class_shift_pk>/<int:pk>', my_views.TimeTableDelete.as_view(), name='time_table_delete'),
] 