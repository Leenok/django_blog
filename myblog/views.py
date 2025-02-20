from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError

from .models import Post
from .forms import SignUpForm, SignInForm, FeedBackForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse

class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/index.html', context={
            # 'posts': posts
            'page_obj': page_obj
        })
    
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/about.html'
        )
    
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/contact.html'
        )
    
class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'myblog/post_detail.html', context={
            'post': post
    })

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })
    
class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={
            'form':form
        })
    
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error(None, "Неправильный пароль или указанная учётная запись не существует!")
                return render(request, 'myblog/signin.html', {"form": form})
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })


def logout_view(request):
    logout(request)
    return redirect('index')


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'myblog/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'ОТ {name} | {subject}', message, from_email, ['L-incanto@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'myblog/contact.html',context={
            'form': form
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/success.html', context={
            'title': 'Спасибо'
        })