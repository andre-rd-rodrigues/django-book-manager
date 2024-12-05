document.addEventListener("DOMContentLoaded", function () {
  // Like book
  document.querySelectorAll(".like-button").forEach((button) => {
    button.addEventListener("click", function () {
      const bookId = this.getAttribute("data-book-id");
      const likeCountElement = document.getElementById(`likes-count-${bookId}`);
      const iconElement = this.querySelector("i");

      // Send POST request to like the book
      fetch("/books/like", {
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

      fetch(`/books/${bookId}/delete`, {
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
      fetch(`/reading/${bookId}`, {
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

      fetch(`/reading/${bookId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value
        },
        body: JSON.stringify({ status })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            console.error("Error updating status:", data.error);
          } else {
            console.log(
              `Status updated to ${data.status} for book ID ${bookId}`
            );
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });

  // Remove book from reading list
  document.querySelectorAll(".remove-from-reading-list").forEach((button) => {
    button.addEventListener("click", function () {
      const bookId = this.getAttribute("data-book-id");

      fetch(`/reading/${bookId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value
        },
        body: JSON.stringify({ action: "toggle_bookmark" })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "removed") {
            // Remove the book's card from the DOM
            const card = button.closest(".col-12");
            card.parentNode.removeChild(card);
            window.location.reload();
          } else {
            console.error("Unexpected response:", data);
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });

  // Delete author

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

  // Handle delete action
  document.querySelectorAll(".delete-author-button").forEach((button) => {
    button.addEventListener("click", function () {
      const authorId = this.getAttribute("data-author-id");

      fetch(`/authors/${authorId}/delete`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": getCookie("csrftoken")
        }
      })
        .then((response) => {
          if (response.ok) {
            window.location.reload();
          } else {
            console.error("Error deleting author");
          }
        })
        .catch((error) => console.error("Error:", error));
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
