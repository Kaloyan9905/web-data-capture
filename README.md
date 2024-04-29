# Web Data Capture

## Setup Instructions

1. Clone the repository.
2. Make sure you have Python and Node.js installed on your system.
3. Navigate to the backend folder and your terminal should look like this: `\web-data-capture\backend`.
4. Install all requirements by running the following command:
   
    ```
    pip install -r requirements.txt
    ```
6. Generate all migration files:
   
    ```
    python manage.py makemigrations
    ```
8. Apply the migrations to the SQLite database:
   
    ```
    python manage.py migrate
    ```
10. Finally, run the Django ASGI server:
    
    ```
    python manage.py runserver
    ```

Now the server should be up and running, ready to capture web data.
