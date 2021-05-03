## DJANGO CLONE AMAZON RE-RENEWED

### 1. INITIAL COMMIT

#### 1.1.1 Create root directory, .gitignore and README.md files

        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders> mkdir DJANGO-CLONE-AMAZON-RE-RENEWED
        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED> cd .\src\
        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .gitignore README.md
        new file:   .gitignore
        new file:   README.md

#### 1.2.2 Create a new remote repository (github)

        https://github.com/gurnitha/django-clone-amazon-re-renewed
        git remote add origin git@github.com:gurnitha/django-clone-amazon-re-renewed.git
        git branch -M main
        git push -u origin main
        new file:   README.md

#### 1.3.3 Pushing project's files to github

        new file:   README.md

### 2. BASIC SETUP

#### 2.1.4 Install Python

        PASS - I have intalled python 3.9 in my computer
        new file:   README.md

#### 2.2.5 Install Django

        PASS - I have installed django v3.2 in my computer

        # Checking installed django version
        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python
        ...
        >>>
        >>> import django
        >>> django.VERSION
        (3, 2, 0, 'final', 0)
        >>> django.get_version()
        '3.2'
        >>> exit()
        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python -m django --version
        3.2
        new file:   README.md

#### 2.3.6 Create virtual environment

        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python -m venv venv3932
        modified:   .gitignore
        modified:   README.md

#### 2.4.7 Installing Django v3.2

        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\DJANGO-CLONE-AMAZON-RE-RENEWED\src> .\venv3932\scripts\activate
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python -m pip install django==3.2
        ...
        Successfully installed asgiref-3.3.4 django-3.2 pytz-2021.1 sqlparse-0.4.1
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python -m pip install --upgrade pip
        new file:   README.md

### 3. CREATE DJANGO PROJECT AND DJANGO APPS

#### 3.1.8 Create django project called 'config' inside src folder

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> django-admin startproject config .
        new file:   README.md

#### 3.2.9 Create django app called 'main' inside 'app' folder

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> mkdir app/main
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py startapp main app/main
        new file:   README.md

#### 3.3.10 Create django app called 'backend' inside 'app' folder

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> mkdir app/backend
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py startapp backend app/backend
        new file:   README.md

#### 3.4.11 Install main and backend apps to project root, checking and testing

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py check
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py runserver
        ..
        Starting development server at http://127.0.0.1:8000/

        modified:   app/backend/apps.py
        modified:   app/main/apps.py
        modified:   config/settings.py
        new file:   db.sqlite3

### 4. DATABASE - USING MYSQL FOR THE DATABASE

#### 4.1.12 Create database

        PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders> mysql -u root
        mysql>
        mysql> CREATE DATABASE django_clone_amazon_re_renewed;
        Query OK, 1 row affected (0.07 sec)
        new file:   README.md

#### 4.2.13 Connecting the project with the database

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python -m pip install mysqlclient
        ..
        Successfully installed mysqlclient-2.0.3
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': 'this_dbname_modified',
                        'USER': 'root',
                        'PASSWORD': '',
                        'HOST': 'localhost',
                        'PORT': 3306
                }
        }
        NOTE:
        Remember the db creadentials sequance (NAME, USER, PASSWORD, HOST, PORT)
        modified:   README.md
        modified:   config/settings.py

### 5. LOGIN AND LOGOUT USING DEFAULT USER MODEL

#### 5.1.14 Create models/tables

        # Use db and check tables
        mysql> USE django_clone_amazon_re_renewed;
        Database changed
        mysql> SHOW TABLES;

        # Run migration to create tables
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py makemigrations
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py migrate

        # Check tables: 10 new tables created
        mysql> SHOW TABLES;
        +------------------------------------------+
        | Tables_in_django_clone_amazon_re_renewed |
        +------------------------------------------+
        | auth_group                               |
        | auth_group_permissions                   |
        | auth_permission                          |
        | auth_user                                |
        | auth_user_groups                         |
        | auth_user_user_permissions               |
        | django_admin_log                         |
        | django_content_type                      |
        | django_migrations                        |
        | django_session                           |
        +------------------------------------------+
        10 rows in set (0.00 sec)

        modified:   README.md

#### 5.2.15 Create superuser

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py createsuperuser
        Username (leave blank to use '62812'): admin
        Email address: ingafter60@admin.com
        Password:
        Password (again):
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        modified:   README.md

#### 5.3.16 Checking the newly created superuser in db auth_user table

        mysql> DESC auth_user;
        +--------------+--------------+------+-----+---------+----------------+
        | Field        | Type         | Null | Key | Default | Extra          |
        +--------------+--------------+------+-----+---------+----------------+
        | id           | int(11)      | NO   | PRI | NULL    | auto_increment |
        | password     | varchar(128) | NO   |     | NULL    |                |
        | last_login   | datetime(6)  | YES  |     | NULL    |                |
        | is_superuser | tinyint(1)   | NO   |     | NULL    |                |
        | username     | varchar(150) | NO   | UNI | NULL    |                |
        | first_name   | varchar(150) | NO   |     | NULL    |                |
        | last_name    | varchar(150) | NO   |     | NULL    |                |
        | email        | varchar(254) | NO   |     | NULL    |                |
        | is_staff     | tinyint(1)   | NO   |     | NULL    |                |
        | is_active    | tinyint(1)   | NO   |     | NULL    |                |
        | date_joined  | datetime(6)  | NO   |     | NULL    |                |
        +--------------+--------------+------+-----+---------+----------------+
        11 rows in set (0.05 sec)

        mysql> SELECT username, email FROM auth_user;
        +----------+------------------------+
        | username | email                  |
        +----------+------------------------+
        | admin    | ingafter60@admin.com   |
        +----------+------------------------+
        1 row in set (0.00 sec)
        modified:   README.md

#### 5.4.17 Run the server, login and logout

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> python manage.py createsuperuser
        # Login and logout using the deafult User model DONE:)
        modified:   README.md

### 6. CREATING HOME PAGE FRONTEND

#### 6.1.18 Create Home and About pages with views, templates and url path

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> mkdir templates/main
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src>  touch templates/main/front-home.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src>  touch templates/main/front-about.html
        modified:   README.md
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/main/front-about.html
        new file:   templates/main/front-home.html

#### 6.2.19 Linking the Home and About pages

        modified:   README.md
        modified:   templates/main/front-about.html
        modified:   templates/main/front-home.html

#### 6.3.20 Modify the pages using template in heritance

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> mkdir .\templates\main\shared
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .\templates\main\shared\front-navbar.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .\templates\front-base.html
        modified:   README.md
        new file:   templates/front-base.html
        modified:   templates/main/front-about.html
        modified:   templates/main/front-home.html
        new file:   templates/main/shared/front-navbar.html

#### 6.4.21 Making page haed title dynamic

        modified:   README.md
        modified:   templates/front-base.html
        modified:   templates/main/front-about.html
        modified:   templates/main/front-home.html

#### 6.5.22 Styling - Adding simple style Home and About pages

        modified:   README.md
        modified:   templates/front-base.html
        modified:   templates/main/front-about.html
        modified:   templates/main/front-home.html

### 7. BACKEND - CREATING HOME AND LOGIN PAGES

#### 7.1.23 Create Home and Login pages with views, templates and url path

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> mkdir .\templates\backend
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .\templates\backend\admin-login.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .\templates\backend\admin-home.html
        modified:   README.md
        modified:   app/backend/views.py
        modified:   config/urls.py
        new file:   templates/backend/admin-home.html
        new file:   templates/backend/admin-login.html

#### 7.2.24 Linking the frontend and backend pages

        modified:   README.md
        modified:   templates/main/shared/front-navbar.html

#### 7.3.25 Modify the pages using template in heritance

        (venv3932) ...\DJANGO-CLONE-AMAZON-RE-RENEWED\src> touch .\templates\admin-base.html
        modified:   README.md
        new file:   templates/admin-base.html
        modified:   templates/backend/admin-home.html
        modified:   templates/backend/admin-login.html

#### 7.4.26 Making page haed title dynamic

        modified:   README.md
        modified:   templates/admin-base.html
        modified:   templates/backend/admin-home.html
        modified:   templates/backend/admin-login.html

#### 7.5.27 Styling - Adding simple style Home and About pages

        modified:   README.md
        modified:   templates/admin-base.html
        modified:   templates/backend/admin-home.html
        modified:   templates/backend/admin-login.html

### 8. CUSTOMUSER - LOGIN AND LOGOUT USING CUSTOMUSER MODEL

#### 8.1.28 Creating CustomUser model

        # Steps (2)
        1. Delete the existing database
        mysql> DROP DATABASE  django_clone_amazon_re_renewed;
        2. Create a new database (can be the same name as it was)
        mysql> CREATE  DATABASE  django_clone_amazon_re_renewed;
        mysql> USE  django_clone_amazon_re_renewed;

        modified:   README.md
        modified:   templates/admin-base.html
        modified:   templates/backend/admin-home.html
        modified:   templates/backend/admin-login.html
