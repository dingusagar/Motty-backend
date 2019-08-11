from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the Topic")
    image = models.ImageField(upload_to='topic_image/', null=True)

    def __str__(self):
        return str(self.name)


class Celebrity(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the Celebrity")
    image = models.ImageField(upload_to='celebrity_image/', null=True)

    def __str__(self):
        return str(self.name)

