from django.contrib import admin

from ludomanagerapp.models import Game, Member, GameSession, GameInstance, Borrowing
from django.contrib.auth.admin import UserAdmin

# register your models here.
admin.site.register(Game)
admin.site.register(Member, UserAdmin)
admin.site.register(GameSession)
admin.site.register(GameInstance)
admin.site.register(Borrowing)
