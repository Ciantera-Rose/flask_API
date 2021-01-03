FLASK API SET-UP Instructions 

-Open Terminal
-mkdir "some file name"
-cd into new project
-code . (Open text editor)
-Open Terminal (In vsCode for MAC = CTRL~)
-pipenv --three
-ls (shows pipfile is there. Also shows in file section)
-pipenv install flask
-create an app.py file

-STEPS:

-from flask import Flask
-Create variable to instantiate a new version of flask:
    app = Flask(__name__)

-CREATE First Route:
    @app.route("/")

-CREATE the Method:    
    def hello():
        return "Hey Flask"

-CALL the method you created:
    if __name__ == "__main__":
        app.run(debug=True)

-In Terminal Run:
    pipenv shell 
    python app.py

-Server should be working on local host: Mine is :5000
    ie: Running on http://127.0.0.1:5000/ 
    (Press CTRL+C) to end server session when needed

-Install Dependencies for Flask Database and API Features
    * pipenv install Flask-SQLAlchemy
    * pipenv install flask-marshmallow
    * pipenv install marshmallow-sqlalchemy

-Add dependency imports to top of app.py file
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_marshmallow import Marshmallow
    import os    

-Save File
-Run to test that everything is working on local host:
    pipenv shell
    python3 app.py 

-Programatically create a database table using SQLlite:
-Create a SCHEMA:  
    *This means we are going to define the table we want to work with and then 
     allow that code to generate the table for us.
    *For this process we don’t need the app route. So we can remove app@ 
     property along with function that follows so it’s not in the way.  

