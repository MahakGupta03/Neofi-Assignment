# Neofi-Assignment
# Installation
1.Clone the repository:
git clone https://github.com/your_username/note-taking-app.git

2. Install the dependencies:
cd note-taking-app\n
pip install -r requirements.txt

3. Set up the database:
python manage.py makemigrations
python manage.py migrate

4.Create a superuser:
python manage.py createsuperuser

5.Run the development server:
python manage.py runserver

# Usage
To create a new note, send a POST request to /notes/create/ with the note data.
To retrieve a specific note, send a GET request to /notes/{id}/.
To share a note with other users, send a POST request to /notes/share/ with the note ID and user IDs.
To update an existing note, send a PUT request to /notes/update/{id}/ with the updated note data.
To get the version history of a note, send a GET request to /notes/version-history/{id}/.
