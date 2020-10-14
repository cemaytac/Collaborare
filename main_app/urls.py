from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team_index, name='team_index'),
    path('team/create', views.TeamCreate.as_view(), name='team_create'),
    path('team/players/', views.players_index, name='index'),
    path('team/players/<int:player_id>/', views.players_detail, name='detail'),
    path('team/players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('team/players/<int:pk>/update/',
         views.PlayerUpdate.as_view(), name='players_update'),
    path('team/players/<int:pk>/delete/',
         views.PlayerDelete.as_view(), name='players_delete'),
    path('team/players/<int:player_id>/add_stats',
         views.add_stats, name='add_stats'),
    # path('players/<int:player_id>/delete_stats/',
    #      views.delete_stats, name='delete_stats'),
    path('training/', views.TrainingList.as_view(), name='training_index'),
    path('training/<int:pk>/', views.TrainingDetail.as_view(),
         name='training_detail'),
    path('training/create/', views.TrainingCreate.as_view(),
         name='training_create'),
    path('training/<int:pk>/update/',
         views.TrainingUpdate.as_view(), name='training_update'),
    path('training/<int:pk>/delete/',
         views.TrainingDelete.as_view(), name='training_delete'),
    path('team/players/<int:player_id>/assoc_training/<int:training_id>/',
         views.assoc_training, name='assoc_training'),
    path('accounts/signup/', views.signup, name='signup'),
]
