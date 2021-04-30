from tasks.api.views import (
                api_task_view,
                api_task_delete_view,
                api_task_upadate_view,
                api_task_create_view,
                api_tasks_moderator_view,
                api_tasks_customer_view
                )

from django.urls import path


app_name = "tasks"


urlpatterns = [
    path("",api_task_view,name = "tasks"),
    path("delete/<int:id>",api_task_delete_view,name="delete"),
    path('update/<int:id>',api_task_upadate_view,name="update"),
    path('create/<str:name_mod>',api_task_create_view,name="createTask"),
    path('view_assignments',api_tasks_moderator_view,name="mod_task_view"),
    path('view_given_tasks',api_tasks_customer_view,name="customer_task_view")
]