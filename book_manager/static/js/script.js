document.addEventListener("DOMContentLoaded", function () {
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
