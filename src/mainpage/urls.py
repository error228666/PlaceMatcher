from django.urls import path, include
from . import views
from .forms import LoginForm
from .views import CustomLoginView, send_request, accept_request, delete_friend, reject_request, schedule_meeting, \
    planned_meetings, accept_meeting_request, reject_meeting_request, cancel_meeting, PersonView
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
    path('planned-meetings', planned_meetings, name='planned-meetings'),
    path('schedule-meeting/', views.schedule_meeting.as_view(template_name='mainpage/schedule_meeting.html'), name='schedule-meeting'),
    path('accept-meeting-request/<int:id>/', accept_meeting_request, name='accept-meeting-request'),
    path('reject-meeting-request/<int:id>/', reject_meeting_request, name='reject-meeting-request'),
    path('cancel-meeting/<int:id>/', cancel_meeting, name='cancel-meeting'),
    path('profile/<int:personid>', PersonView, name="person"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
