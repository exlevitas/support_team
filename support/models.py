from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.shortcuts import reverse


class Ticket(models.Model):
    TICKET_STATUS = (
        ('Under Consideration', 'Under Consideration'),
        ('Reviewed', 'Reviewed'),
        ('Freezed', 'Freezed')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=TICKET_STATUS, default='Under Consideration')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('support:show_one_ticket', kwargs={'id':self.id})
        return f'/ticket/{self.pk}/'
        # return f'/ticket/{self.id}/'


class Comment(models.Model):
    ticket_comment = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    name_comment = models.CharField(max_length=50)
    position_comment = models.CharField(max_length=50)
    text_comment = models.TextField(max_length=250, blank=True)
    created_comment = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_comment']

    def __str__(self):
        return self.text_comment
