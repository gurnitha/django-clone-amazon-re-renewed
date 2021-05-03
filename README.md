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
