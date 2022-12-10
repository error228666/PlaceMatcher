from django.urls import path, include
from . import views
from .forms import LoginForm
from .views import CustomLoginView, send_request, accept_request, delete_friend, reject_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.mainpage, name="home"),
    path("search/", include("search.urls")),
    path("profile/", views.profile, name="profile"),
    path("friends/", views.friends, name="friends"),
    path("favorites/", views.favorites, name="favorites"),
    path("meetings/", views.meetings, name="meetings"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('add-friend/<int:id>/', send_request,name='add-friend'),
    path('accept/<int:id>/', accept_request, name='accept'),
    path('delete-friend/<int:id>/', delete_friend, name='delete-friend'),
    path('reject/<int:id>/', reject_request, name='reject'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
