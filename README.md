# Web Data Capture

## Setup Instructions

1. Clone the repository.
2. Make sure you have Python and Node.js installed on your system.
3. Navigate to the backend folder using the following path: `\web-data-capture\backend`.
4. Install all requirements by running the following command:
    ```
    pip install -r requirements.txt
    ```
5. Generate all migration files:
    ```
    python manage.py makemigrations
    ```
6. Apply the migrations to the SQLite database:
    ```
    python manage.py migrate
    ```
7. Finally, run the Django ASGI server:
    ```
    python manage.py runserver
    ```

Now the server should be up and running, ready to capture web data.
