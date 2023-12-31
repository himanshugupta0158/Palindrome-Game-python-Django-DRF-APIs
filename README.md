# Palindrome Game Django APIs

- **Description:** This project implements REST APIs for a palindrome game using Python Django and Django Rest Framework (DRF). It includes user management and game-related APIs.
- **Database Used:**  <i>Postgresql Database</i>, you can do the required changes for setting up Postgresql with django by going into Django project root directory's settings.py's DATABASE variable and out required values for PostgreSQL there  like database name, username and password for PostgreSQL

## Setting Up the Project
Follow these steps to set up the project:
* Install Python Virtual Environment library :
* ```bash
  pip install virtualenv
  ```
* Create a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
  ```
* Activate the virtual environment:
  - On Windows
    ``` bash
    venv\Scripts\activate
    ```
  - On macOS and Linux:
    ``` bash
    source venv/bin/activate
    ```
* Clone this repository:
  ``` bash
  git clone <repository_url>
  cd Palindrome-Game-python-Django-DRF-APIs
  ```
* Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
* Run the Django development server:
   ```bash
  python manage.py migrate
  ```
  ```bash
  python manage.py runserver
  ```
**NOTE : The server will start at http://127.0.0.1:8000/.**

## API Documentation
You can access the API documentation at the following URL after starting the Django development server:
``` bash
http://127.0.0.1:8000/api-doc/
```
## APIs Available
1. User APIs
- Create User: POST /create-user/
- User View: GET /user-view/
- User Update: PUT /user-view/
- User Delete: DELETE /user-view/
- 
2. User Authentication
- User Login: POST /login/
- User Logout: GET /logout/
  
3. Game APIs
- Get Board: GET /getBoard/
- Update Board: GET /updateBoard/
- Combined Update Board: GET /combined-updateBoard/
- List Games: GET /list-games/

## User Management
- User creation, deletion, and update can be performed.
- Users can log in to access game-related functionality.

## Game Logic
- The game initializes with an empty string and returns a game ID.
- The getBoard API retrieves the string value from the server.
- The updateBoard API appends one character between 'a' and 'z' to the string and checks if the string is a palindrome.
- The list-games API lists all game IDs created in the system.
  
