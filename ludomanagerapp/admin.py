from django.contrib import admin

from ludomanagerapp.models import Game, Member, GameSession, GameInstance, Borrowing
# register your models here.
admin.site.register(Game)
admin.site.register(Member)
admin.site.register(GameSession)
admin.site.register(GameInstance)
admin.site.register(Borrowing)
