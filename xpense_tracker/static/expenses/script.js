document.addEventListener("DOMContentLoaded", function() {
  // Get the modal
  var modal = document.getElementById("addExpenseModal");

  // Get the button that opens the modal
  var btn = document.getElementById("addExpenseBtn");

  // Get the <span> element that closes the modal
  var span = document.getElementById("closeButton");

  // When the user clicks on the button, open the modal
  btn.onclick = function() {
      modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function(event) {
      console.log("Close button clicked"); // Add this line
      event.stopPropagation(); // Prevents the event from bubbling up the DOM tree, preventing any parent handlers from being notified of the event
      modal.style.display = "none"; // Change from hide() to style.display
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }

  // Submit form data
  document.getElementById("expenseForm").addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the form from submitting traditionally
      var form = event.target;
      var formData = new FormData(form);
      // Here you can handle the form submission, for example, by sending data to the server
      // You can use formData to access form data
      // After handling form submission, you can close the modal
      modal.style.display = "none";
  });
});
