from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from core.models import Places, Category


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    friends = models.ManyToManyField("Profile", blank=True)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profile, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name="to_user", on_delete=models.CASCADE)


class Meeting(models.Model):
    from_user_m = models.ForeignKey(Profile, related_name="from_user_m", on_delete=models.CASCADE)
    to_user_m = models.ForeignKey(Profile, related_name="to_user_m", on_delete=models.CASCADE)
    place_m = models.ForeignKey(Places, related_name="place_m", on_delete=models.CASCADE)
    date_m = models.DateField(default='')
    time_m = models.TimeField(default='', max_length=10)

    def __str__(self):
        return f"Время: {self.date_m} {self.time_m }\n Место:{self.place_m}"


class MeetingRequest(models.Model):
    from_user_mr = models.ForeignKey(Profile, related_name="from_user_mr", on_delete=models.CASCADE)
    to_user_mr = models.ForeignKey(Profile, related_name="to_user_mr", on_delete=models.CASCADE)
    place = models.ForeignKey(Places, related_name="places", on_delete=models.CASCADE)
    date = models.DateField(default='')
    time = models.TimeField(default='', max_length=10)



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainpageProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    bio = models.TextField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    avatar = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mainpage_profile'


class Meetings(models.Model):
    id1 = models.IntegerField()
    id2 = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings'


<<<<<<< Updated upstream
=======
# class Places(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     type = models.CharField(max_length=270, blank=True, null=True)
#     adress = models.CharField(max_length=180, blank=True, null=True)
#     site = models.CharField(max_length=270, blank=True, null=True)
#     vk = models.CharField(max_length=45, blank=True, null=True)
#     average_rating = models.FloatField(blank=True, null=True)
#     min_count_of_people = models.IntegerField(blank=True, null=True)
#     max_count_of_people = models.IntegerField(blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     other_info = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'places'



>>>>>>> Stashed changes
class Reviews(models.Model):
    place_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Users(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'
