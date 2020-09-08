from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, EditForm, ContactForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


# Create your views here.

# shows all post in a index page
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']


# shows a specific post in detailpost.html page
class DetailPost(DetailView):
    model = Post
    template_name = 'detailpost.html'


# add a new post
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'


# update a existing posts
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'updatepost.html'
    form_class = EditForm
    # fields = [
    #     'title', 'title_tag', 'body'
    # ]


# delete a existing posts
@method_decorator(login_required, name='dispatch')  # -> used for only logged in user to access the page
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# contact page template
class ContactPage(FormView, TemplateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    # it returns a admin detail to contact page
    def get_context_data(self, *args, **kwargs):
        admin = User.objects.filter(is_superuser=True)
        context = super(ContactPage, self).get_context_data(*args, **kwargs)
        context['admin'] = admin
        return context

    # valid and sends a users mail to admin
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        name = form.cleaned_data.get('name')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        send_mail(
            subject=subject,
            message=message,
            from_email=email,
            recipient_list=['ramkumarmani2000@gmail.com']
        )

        # success message show on contact page after mail send
        messages.success(self.request, 'name')
        return render(self.request, 'contact.html', {'name': name})
        return super(ContactPage, self).form_valid(form)
