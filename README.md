This is basic Python REST API with Flask and SQLite as database, no frontend templates are used.
The application implements endpoint that retrieves users from database, and performs CRUD operations on data.  
Flask is installed via command 'pip install flask'.
The app can be staretd wth command 'flask run' or 'python3 app.py'. 
This will start a default develpment server on http://127.0.0.1:5000.
Test API calls are send directly to development server, no mocks are used. 
Tests are using unnitest library, and can be run locally via command 'python3 tests.py'.
Test workflow is also running on GitHub Actions.




