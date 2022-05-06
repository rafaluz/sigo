from django.urls import path   
# from .views import UserCreate, AxisCreate, AxisUpdate, AxisDelete
from . import views as my_views
from django.urls import reverse_lazy   
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "accounts"

urlpatterns = [ 
    path('accounts/user_create/', my_views.UserCreate.as_view(), name="user_create"),
    path('', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Alterar password
    path('password_change/', views.PasswordChangeView.as_view(
        template_name='user/password_change_form.html',
        success_url=reverse_lazy('accounts:password_change_done'),
        ), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(
        template_name='user/password_change_done.html',
        ), name='password_change_done'),
    #form para colocar email
    path('password_reset/', views.PasswordResetView.as_view(
        template_name='user/password_reset.html',
        email_template_name='user/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done'),
        ), name='password_reset'),
    # mensagem apos enviar o email
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    # tela do form para inserir a nova senha
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete'),
        ), name='password_reset_confirm'),
    # mensagem final, apos redefinir a senha
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),


    # Axis
    path('axis/add', my_views.AxisCreate.as_view(), name='axis_create'),
    path('axis/edit/<int:pk>', my_views.AxisUpdate.as_view(), name='axis_update'),
    path('axis/delete/<int:pk>', my_views.AxisDelete.as_view(), name='axis_delete'),

    # Teacher
    path('teacher/add', my_views.TeacherCreate.as_view(), name='teacher_create'),
    path('teacher/edit/<int:pk>', my_views.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/delete/<int:pk>', my_views.TeacherDelete.as_view(), name='teacher_delete'),
]