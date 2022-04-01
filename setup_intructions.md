## Steps to deploy django app to heroku
step 1: create a heroku account
step 2: download heroku CLI
step 3: open your cmd or powershell and type command 
heroku login
your browser will open a window login with your heroku credentials there.
step 4: within your local repositories main directory open terminal
step 5: type command 
heroku create -a some-name-for-your-app
step 6: now install gunicorn and django-heroku using command
pip install gunicorn django-heroku
step 7: create a requirements.txt file using command
pip freeze > requirements.txt
step 8: within your main directory create a file named 'Procfile'
step 9: inside that file add these lines (replace your-project-name with your projects name)
web: gunicorn your-project-name.wsgi
step 10: now in your settings.py add these lines
import django-heroku
django_heroku.settings(locals())
step 11: git commit -a "with some message"
step 12: git push heroku master (if you have commited all the changes to master branch)
step 13: wait for some while and heroku will deploy your django app for you and will provide with the link
step 14: add the domain name heroku provided you with in allowed hosts list within your settings.py file
step 15: change debug settings to DEBUG = False also in settings.py
repeat step 11 and 12 to re-deploy your changes
step 16: run command in terminal
heroku run python manage.py makemigrations
heroku run python manage.py migrate


