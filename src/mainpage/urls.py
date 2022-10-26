from django.urls import path
from . import views
from .forms import LoginForm
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.mainpage, name="home"),
    path("search/", views.search, name="search"),
    path("profile/", views.profile, name="profile"),
    path("friends/", views.friends, name="friends"),
    path("favorites/", views.favorites, name="favorites"),
    path("meetings/", views.meetings, name="meetings"),
<<<<<<< Updated upstream
    path("login", views.login, name="login")
]
=======
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> Stashed changes
