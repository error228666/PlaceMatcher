## Placematcher: _This site helps you find places to go alone/with friends and schedule meetings with them._

## Current version

- Main page here and top navigation bar with all planned folders (search, friends, meetings, favorites, profile). It has personalized logo for out website.
- You can edit your profile information, log in into account, log out of it, create new one.
- Top navigation bar contains login and sign up buttons, if you are not logged in, and logout button, if you are.
- You can add friends, accept/reject friend requests and delete user from your friend list.
- Meeting tab has button for scheduling a meeting or seeng planned ones, but they are not quiet working yet.
- You can search places, choose categories to search in and see closest metro station!

## Installation

```sh
1) Clone this repository. Make sure you installed everything from requirements.txt
2) Run "python  manage.py import_data Places" command to import database.
3) Start local server with "python manage.py runserver" command.
4) Open the suggested link in your browser. Usually it is http://127.0.0.1:8000/
```

## Plans

- Make a good-looking place tab for each place and final search version.
- Make working favorite tab.
- Make buttons on meeting tab work: create Meeting, MeetingRequest models and add needed views and forms.

## Authors:
- Valeria Rubanova: profile, login, logout, signup forms, friends, top navigation bar.
- Ivan Eroshkin: search, top navigation bar.


