# 📝 Blog System

A **Django-based Blog System** that allows users to create, read, update, and delete blog posts with a responsive frontend and secure backend. This project leverages Django, HTML, and Tailwind CSS for a seamless user experience.

---

## 🚀 Features

- ✍️ Create, edit, delete, and view blog posts (CRUD functionality)
- 🧑‍💻 Admin interface to manage content
- 🌐 Responsive frontend using **HTML + Tailwind CSS**
- 🛡️ Backend powered by Django and Python
- 💾 Data storage using SQLite (Django's default database)

---

## 📁 Project Structure

```
BLOG_SYSTEM/
├── myapp/
│   ├── migrations/
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── myblogproject/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
├── db.sqlite3
├── manage.py
```

### Key Directories and Files

- **myapp/**: Contains the core application logic for the blog system.
  - `admin.py`: Configuration for the admin panel.
  - `models.py`: Database models for the blog system.
  - `views.py`: Handles request/response logic.
  - `urls.py`: URL routing for the application.

- **myblogproject/**: Contains project-level settings and configuration files.
  - `settings.py`: Django project settings.
  - `urls.py`: URL configuration at the project level.
  - `wsgi.py` and `asgi.py`: Files for WSGI and ASGI server deployment.

- **templates/**: Stores HTML templates for rendering the frontend of the blog.
- **db.sqlite3**: The SQLite database file.
- **manage.py**: A command-line utility for managing the Django project.



## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)
- Django

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/radhipatel157/Blog-System.git
   cd Blog-System
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

---

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
﻿# Blog-System
