<<<<<<< Updated upstream
from django.shortcuts import render
from django.http import HttpResponse
=======
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

>>>>>>> Stashed changes


def mainpage(request):
    return render(request, "mainpage/mainpage.html")


def friends(request):
    return render(request, "mainpage/friends.html")


def search(request):
    return render(request, "mainpage/search.html")


def favorites(request):
    return render(request, "mainpage/favorites.html")


def meetings(request):
    return render(request, "mainpage/meetings.html")


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'mainpage/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class SignUp(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='search')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

<<<<<<< Updated upstream

def login(request):
    return render(request, "mainpage/login.html")
=======
        if not remember_me:
            self.request.session.set_expiry(0)
>>>>>>> Stashed changes

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)