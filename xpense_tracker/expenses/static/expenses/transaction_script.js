
function searchTransactions(event) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toLowerCase(); // Convert filter to lowercase
    var option = document.getElementById("searchOption").value;
    table = document.getElementById("transactionsTable");
    tr = table.getElementsByTagName("tr");

    var suggestions = []; // Array to store search suggestions

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[getOptionIndex(option)];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (option === "amount" && getAmount(txtValue) === parseInt(filter)) {
                tr[i].style.display = "";
                suggestions.push(txtValue); // Add suggestion
            } else if (option !== "amount" && txtValue.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                suggestions.push(txtValue); // Add suggestion
            } else {
                tr[i].style.display = "none";
            }
        }
    }

    // Display search suggestions
    showSuggestions(suggestions);
}

function getAmount(amountString) {
    // Extract the numeric part of the amount string
    return parseInt(amountString.match(/\d+/)[0]);
}






function showSuggestions(suggestions) {
    var suggestionsList = document.getElementById("suggestionsList");
    suggestionsList.innerHTML = ""; // Clear previous suggestions
    suggestions.forEach(function(suggestion) {
        var li = document.createElement("li");
        li.textContent = suggestion;
        suggestionsList.appendChild(li);
    });
}

function getOptionIndex(option) {
    switch (option) {
        case "date":
            return 0;
        case "category":
            return 1;
        case "name":
            return 2;
        case "amount":
            return 3;
        default:
            return 0;
    }
}



// Initial number of rows displayed
var numRowsDisplayed = 10;
var isShowingAll = false;

// Function to toggle display of additional rows
function toggleTransactions() {
  var tableRows = document.querySelectorAll('#transactionsTable tbody tr');
  isShowingAll = !isShowingAll;
  for (var i = numRowsDisplayed; i < tableRows.length; i++) {
    tableRows[i].classList.toggle('hidden', !isShowingAll);
  }
  document.getElementById('readMoreButton').innerText = isShowingAll ? 'Show Less' : 'Read More';
}

// Call toggleTransactions initially
toggleTransactions();

// Call toggleTransactions again to ensure only 10 entries are visible initially
toggleTransactions();



