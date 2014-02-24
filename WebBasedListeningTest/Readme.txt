1.Open views.py and enter your emailname and password.Your email should support STMP/POP3 service.

2.In cmd enter python manage.py syncdb to create new SQLite database.

3.In cmd enter python manage.py runserver to run the server.

4.Copy your sound sources to /static/mp3/ and in URL localhost:8000/mp3/ to scan sounds.

5.To see the backend information enter localhost:8000/admin/.