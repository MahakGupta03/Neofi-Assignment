# Neofi-Assignment
# Installation
1.Clone the repository:
git clone https://github.com/your_username/note-taking-app.git

2.Install the dependencies:<br />
cd note-taking-app<br />
pip install -r requirements.txt

3.Set up the database:<br />
python manage.py makemigrations<br />
python manage.py migrate

4.Create a superuser:<br />
python manage.py createsuperuser

5.Run the development server:<br />
python manage.py runserver

# Usage
To create a new note, send a POST request to /notes/create/ with the note data.<br />
To retrieve a specific note, send a GET request to /notes/{id}/.<br />
To share a note with other users, send a POST request to /notes/share/ with the note ID and user IDs.<br />
To update an existing note, send a PUT request to /notes/update/{id}/ with the updated note data.<br />
To get the version history of a note, send a GET request to /notes/version-history/{id}/.
