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
    * This means we are going to define the table we want to work with and then 
      allow that code to generate the table for us.
    * For this process we don’t need the app route. So we can remove app@ 
      property along with function that follows so it’s not in the way.  
    * We will be building out our own API endpoint and integrate with the file 
      system so we can save our database to our project. To do this, we previously imported the os library  and can now work with it. 

-Create variable basedir. This variable is the base directory for our application. 
 This allows flask to  know where to save our SQL table to.

    basedir = os.path.abspath(os.path.dirname(__file__))     

    *So the base directory of our application is followed by the operating system 
     library path, the absolute path, which is a function so we pass in the argument
     path and the file we are calling. Simply telling flask in our server/environment where the app is located so it knows where to place our SQLlite database.

-Then we perform a lookup and set a value in our application with:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

    *Allows sql database to know where to go and what the values are. Then pass in string + paths,
     one path being basedir we created and the name of the database we created.

-Now we can create a database object and marshmallow object and pass in arguments (app) (or file name)

    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    *So now we have a SQLlite database and have instantiated a db and ma object.

-Next: Create Schema for table:
    Class Guide(db.Model): (inherits from object db.(model method from that library))   
        id = db.Column(db.Integer, primary_key=True)  
            (Built in column set automtically, primary unique id that increments as new data is added)
        title = db.Column(db.String(100), unique=False)
        content = db.Column(db.String(144), unique=False)

-Constructor for when a guide is called
    class Guide(db.Model):
    def __init__(self, title, content):
        self.title = title
        self.content = content 
