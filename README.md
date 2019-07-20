# Flask_Bootcamp




python virtual environment
&nbsp; python -m virtualenv venv\
&nbsp; . venv/bin/activate\
&nbsp; pip install -r requirement.txt
\
\
\
flask basics\
-. basic routes, dynamic route\
-. debug mode, debug console\
templates\
-. template basics\
-. template variables\
-. template control flow (for, if, ..)\
-. template inheritance & filters {{variable | filter}}\
-. url link with template (url_for)\
-. form example & page not found 404\
-. exercise 1: test if a username provided meets 3 requirement, if not, provide which not met (e1 in basic.py and templates)\
forms\
-. form\
-. form field\
-. form alert (flash)\
-. form alert2: exercise\
SQL Databases with Flask: flask_database.py\
-. python and database: ORM, Flask-SQLAlchemy, \
&nbsp;  pip install Flask-SQLAlchemy\
&nbsp;  CRUD (create, read, update, delete) database\
-. flask migrate\
&nbsp;  pip install Flask-Migrate\
&nbsp;  export FLASK_APP=flask_database.py\
&nbsp;  flask db init\
&nbsp;  if you already have migrated for another database, this will fail, need to delete 'migrations' folder
&nbsp; flask db migrate -m "some message, like, update columns"\
&nbsp;  flask db upgrade\
-. flask relationships, 3 tables: flask_model.py\
-. database in views: database_view folder\
&nbsp; complete a fully functioning website\
-. exercise: database project: database_exercise folder\
this is just a upgrade of database_view website\
code all myself\
large flask applications\
-. see 'structure-example.txt'\
-. restructure the application using Blueprint: large_application folder\
Migrate\
-. user authentication: Migrate folder\
&nbsp; pip install flask-bcrypt\
&nbsp; pip install Werkzeug\
-. flask login: Migrate/try_glask_login folder\
&nbsp; pip install flask-login\
-. flask OAuth\
&nbsp; flash-dance.readthedocs.io\
&nbsp; pip install Flask-Dance\
&nbsp; flask OAuth with Google example: Migrate/OAuth_google_example folder\
Large Project: Social Company Blog: Large_project_company_blog folder\
-. we will combine all the skills we've learned so far into a singular project.\
-. we'll create a company blog page, where multiple users can log in, create blog posts,
 and update or delete their existing blog posts.\
-. also learn handling image files, dividing long pages into multiple pages (for posts),
using Bootstrap pop up modals\
