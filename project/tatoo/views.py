from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Work
from .forms import CreatePostForm, UpdatePostForm


error_message = '''<p>Поздравляю, ты только что нашел баг на сайте! Напиши 
                об этом на мою электронную почту hello@kkomissarov.ru  и опиши ситуацию, при 
                которой это случилось.</p> '''






class MainPageView(View):

    def get(self, request):
        post_form = CreatePostForm()
        update_form = UpdatePostForm()

        context = {
            'works': Work.objects.all().filter(type='w').order_by('-date'),
            'sketches': Work.objects.all().filter(type='s'),
            'post_form': post_form,
            'update_form': update_form
        }
        return render(request, 'tatoo/mainpage.html', context)


class Login(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'tatoo/login.html', {'form': form})


    def post(self, request):

        form = AuthenticationForm(data=request.POST)


        if form.is_valid():
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            login(request, user)
            return redirect('main_view')

        else:
            return render(request, 'tatoo/login.html', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('main_view')




class CreatePost(View):

    def get(self, request):
        return redirect('main_view')


    def post(self, request):

        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_staff:
            new_post = form.save()
            return redirect('main_view')

        else:
            return HttpResponse(error_message)


class UpdatePost(View):

    def get(self, request):
        redirect('main_view')


    def post(self, request):

        current_post = Work.objects.get(id=request.POST.get('post_id'))
        form = UpdatePostForm(request.POST, request.FILES, instance=current_post)

        if form.is_valid() and request.user.is_staff:
            update_post = form.save()
            return redirect('main_view')

        else:
            return HttpResponse(error_message)



class DeletePost(View):
    def get(self, request):
        try:
            if request.user.is_staff:
                post = Work.objects.get(id=request.GET.get('post_id'))
                post.delete()
                return redirect('main_view')
            else:
                return HttpResponse(error_message)

        except:
            return HttpResponse(error_message)











