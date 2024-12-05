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
   - Users can create accounts, log in, and log out securely.
   - Authentication is required to perform certain actions like adding books, authors, and reviews or access the reading list.
   - User-specific data, such as reading lists is personalized for each account.
2. **Book Management**:
   - Users can browse and view detailed information about books, including title, author, description, genre, and publication date.
   - The application supports adding, editing, and deleting books.
   - Books can be sorted by title, author, date added, likes, or average rating, with ascending/descending toggle options.
   - Books can also be filtered by genre or searched dynamically.
3. **Reading List**:
   - Users can add books to a personalized reading list with statuses: "Reading," or "Finished."
   - The reading list is easily accessible and allows users to update the status of books directly.
   - Sorting and filtering options are available, similar to the main book management features.
   - An intuitive UI shows the current status of each book, with options to update or remove books from the reading list seamlessly.
4. **Author Management**:
   - Users can view a list of authors with their biographies.
   - Admins or the user who created an author can edit or delete them.
   - Authors can be sorted by name, date created, with ascending/descending toggle options.
   - A search feature allows users to quickly find specific authors.
5. **Reviews**:
   - Users can rate books using a 5-star system and leave comments.
   - Reviews can be added, edited, or deleted, with interactive modals for these operations.
   - The average rating for each book is dynamically calculated and displayed.
   - Pagination is available for reviews, ensuring a user-friendly experience even for books with many reviews.
6. **Interactive Modals**:
   - Modals are used for tasks like confirming deletions and editing reviews, enhancing the user experience.
   - Review modals dynamically pre-fill form fields with existing data, allowing for seamless updates.
   - JavaScript handlers manage the opening and closing of modals after form submission.
7. **Search and Filter**:
   - Real-time search across books, authors, and genres helps users find what they’re looking for quickly.
   - Advanced filtering options enable users to narrow down results by genre, author, or status (for the reading list).
   - Combined with sorting features, users can organize and locate content effortlessly.
8. **Responsive Design**:
   - The application is mobile-friendly, ensuring usability on all devices.
   - Layouts dynamically adjust for smaller screens while maintaining functionality and aesthetics.
9. **Administrative Features**:
   - A default admin account is created during setup, allowing the teacher or evaluator to test all features easily.
   - Admins have additional privileges, such as editing or deleting any content, including books, authors, and reviews.
10. **Real-Time Updates**:
    - JavaScript and Django integration ensure a responsive experience:
      - Adding or removing books from the reading list updates the UI immediately.
      - Review edits and deletions are reflected without needing to reload the page.
    - Server-side logic guarantees data integrity and consistency across all views.

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
