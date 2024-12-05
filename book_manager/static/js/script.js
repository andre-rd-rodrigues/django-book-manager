document.addEventListener("DOMContentLoaded", function () {
  // Like book
  document.querySelectorAll(".like-button").forEach((button) => {
    button.addEventListener("click", function () {
      const bookId = this.getAttribute("data-book-id");
      const likeCountElement = document.getElementById(`likes-count-${bookId}`);
      const iconElement = this.querySelector("i");

      // Send POST request to like the book
      fetch("/books/like/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ book_id: bookId })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            console.error(data.error);
            return;
          }
          // Update the like count
          likeCountElement.textContent = data.like_count;

          // Toggle the like button icon
          if (data.liked) {
            iconElement.classList.remove("far");
            iconElement.classList.add("fas", "text-danger");
          } else {
            iconElement.classList.remove("fas", "text-danger");
            iconElement.classList.add("far");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });

  // Delete book
  document.querySelectorAll(".delete-button").forEach((button) => {
    button.addEventListener("click", function () {
      const bookId = this.getAttribute("data-book-id");

      fetch(`/books/${bookId}/delete/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": getCookie("csrftoken")
        }
      }).then((response) => {
        if (response.ok) {
          window.location.href = "/"; // Redirect to home page after deletion
        } else {
          alert("Error deleting book");
        }
      });
    });
  });

  // Toggle bookmark
  document.querySelectorAll(".bookmark-button").forEach((button) => {
    button.addEventListener("click", function () {
      const bookId = this.getAttribute("data-book-id");

      // Send request to toggle bookmark
      fetch(`/reading/${bookId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ action: "toggle_bookmark" })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "added") {
            this.innerHTML = '<i class="fas fa-bookmark"></i>';
          } else if (data.status === "removed") {
            this.innerHTML = '<i class="far fa-bookmark"></i>';
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });

  // Update book status
  document.querySelectorAll(".update-status-form").forEach((form) => {
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission

      const bookId = this.querySelector(".reading-list-status").getAttribute(
        "data-book-id"
      );
      const status = this.querySelector(".reading-list-status").value;

      fetch(`/reading/${bookId}/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ status })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            console.error("Error updating status:", data.error);
          } else {
            window.location.reload();
            console.log(
              `Status updated to ${data.status} for book ID ${bookId}`
            );
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });

  // Set hidden input field for book ID on remove from reading list button
  document
    .querySelectorAll(".remove-from-reading-list-button")
    .forEach((button) => {
      button.addEventListener("click", function () {
        const bookId = this.getAttribute("data-book-id");
        document.getElementById("removeFromReadingListBookId").value = bookId;
      });
    });

  // Remove book from reading list
  document
    .querySelectorAll(".remove-from-reading-list-button-modal")
    .forEach((button) => {
      button.addEventListener("click", function () {
        const bookId = document.getElementById(
          "removeFromReadingListBookId"
        ).value;

        fetch(`/reading/${bookId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
          },
          body: JSON.stringify({ action: "toggle_bookmark" })
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.status === "removed") {
              window.location.reload();
            } else {
              console.error("Unexpected response:", data);
            }
          })
          .catch((error) => console.error("Error:", error));
      });
    });

  // Handle delete button clicks
  document
    .querySelectorAll("[data-bs-target='#deleteModal']")
    .forEach((button) => {
      button.addEventListener("click", function () {
        // Get the author ID from the clicked button
        const authorId = this.getAttribute("data-author-id");

        // Set the author ID in the modal's delete button
        const deleteButton = document.querySelector(".delete-author-button");
        deleteButton.setAttribute("data-author-id", authorId);

        // Optionally update the modal's body or title with author-specific information
        const modalBody = document.querySelector("#deleteModal .modal-body");
        modalBody.textContent = `Are you sure you want to delete this author? This will delete all books associated with them.`;
      });
    });

  // Edit review
  document.querySelectorAll(".edit-review-btn").forEach((button) => {
    button.addEventListener("click", function () {
      // Get review details from data attributes
      const reviewId = this.getAttribute("data-review-id");
      const reviewComment = this.getAttribute("data-review-comment");
      const reviewRating = this.getAttribute("data-review-rating");

      // Set the form action dynamically
      const editForm = document.getElementById("editReviewForm");
      editForm.action = `/reviews/${reviewId}/edit/`;

      // Populate the modal fields
      document.getElementById("editReviewComment").value = reviewComment;
      document.getElementById("editReviewRating").value = reviewRating;

      // Set the hidden input field for review ID
      document.getElementById("editReviewId").value = reviewId;
    });
  });

  // Set the hidden input field for review ID
  document.querySelectorAll(".delete-review-btn").forEach((button) => {
    button.addEventListener("click", function () {
      const reviewId = this.getAttribute("data-review-id");
      document.getElementById("deleteReviewId").value = reviewId;
    });
  });

  // Handle update review
  document
    .getElementById("editReviewForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      const reviewId = document.getElementById("editReviewId").value;
      const formData = {
        rating: document.getElementById("editReviewRating").value,
        comment: document.getElementById("editReviewComment").value
      };

      fetch(`/reviews/${reviewId}/edit/`, {
        method: "PATCH",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Failed to update review");
          }
        })
        .then((data) => {
          window.location.reload();
        })
        .catch((error) => console.error("Error:", error));
    });

  // Delete review
  document.querySelectorAll(".delete-review-btn-modal").forEach((button) => {
    button.addEventListener("click", function () {
      const reviewId = document.getElementById("deleteReviewId").value;

      fetch(`/reviews/${reviewId}/delete/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": getCookie("csrftoken")
        }
      }).then((response) => {
        if (response.ok) {
          window.location.reload();
        } else {
          console.error("Error deleting review");
        }
      });
    });
  });

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
