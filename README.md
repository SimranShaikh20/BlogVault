# Blog Project

This is a Django-based project for managing blog posts. Users can register, log in, create, edit, delete, and search blog posts. Each user can only edit or delete their own blog posts.

## Features

- User authentication (Registration, Login, Logout)
- Create, read, update, and delete (CRUD) operations for blogs
- Search functionality for blog posts
- Restriction: Users can edit or delete only their own blogs

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SimranShaikh20/BlogVault
   cd blog-project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

```
blog-project/
├── app_name/           # Replace with your app name
│   ├── migrations/     # Database migration files
│   ├── templates/      # HTML templates
│   │   ├── app_name/   # Replace with your app name
│   │       ├── blog_list.html  # List view for blogs
│   │       ├── blog_form.html  # Form for creating/editing blogs
│   │       ├── register.html   # User registration page
│   │       ├── login.html      # User login page
│   └── views.py        # Application views
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Key Files

### `views.py`
Contains the logic for handling requests and rendering templates.

- **`blog_list`**: Displays a list of blog posts with search functionality.
- **`blog_create`**: Allows users to create a new blog post.
- **`blog_edit`**: Allows users to edit their own blog posts.
- **`blog_delete`**: Allows users to delete their own blog posts.
- **`register`**: Handles user registration.
- **`login_view`**: Handles user login.
- **`logout_view`**: Logs the user out.

### `urls.py`
Defines URL patterns for routing requests to the appropriate views.

### `models.py`
Defines the `Blog` model for storing blog post data in the database.

### `forms.py`
Contains form definitions for user registration and blog post creation/editing.

## Templates

### `blog_list.html`
Displays the list of blog posts with a search bar.

### `blog_form.html`
Form template for creating and editing blog posts.

### `register.html`
Template for user registration.

### `login.html`
Template for user login.

## Usage

### Register
1. Navigate to `/register/`.
2. Fill in the registration form and submit.

### Login
1. Navigate to `/login/`.
2. Enter your credentials and submit.

### Create a Blog Post
1. Log in to your account.
2. Navigate to `/create/`.
3. Fill out the form and submit.

### Edit or Delete a Blog Post
1. Log in to your account.
2. Navigate to the blog list.
3. Click on "Edit" or "Delete" for the blog post you own.

### Search Blog Posts
1. Use the search bar on the blog list page to filter posts by keywords.

## License

This project is licensed under the [MIT License](LICENSE).

---

### Contributions

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

### Contact

For questions or suggestions, please contact:

- **Name**: Simran Shaikh 
