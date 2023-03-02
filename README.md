# inventory-management-system

## Tech


| Technology        | Version       |
| -------------     |:-------------:| 
| Python            | 3.9.6         | 
| Django            | 4.1.7         |
| mysql             | 8.0.32        |


### Installation

This project requires Python3 to run. If you have a Linux machine, dont worry your good to go. If not, please refer https://www.python.org/downloads/

Create a virtual env
```sh
➜  inventory-management-system git:(main) ✗ python3 -m venv env
➜  inventory-management-system git:(main) ✗ ls
README.md        env              ims              requirements.txt
➜  inventory-management-system git:(main) ✗
```
You will notice an env folder has been created.

Now we need to activate our virtual environment using following:
```sh
➜  inventory-management-system git:(main) ✗ source env/bin/activate
```

Note: In case you need to deactivate the virtual environment or no longer need it just run `deactivate` like this:
```
(env) ➜  inventory-management-system git:(main) ✗ deactivate
```

We notice `(env)` in the path name of our terminal. Now we have successfully activated our virtual environment. Lets install the required packages via `requirements.txt` file
```sh
(env) ➜  ims git:(main) ✗ pip install -r requirements.txt
Requirement already satisfied: appnope==0.1.3 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (0.1.3)
Requirement already satisfied: asgiref==3.6.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.6.0)
Requirement already satisfied: asttokens==2.2.1 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2.2.1)
Requirement already satisfied: backcall==0.2.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (0.2.0)
Requirement already satisfied: decorator==5.1.1 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 5)) (5.1.1)
Requirement already satisfied: Django==4.1.7 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 6)) (4.1.7)
Requirement already satisfied: django-environ==0.9.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (0.9.0)
Requirement already satisfied: django-filter==22.1 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 8)) (22.1)
Requirement already satisfied: executing==1.2.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 9)) (1.2.0)
Requirement already satisfied: ipython==8.10.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 10)) (8.10.0)
Requirement already satisfied: jedi==0.18.2 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 11)) (0.18.2)
Requirement already satisfied: matplotlib-inline==0.1.6 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 12)) (0.1.6)
Requirement already satisfied: mysqlclient==2.1.1 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 13)) (2.1.1)
Requirement already satisfied: parso==0.8.3 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 14)) (0.8.3)
Requirement already satisfied: pexpect==4.8.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 15)) (4.8.0)
Requirement already satisfied: pickleshare==0.7.5 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 16)) (0.7.5)
Requirement already satisfied: prompt-toolkit==3.0.37 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 17)) (3.0.37)
Requirement already satisfied: ptyprocess==0.7.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 18)) (0.7.0)
Requirement already satisfied: pure-eval==0.2.2 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 19)) (0.2.2)
Requirement already satisfied: Pygments==2.14.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 20)) (2.14.0)
Requirement already satisfied: six==1.16.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 21)) (1.16.0)
Requirement already satisfied: sqlparse==0.4.3 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 22)) (0.4.3)
Requirement already satisfied: stack-data==0.6.2 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 23)) (0.6.2)
Requirement already satisfied: traitlets==5.9.0 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 24)) (5.9.0)
Requirement already satisfied: wcwidth==0.2.6 in /Users/sachinharpalani/Projects/inventory-management-system/env/lib/python3.9/site-packages (from -r requirements.txt (line 25)) (0.2.6)
WARNING: You are using pip version 21.2.4; however, version 23.0.1 is available.
You should consider upgrading via the '/Users/sachinharpalani/Projects/inventory-management-system/env/bin/python3 -m pip install --upgrade pip' command.
(env) ➜  ims git:(main) ✗ pip list
Package           Version
----------------- -------
appnope           0.1.3
asgiref           3.6.0
asttokens         2.2.1
backcall          0.2.0
decorator         5.1.1
Django            4.1.7
django-environ    0.9.0
django-filter     22.1
executing         1.2.0
ipython           8.10.0
jedi              0.18.2
matplotlib-inline 0.1.6
mysqlclient       2.1.1
parso             0.8.3
pexpect           4.8.0
pickleshare       0.7.5
pip               21.2.4
prompt-toolkit    3.0.37
ptyprocess        0.7.0
pure-eval         0.2.2
Pygments          2.14.0
setuptools        58.0.4
six               1.16.0
sqlparse          0.4.3
stack-data        0.6.2
traitlets         5.9.0
wcwidth           0.2.6
WARNING: You are using pip version 21.2.4; however, version 23.0.1 is available.
You should consider upgrading via the '/Users/sachinharpalani/Projects/inventory-management-system/env/bin/python3 -m pip install --upgrade pip' command.
```


Now we need to configure out DB settings. Create a file '.env' in ims directory. This file has to be kept in same directory as settings.py file

```sh
(env) ➜  ims git:(main) ✗ ll
total 32
-rw-r--r--  1 sachinharpalani  staff     0B Feb 27 15:26 __init__.py
-rw-r--r--  1 sachinharpalani  staff   383B Feb 27 15:26 asgi.py
-rw-r--r--  1 sachinharpalani  staff   3.6K Mar  2 14:12 settings.py
-rw-r--r--  1 sachinharpalani  staff   1.0K Mar  1 22:33 urls.py
-rw-r--r--  1 sachinharpalani  staff   383B Feb 27 15:26 wsgi.py
```

Now replace the following parameters with your db cofiguration and save it.

```sh
DB_NAME=<db_name>
DB_USER=<db_user>
DB_HOST=<db_host>
DB_PASSWORD=<db_password>
DB_PORT=<db_port>
```

NOTE: You dont need to use ' or " in strings here.


Now we need to migrate our Database and runserver. Follow these steps:
```sh
(env) ➜  ims git:(main) ✗ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying core.0001_initial... OK
  Applying sessions.0001_initial... OK
(env) ➜  ims git:(main) ✗ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 02, 2023 - 08:49:38
Django version 4.1.7, using settings 'ims.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you see `Starting development server at http://127.0.0.1:8000/` this means our server is now hosted on localhost at port 8000. Now we can go to `localhost:8000` and browse the webapp.

You will also need a user to be created to access the project first time.
You can create a superuser as follows:

```sh
(env) ➜  ims git:(main) ✗ python3 manage.py createsuperuser
Username (leave blank to use 'sachinharpalani'):
Email address:
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

You can use this superuser to login and create more users as well.