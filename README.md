# task_server

to run the application in debug mode:

1) Install the required dependencies from the requipments folder
2) Set the following environment variables:
      - SECRET_KEY - for securely signing the session cookie and can be used for any other security related needs by extensions or your application
      - APP_SETTINGS - application configuration option (example: "config.DevelopmentConfig")
      - JWT_SECRET_KEY - to encode and decode JWTs when using a symmetric signing algorightm
      - DATABASE_URL
3) Run the following commands sequentially to create the database and migrations
      - python manage.py db init
      - python manage.py db migrate
      - python manage.py db upgrade
4) To run the application, execute the command:
      - python manage.py runserver
      
URL for API Doc:
      basepath/api/ui
