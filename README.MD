# Blog Application

A Django blog application where users can register, log in, create blog posts, and manage their own posts.

## Features
- User registration, login, and logout
- Authentication-protected pages (create, edit, delete require login)
- Ownership-based authorization (users can only edit/delete their own posts)
- Full CRUD for blog posts
- "My Posts" page showing only the logged-in user's posts

## Tech Stack
- Python, Django
- SQLite
- Django Templates, Django Forms, Django ORM
- Custom CSS

## Setup Instructions

1. Clone the repository
   \`\`\`
   git clone https://github.com/Shuvonkar005/blog_project
   cd blog_project
   \`\`\`

2. Create and activate a virtual environment
   \`\`\`
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Mac/Linux
   \`\`\`

3. Install dependencies
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Run migrations
   \`\`\`
   python manage.py migrate
   \`\`\`

5. Create a superuser (optional, for admin access)
   \`\`\`
   python manage.py createsuperuser
   \`\`\`

6. Run the development server
   \`\`\`
   python manage.py runserver
   \`\`\`

7. Visit `http://127.0.0.1:8000/blog/`

## Project Structure
- `blogsite/` — project settings and root URL configuration
- `blog/` — main app: models, views, forms, templates, static files