# SRIT Talks

**SRIT Talks** is an internal news feed platform built for the college community of SRIT. This platform allows users to share and view posts related to events, announcements, and news happening within the college. It is developed as a demo and has not yet been deployed.

## Features

- **User Authentication**: Users can register, log in, and manage their profile.
- **Post Creation**: Users can create, update, and delete posts.
- **Feed Display**: A feed page displays posts in chronological order.
- **User Profile**: Displays personal information and user's posts.
- **Admin Panel**: Admin can manage users and posts.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database)
- **Version Control**: Git, GitHub

## Setup

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/srit-talks.git
   cd srit-talks
2. **Create a Virtual Environment**:

   ```bash
   python -m venv env
3. **Activate the Virtual Environment**:

   ```bash
   .\env\Scripts\activate
4. **Install the Required Dependencies**:

   ```bash
   pip install -r requirements.txt
5. **Run Migrations**:

   ```bash
   python manage.py migrate
6. **Create a Superuser (Admin)**:

   ```bash
   python manage.py createsuperuser
7. **Run the Development Server**:

   ```bash
   python manage.py runserver
8.Access the Project:

Visit http://127.0.0.1:8000/ to view the project.
Go to http://127.0.0.1:8000/admin/ to access the admin panel.

**Usage**
  - **Login: Users can log in using their registered credentials.
  - **Post Creation: After logging in, users can create posts that will appear on the feed.
  - **Profile: Users can view their profile and posts they have created.
**Future Enhancements**
  - **Deployment: Plan to deploy the project on a public platform.
  - **Additional Features: Add commenting, notifications, and more content filtering options.
**License**
This project is licensed under the MIT License - see the LICENSE file for details.
