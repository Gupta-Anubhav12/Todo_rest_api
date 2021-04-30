# TODO tasks assignment and notification APi in Django Rest Framework

This is a simple api made for electura intern assignment phase submissions, 
It works using basic authentication and has two types of roles , being moderators and consumers,

## Installation and setup

```
pip install -r requirements.txt

python manage.py runserver
```

## Moderators can create a profile using

http://anubhavgupta.pythonanywhere.com/api/profiles/register_mod

example Json data to be sent
```
{"contact_number":"7889187788",
"user":{"username":"anubhav","password":7865151addasadsAS@Q#","email":"anubhavgupta2260@gmail.com"},
"tasks_completed":"25",
"efficiency":"25"
}
```
## Consumers can create a profile using
http://anubhavgupta.pythonanywhere.com/api/profiles/register_consumer
```
{"contact_number":"7889187788",
"user":{"username":"consumer","password":"7865151addasadsAS@Q#","email":"anubhavgupta2261@gmail.com"},
"tasks_given":"25"
}
```

Now there are endpoints for viewing the users and details of consumers and moderators

- http://anubhavgupta.pythonanywhere.com/api/profiles/view-all-mods
- http://anubhavgupta.pythonanywhere.com/api/profiles/view-all-consumer
- http://anubhavgupta.pythonanywhere.com/api/profiles/view-one-mods/<str:name>
- http://anubhavgupta.pythonanywhere.com/api/profiles/view-all-consumer/view-one-consumer/<str:name>
  

  all these links have suitable authentications that can be changed , and are well commented in the code for better review

 ## now tasks are created by following

- http://anubhavgupta.pythonanywhere.com/api/tasks/create/(name of modetator here)
   this way a particular moderator can be assigned tasks and both user and mod are notified via email that can be added with html templated context for UI

```
{
    "title":"Make an APi",
    "description":"try getting intern at ELECTURA",
    "deadline":"2021-05-01"
}
```

## Tasks can be upadated by a moderator level perm account after authentication on 
- http://anubhavgupta.pythonanywhere.com/api/tasks/update/(id of task)

this set's the no of tasks completed by a mod and no his/her efficiency is updated as tasks on deadline vs total tasks 
commented in code for better readibility

## mods can see tasks assigned at
- http://anubhavgupta.pythonanywhere.com/api/tasks/view_assignments
  
## clients can see tasks made at

- http://anubhavgupta.pythonanywhere.com/api/tasks/view_given_tasks

## Notes
there are some other end points in api for which you can refer the code , everything is written with apt comments and apt writing style following snakecase in most of the repo

Due to lack of time and college load , I left making .env file as all credentials are single use ~ it ain't an unknown error,
I could have written more apt docs and ER diagram is missing due to same reason because we've got end sems starting this week on 5th may 😕

Overall I think This api fulfills most of the assignment requirements 

superuser :
electura
25654
@ /admin
Thanks 
