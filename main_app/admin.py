from django.contrib import admin
from .models import Team, Player, Stat, Training

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stat)
admin.site.register(Training)
