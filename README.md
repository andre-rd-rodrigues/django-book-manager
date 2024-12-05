# 📚 **Book Manager**

## **Overview**

Book Manager is a CRUD web application designed to help users manage their personal book collections, track their reading lists, and write reviews. It enables users to browse books, authors, and genres, while also providing a user-friendly platform to manage their reading habits. The app is built using Django for the backend and integrates a responsive front-end to ensure a seamless user experience.

---

## **Distinctiveness and Complexity**

### **Distinctiveness**

Book Manager is distinct from other projects in CS50's Web Programming course because:

1. It is not an e-commerce platform or a social network.
2. It focuses on personal book management, including features like creating a reading list, adding and editing books and authors, browsing books by genres or authors, and managing book reviews.
3. The application supports dynamic, real-time updates using Django models and templates for seamless user interaction.
4. It utilizes Docker containerization for simplified deployment and testing.

### **Complexity**

Book Manager satisfies the complexity requirement by:

1. Utilizing Django’s relational database to model relationships between books, authors, users, likes, reading list and reviews.
2. Incorporating user authentication and permissions to manage personalized experience.
3. Leveraging responsive design principles to create a mobile-friendly interface.
4. Implementing comprehensive filtering and ordering systems:
   - Books can be ordered by title, genre, author, date added, ratings and likes count;
   - Reading lists include additional filtering by book reading status;
   - Authors can be filtered by search and ordered by name and by creation user;
   - All listings support ascending/descending order direction.
5. Implementing interactive modals using JavaScript and Django integration:
   - Confirmation modals for all deletion operations to prevent accidental deletions
   - Edit and delete review operations are handled through modals for improved user experience
   - Custom JavaScript handlers manage modal interactions and form submissions

---

## **Features**

### Core Features

- **User Authentication**: Users can sign up and log in.
- **Book Management**:
  - Browse and manage books, view detailed information
  - Add, edit and delete new books
  - Search functionality for finding specific books
  - Order books by title, author, date added, or number of likes
  - Toggle ascending/descending order
  - Filter using the search functionality
- **Reading List**:
  - Personalized reading list with book status tracking
  - Same ordering and search options as book management
  - Additional filtering by reading status
- **Author Management**:
  - Add, edit and delete new authors
  - Search functionality for finding specific authors
  - Order by author name or creation date
  - Toggle ascending/descending order
- **Reviews**: Users can rate and review books, with an average rating displayed for each book.
- **Responsive Design**: The application is mobile-friendly, ensuring usability across devices.

---

## **File Descriptions**

### Main Project Files

- **`manage.py`**: Django's command-line utility for administrative tasks
- **`requirements.txt`**: Lists all Python dependencies for the project
- **`docker-compose.yml`**: Docker Compose configuration for containerization
- **`dockerfile`**: Docker configuration for building the application container
- **`entrypoint.sh`**: Shell script for Docker container initialization

### App Files (`book_manager/`)

- **`models.py`**: Defines database models for books, authors, reviews, and users
- **`views.py`**: Contains view functions to handle HTTP requests and return responses
- **`urls.py`**: Maps URLs to view functions for the app
- **`forms.py`**: Contains form definitions for data input handling

#### Templates (`book_manager/templates/book_manager/`)

- **`layout.html`**: Base template for all pages
- **`index.html`**: Homepage template
- **`books.html`**: Displays list of books
- **`book.html`**: Shows detailed information for a specific book
- **`book_card.html`**: Reusable component for book display
- **`add_book.html`**: Form template for adding new books
- **`edit_book.html`**: Form template for editing books
- **`authors.html`**: Displays list of authors
- **`add_author.html`**: Form template for adding new authors
- **`edit_author.html`**: Form template for editing authors
- **`reading_list.html`**: Template for user's reading list
- **`login.html`**: Login page template
- **`register.html`**: Registration page template
- **`_star_rating.html`**: Reusable component for star ratings

#### Static Files (`book_manager/static/`)

- **`css/`**: Contains CSS stylesheets
- **`images/`**: Stores image assets
- **`js/script.js`**: JavaScript code for client-side functionality

### Project Configuration (`myproject/`)

- **`settings.py`**: Project settings and configuration
- **`urls.py`**: Project-level URL configuration
- **`wsgi.py`**: WSGI application configuration
- **`asgi.py`**: ASGI application configuration

### Additional Files

- **`.gitignore`**: Specifies which files Git should ignore
- **`.prettierignore`**: Configuration for Prettier code formatter
- **`Makefile`**: Contains commands for project management

---

## **How to Run the Application**

### Option 1: Using Docker Compose (Recommended)

1. **Clone the Repository**:

```bash
git clone https://github.com/andre-rd-rodrigues/django-book-manager
cd django-book-manager
```

2. **Run with Docker Compose**:

To run the project using Docker Compose, follow these steps:

1. Build the Docker image: Before starting the application, build the Docker image locally:

```bash
docker-compose build
```

2. Start the application: Once the image is built, you can start the application:

```bash
docker-compose up
```

The application will be accessible at:

- Frontend: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

**Note:** A default admin account will be automatically created when running `restore-db`. For security purposes, please change the admin password after first login.

### Option 2: Manual Setup

1. **Clone the Repository**:

```bash
git clone https://github.com/andre-rd-rodrigues/django-book-manager
cd django-book-manager
```

2. **Set Up the Virtual Environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

4. **Apply Migrations**:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the Server**:

```bash
python manage.py runserver
```

---

## **Features in Detail**

1. **User Authentication**:
   - Users can create accounts, log in, and log out.
   - User-specific reading lists and reviews are tied to their accounts.
2. **Book Management**:
   - Books are displayed with details like title, author, genre, and description.
   - Relationships between books and authors are dynamically managed using Django models.
3. **Reading List**:
   - Users can mark books as "to read" or "read."
   - A dedicated page displays the user’s personalized reading list.
4. **Reviews**:
   - Users can write and edit reviews for books.
   - Average ratings are calculated and displayed dynamically.
5. **Search and Filter**:
   - A real-time search bar helps users find books by title, author, or genre.
   - Filter options enable browsing by genre or author.

---

## **Additional Information**

- **Dependencies**: The app uses the following major packages:

  - Django
  - SQLite (default database)
  - Font Awesome
  - Halfmoon CSS

- **Development Tools**:
  - VS Code for editing.
  - Git for version control.

---

## **Acknowledgments**

- The design and structure of the project draw upon lessons from CS50’s Web Programming course.
- Icons and design assets (if used) are sourced from free resources.
