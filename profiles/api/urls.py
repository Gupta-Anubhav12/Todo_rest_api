from django.urls import path,include
# Create your views here.


from .views import (api_register_moderator_view,
                    api_all_moderator_view,
                    api_one_moderator_view,
                    api_all_consumer_view,
                    api_register_consumer_view,
                    api_one_consumer_view,
                    )   
app_name = "profiles"

urlpatterns = [
    # path("login",)
    path('register_mod',api_register_moderator_view,name="register_moderator"),
    path('register_consumer',api_register_consumer_view,name="register_moderator"),
    path('view-all-mods',api_all_moderator_view,name="view-all-mods"),
    path('view-all-consumer',api_all_consumer_view,name="view-all-mods"),
    path('view-one-mods/<str:name>',api_one_moderator_view,name="view-one-mods"),
    path('view-one-consumer/<str:name>',api_one_consumer_view,name="view-one-mods"),
]