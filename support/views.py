from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .forms import *
from django.views.generic.detail import DetailView

# Create your views here.


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


def ticket_list(request):
    tickets = Ticket.objects.all()
    # paginator = Paginator(tickets, 5)
    # page = request.GET.get('page')
    # try:
    #     ticket = paginator.page(page)
    # except PageNotAnInteger:
    #     ticket = paginator.page(1)
    # except EmptyPage:
    #     ticket = paginator.page(paginator.num_pages)
    # return render(request, 'support/ticket.html', {'page':page, 'ticket':ticket})
    return render(request, 'support/ticket.html', {'tickets': tickets})
#
# def show_one_ticket(request, pk):
#     tickets = Ticket.objects.get(pk=pk)
#     return render(request, 'support/ticket_info.html', {'tickets':tickets})

# def current_ticket(request, ticket, author):
#     ticket = get_object_or_404(Ticket, slug=ticket, author=author)
#     return render(request, 'support/ticket_info.html', {'ticket':ticket})


def TicketFormView(request):
    form = TicketForm(request.POST)
    abc = {'form':form}
    if request.method == 'POST' and form.is_valid():
            data = form.cleaned_data
            form.save()
    return render(request, 'support/index.html', abc)


class TicketDetailView(DetailView, FormMixin):
    model = Ticket
    # template_name = 'support/ticket_info.html'
    form_class = CommentForm
    success_msg = 'Комментарий успешно добавлен'
    success_url = 'http://127.0.0.1:8000/ticket_list/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.ticket_comment = self.get_object()
        self.object.save()
        return super().form_valid(form)


    def show_one_ticket(request, pk):
        tickets = Ticket.objects.get(pk=pk)
        return render(request, 'support/ticket_detail.html', {'tickets':tickets})


# def CommentFormView(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CommentForm(request.POST)
#         comments = Comment.objects.all()
#     return render(request, 'support/ticket_detail.html', {'form':form,
#                                                           'comments':comments})

# def CommentFormView(request):
#     form = CommentForm(request.POST)
#     abc = {'form':form}
#     if request.method == 'POST' and form.is_valid():
#         new_comment = form.save(commit=False)
#         new_comment.
#         form.save()
#     return render(request, 'support/ticket_detail.html')


