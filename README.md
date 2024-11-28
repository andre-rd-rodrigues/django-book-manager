# 📚 **Book Manager**

## **Overview**

Book Manager is a web application designed to help users manage their personal book collections, track their reading lists, and write reviews. It enables users to browse books, authors, and genres, while also providing a user-friendly platform to manage their reading habits. The app is built using Django for the backend and integrates a responsive front-end to ensure a seamless user experience.

---

## **Distinctiveness and Complexity**

### **Distinctiveness**

Book Manager is distinct from other projects in CS50’s Web Programming course because:

1. It is not an e-commerce platform or a social network.
2. It focuses on personal book management, including features like creating a reading list, browsing by genres or authors, and managing book reviews.
3. The application supports dynamic, real-time updates using Django models and templates for seamless user interaction.

### **Complexity**

Book Manager satisfies the complexity requirement by:

1. Utilizing Django’s relational database to model relationships between books, authors, users, and reviews.
2. Incorporating user authentication and permissions to manage personalized reading lists.
3. Leveraging responsive design principles to create a mobile-friendly interface.
4. Employing advanced URL routing and filtering to enable dynamic search and browsing by authors, genres, and books.

---

## **Features**

### Core Features

- **User Authentication**: Users can sign up, log in, and manage their accounts.
- **Book Management**: Users can browse books, view detailed information, and explore by genres or authors.
- **Reading List**: Each user has a personalized reading list to track books they wish to read or have read.
- **Reviews**: Users can rate and review books, with an average rating displayed for each book.
- **Search and Filter**: A dynamic search bar allows users to find books by title, author, or genre.
- **Responsive Design**: The application is mobile-friendly, ensuring usability across devices.

### Optional Features

- **Trending Books**: Highlights books with the most recent reviews.
- **User Stats**: Displays statistics like the number of books read and average ratings given by the user.

---

## **File Descriptions**

### Main Project Files

- **`manage.py`**: Django’s command-line utility for administrative tasks.
- **`settings.py`**: Contains the global configuration for the project.
- **`urls.py`**: Defines URL routing for the project.
- **`db.sqlite3`**: The SQLite database file storing all application data.

### App Files (`book_manager`)

- **`models.py`**: Defines database models for books, authors, reviews, and users.
- **`views.py`**: Contains view functions to handle HTTP requests and return responses.
- **`urls.py`**: Maps URLs to view functions for the app.
- **`templates/book_manager/`**:
  - `base.html`: The base layout for all pages.
  - `index.html`: The homepage template.
  - `book_list.html`: Displays a list of books.
  - `book_detail.html`: Shows detailed information for a specific book.
- **`static/`**:
  - `styles.css`: Custom CSS for styling the app.

### Additional Files

- **`.gitignore`**: Specifies files to be ignored by Git.
- **`requirements.txt`**: Lists all Python dependencies for the project.

---

## **How to Run the Application**

1. **Clone the Repository**:

```jsx
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

1. **Set Up the Virtual Environment**:

```jsx
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. **Install Dependencies**:

```jsx
pip install -r requirements.txt
```

1. **Apply Migrations**:

```jsx
python [manage.py](http://manage.py/) makemigrations
python [manage.py](http://manage.py/) migrate
```

1. **Run the Server**:

```jsx
python [manage.py](http://manage.py/) runserver
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
  - Bootstrap (optional, for responsive design)
- **Development Tools**:
  - VS Code for editing.
  - Git for version control.

---

## **Acknowledgments**

- The design and structure of the project draw upon lessons from CS50’s Web Programming course.
- Icons and design assets (if used) are sourced from free resources.
