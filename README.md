This is basic Python REST API with Flask and SQLite as database.
The application implements endpoint that retrieves users from database, and performs CRUD operations on data.  
Flask is installed via command 'pip install flask'.
The app can be started wth command 'flask run' or 'python3 app.py'.
This will start a default development server on http://127.0.0.1:5000.
Sample sqlite database is generated running 'python3 create_database.py'.
Application is tested by sending calls directly to development server, no mocks are used. 
Tests are using unnitest library, and can be run locally via command 'python3 -m  unittest'.
Test workflow is also running on GitHub Actions.




