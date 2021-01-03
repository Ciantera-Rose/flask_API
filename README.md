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
-app = Flask(__name__)

-Add Route:

    @app.route("/")
    def hello():
        return "Hey Flask"

    if __name__ == "__main__":
        app.run(debug=True)

-In Terminal Run:
    pipenv shell 
    python app.py

-Server should be working on local host: Mine is :5000
    ie: Running on http://127.0.0.1:5000/ 
    (Press CTRL+C) to end server session when needed
