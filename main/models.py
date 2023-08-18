from django.db import models
from ckeditor.fields import RichTextField


class HomeImg(models.Model):
    first_img = models.ImageField(upload_to="home/img/")
    second_img = models.ImageField(upload_to="home/img/")
    third = models.ImageField(upload_to="home/img/")
    word = models.CharField(max_length=255)


class Player(models.Model):
    photo = models.ImageField(upload_to="player/")
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    player_number = models.IntegerField()
    matches_played = models.IntegerField(default=0)
    goals = models.IntegerField()
    minutes_played = models.IntegerField()
    started = models.IntegerField()
    sub_off = models.IntegerField()
    role = models.IntegerField(choices=((1, "Darvozabon"),
                                        (2, "Himoya"),
                                        (3, "Markaz"),
                                        (4, "Hujumchi"))
                               )


class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    cover_image = models.ImageField(upload_to="blog/")
    publish_date = models.DateField(auto_now=True)
    is_tournament = models.BooleanField(default=False)


class Statistic(models.Model):
    logo = models.ImageField(upload_to="table/")
    team = models.CharField(max_length=255)
    o = models.IntegerField()
    g = models.IntegerField()
    d = models.IntegerField()
    m = models.IntegerField()
    t_f = models.CharField(max_length=255)


class Sponsor(models.Model):
    logo = models.ImageField(upload_to="sponsors/")


class BoburArena(models.Model):
    history = models.TextField()
    body = RichTextField()


class Rahbariyat(models.Model):
    photo = models.ImageField(upload_to="rahbariyat/")
    name_or_title = models.CharField(max_length=255)
    text = models.TextField()
    is_coach = models.BooleanField(default=True)


class Club(models.Model):
    body = RichTextField()


class Advice(models.Model):
    advices_img = models.ImageField(upload_to='advices/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateField()


