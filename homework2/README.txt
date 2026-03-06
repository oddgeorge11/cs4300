Movie Theatre Booking app

This is a Django app that allows a user to book from 5 different movie showings using Django REST Framework. A user account can be created via Django's manage.py createsuperuser command. With this acccount, a user can go and look at each movie on the website and choose to book different seats that are available to them. A user can also delete a seat booking if they would like.

How to run locally:
1) Install packages
pip install -r requirements.txt

2) Migrate database
python manage.py migrate

3) Run server
python manage.py runserver 0.0.0.0:8000

4) Open in browser
http://localhost:8000/

Additional endpoints:

Login page:
http://localhost:8000/accounts/login/

Admin page:
http://localhost:8000/admin/

API endpoints:
/api/movies/
/api/seats/
/api/bookings/

To run on Render:
./build.sh

Start command
python -m gunicorn movie_theater_booking.asgi:application -k uvicorn.workers.UvicornWorker

Code Structure:
homework2/
  manage.py
  requirements.txt
  build.sh
  movie_theater_booking/
    settings.py
    urls.py
    wsgi.py
    asgi.py
  bookings/
    models.py
    views.py
    urls.py
    serializers.py
    tests.py
    templates/
      bookings/
      registration/
    migrations/

AI was used in tandom with the provided resources to help further explain how this project was to be accomplished and to help generate a starting point for each of the different 3.x assignment parts. For example, AI was used to help come up with some of the ideads for the Integration and BDD testing, as well as to review any code errors encounted to help explain issues and provide soltuions or reoucources to fix the issue.

PS: Enjoy them mix of 2000's comedy moives!
