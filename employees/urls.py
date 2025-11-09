from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),

    # Employee Import/Export
    path('employees/import/', views.import_excel, name='import_excel'),
    path('employees/export/', views.export_excel, name='export_excel'),

    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),

    # Task Import/Export
    path('tasks/import/', views.import_tasks_excel, name='import_tasks_excel'),
    path('tasks/export/', views.export_tasks_excel, name='export_tasks_excel'),
]
