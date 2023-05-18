from ast import mod
from pickle import TRUE
from tkinter import CASCADE
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=150, null=True)
    password = models.TextField(max_length=50, null=True)
    types = models.CharField(max_length=100, null=True)
    status = models.TextField(max_length=50, default='0', null=True)


class Association(models.Model):
    logid = models.ForeignKey(
        Login, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, null=True)
    addr = models.CharField(max_length=150, null=True)
    assochead = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phno = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, default='0', null=True)


class Photographer(models.Model):
    logid = models.ForeignKey(
        Login, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, null=True)
    addr = models.CharField(max_length=150, null=True)
    gender = models.CharField(max_length=150, null=True)
    district = models.CharField(max_length=150, null=True)
    specialization = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, null=True)
    association1 = models.CharField(max_length=150, null=True)
    profile = models.ImageField(upload_to='Profile', null=True)
    insta = models.URLField(null=True)
    fb = models.URLField(null=True)


class Customer(models.Model):
    logid = models.ForeignKey(
        Login, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, null=True)
    addr = models.CharField(max_length=150, null=True)
    gender = models.CharField(max_length=150, null=True)
    district = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)


class Packages(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    package = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=150, null=True)


class Booking(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    pkgid = models.ForeignKey(
        Packages, on_delete=models.CASCADE, blank=True, null=True)
    bookingdate = models.CharField(max_length=150, null=True)
    fromdate = models.CharField(max_length=150, null=True)
    todate = models.CharField(max_length=150, null=True)
    days = models.CharField(max_length=150, null=True)
    location = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)
    cid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    tamount = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, null=True)


class Artgallery(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=150, null=True)


class Award(models.Model):
    assocname = models.CharField(max_length=150, null=True)
    award = models.CharField(max_length=150, null=True)
    pname = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=150, null=True)
    date = models.CharField(max_length=150, null=True)


class Complaint(models.Model):
    cid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    cname = models.CharField(max_length=150, null=True)
    cdesc = models.CharField(max_length=150, null=True)
    date = models.CharField(max_length=150, null=True)
    type = models.CharField(max_length=150, null=True)


class District(models.Model):
    district = models.CharField(max_length=150, null=True)


class Feedback(models.Model):
    cid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    feedback = models.CharField(max_length=150, null=True)
    rating = models.CharField(max_length=150, null=True)
    phid = models.CharField(max_length=150, null=True)


class Giftgallery(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=150, null=True)


class Notification(models.Model):
    assocname = models.CharField(max_length=150, null=True)
    event = models.CharField(max_length=150, null=True)
    date = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=150, null=True)
    loc = models.CharField(max_length=150, null=True)


class Payment(models.Model):
    custid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.CharField(max_length=150, null=True)


class purchased(models.Model):
    pmid = models.ForeignKey(
        Payment, on_delete=models.CASCADE, blank=True, null=True)
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    artid = models.ForeignKey(
        Artgallery, on_delete=models.CASCADE, blank=True, null=True)
    saleid = models.ForeignKey(
        Giftgallery, on_delete=models.CASCADE, blank=True, null=True)


class Photographerimage(models.Model):
    caption = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=150, null=True)
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)


class Photographervideo(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=150, null=True)


class Place(models.Model):
    did = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True)
    loc = models.CharField(max_length=150, null=True)


class Specification(models.Model):
    camera = models.CharField(max_length=150, null=True)
    cmodel = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=150, null=True)
    image = models.CharField(max_length=150, null=True)
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)


class Workstatus(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    bkid = models.ForeignKey(
        Booking, on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=150, null=True)
    date = models.CharField(max_length=150, null=True)


class review(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    cid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.FloatField(default=0)
    feedback = models.CharField(max_length=150, null=True)


class ForAlbum(models.Model):
    phid = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, blank=True, null=True)
    cid = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=150, null=True)


class AlbumImages(models.Model):
    fa = models.ForeignKey(ForAlbum, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='album')


# Create your models here.
