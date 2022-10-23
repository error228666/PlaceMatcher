WHAT THIS SITE IS USEFUL FOR?
This site helps you find places to go alone/with friends and schedule meetings with friends.

HOW TO INSTALL?
1) Clone this repository. make sure you installed everything from requirements.txt
2) Start app with "python manage.py startapp" command. You need to be in placematcher directory for that.
3) Start local server with "python manage.py runserver" command.
4) Open the suggested link in your browser. Usually it is http://127.0.0.1:8000/

CURRENT VERSION:
We switched from making android app to making website on django. This version is based on sqlite3 database, you can see main page here and top navigation bar with all planned folders (search, friends, meetings, favorites, profile). Right now all buttons link to placeholders, except for profile. If you logged in, it shows you "Hi, username!" and if not, it shows "You are not logged in."
Top navigation bar contains login and sign up buttons, if you are not logged in, and logout button, if you are.
All forms are working, so you can login/sign up to check all options.

PLANS:
We are planning to add fully-working search, update profile (add about-me, last and first name, etc), add friends list and option to add a friends. Also we'll update favorite page and add option to schedule a meeting.

Authors:
Valeria Rubanova made login, logout, sign up, Ivan Eroshkin and I made the main page and navigation bar. Ivan is currently working on search page.