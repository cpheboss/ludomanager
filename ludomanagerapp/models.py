from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    minimum_players = models.IntegerField()
    maximum_players = models.IntegerField()

    def __str__(self):
        return self.name

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GameSession(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class GameInstance(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    players = models.ManyToManyField(Member, null=True, blank=True)
    game_session = models.ForeignKey(GameSession, on_delete=models.PROTECT)

    def __str__(self):
        return self.game.name + '(' + str(self.players.count()) + ')'

class Borrowing(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    date_out = models.DateField()
    expected_date_in = models.DateField()
    date_in = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.game) + ' by ' + str(self.member)
