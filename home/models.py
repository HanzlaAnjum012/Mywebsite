from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=100)
    profile_image_link = models.CharField(max_length=800,null=False)
    logo_link = models.CharField(max_length=200, default="")
    shortuct_icon_link = models.CharField(max_length=200, default="")
    bio_data = models.TextField(default="")
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=100,null=False)
    link = models.CharField(max_length=200,null=False)
    color_code = models.CharField(max_length=40, null=False, default="")
    shadow_color_code = models.CharField(max_length=100, null=False, default="")
    favicon = models.CharField(max_length=500, null=False, default="")
    text_color_code = models.CharField(max_length=50, null=False, default="#ffffff")
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "'s link"

class Contact(models.Model):
    name = models.CharField(max_length=99,null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    message = models.TextField()

    def __str__(self):
        return self.name + "contacted you."

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, default="")
    description = models.CharField(max_length=500, null=False, default="")
    image_link = models.CharField(max_length=300, null=False, default="")
    project_link = models.CharField(max_length=1000, null=False, default="")
    preview = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name