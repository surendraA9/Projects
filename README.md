# SRIT Talks

SRIT Talks is an internal news feed platform built for the college community of SRIT. It allows users to share and view posts related to events, announcements, and news happening within the college. The project is developed as a demo and is not deployed yet.

## Features

- **User Authentication**: Users can register, login, and manage their profile.
- **Post Creation**: Users can create, update, and delete posts.
- **Feed Display**: A feed page that displays posts in a chronological order.
- **User Profile**: Displays personal information and user's posts.
- **Admin Panel**: Admin can manage users and posts.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database)
- **Version Control**: Git, GitHub

## Setup

Follow these steps to get the project up and running locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/srit-talks.git
   cd srit-talks
Create a Virtual Environment:

bash
Copy code
python -m venv env
Activate the Virtual Environment:

On Windows:
bash
Copy code
.\env\Scripts\activate
On MacOS/Linux:
bash
Copy code
source env/bin/activate
Install the Required Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (Admin):

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Project:

Go to http://127.0.0.1:8000/ to view the project.
Go to http://127.0.0.1:8000/admin/ to access the admin panel.
Usage
Login: Users can log in using their registered credentials.
Post Creation: After logging in, users can create posts that will appear on the feed.
Profile: Users can view their own profile and the posts they have created.
Future Enhancements
Deployment: Plan to deploy the project on a public platform.
Additional Features: Add commenting, notifications, and more dynamic content filtering.
License
