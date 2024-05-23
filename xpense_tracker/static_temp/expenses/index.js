const sideMenu = document.querySelector('aside');
const menuBtn = document.getElementById('menu-btn');
const closeBtn = document.getElementById('close-btn');

const darkMode = document.querySelector('.dark-mode');

menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
});

darkMode.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode-variables');
    darkMode.querySelector('span:nth-child(1)').classList.toggle('active');
    darkMode.querySelector('span:nth-child(2)').classList.toggle('active');
})


Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
        <td>${order.productName}</td>
        <td>${order.productNumber}</td>
        <td>${order.paymentStatus}</td>
        <td class="${order.status === 'Declined' ? 'danger' : order.status === 'Pending' ? 'warning' : 'primary'}">${order.status}</td>
        <td class="primary">Details</td>
    `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
});






// // Get the canvas element
// var ctx = document.getElementById('myChart').getContext('2d');

// // Create the chart
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['January', 'February', 'March', 'April', 'May', 'June'],
//         datasets: [{
//             label: 'Monthly Spendings (in Rs)',
//             data: [5400, 6200, 5800, 5340, 6670, 5230],
//             fill: false,
//             borderColor: 'rgba(54, 162, 235, 1)',
//             backgroundColor: 'rgba(54, 162, 235, 0.2)',
//             borderWidth: 2
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//                 ticks: {
//                     callback: function (value, index, values) {
//                         return '₹' + value.toLocaleString();
//                     }
//                 }
//             }
//         },
//         plugins: {
//             legend: {
//                 position: 'bottom'
//             },
//             title: {
//                 display: true,
//                 text: 'Monthly Spendings',
//                 font: {
//                     size: 20,
//                     weight: 'bold'
//                 }
//             }
//         }
//     }
// });





// // Get the canvas element
// var ctx = document.getElementById('myChart').getContext('2d');

// // Create the chart
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['January', 'February', 'March', 'April', 'May', 'June'],
//         datasets: [{
//             label: 'Spendings',
//             data: [5400, 6200, 5800, 5340, 6670, 5230],
//             fill: false,
//             borderColor: 'rgb(75, 192, 192)',
//             tension: 0.4
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//                 ticks: {
//                     callback: function (value, index, values) {
//                         return '₹' + value;
//                     }
//                 }
//             }
//         },
//         plugins: {
//             legend: {
//                 display: false
//             },
//             title: {
//                 display: true,
//                 text: 'Monthly Spendings',
//                 font: {
//                     size: 18,
//                     weight: 'bold'
//                 }
//             }
//         }
//     }
// });





// Get the canvas element
var ctx = document.getElementById('myChart').getContext('2d');

// Create the chart
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [{
            label: 'Monthly Spendings (in Rs)',
            data: [5400, 6200, 5800, 5340, 6670, 5230],
            fill: false,
            borderColor: '#3498db', // Blue color for light mode
            backgroundColor: 'rgba(52, 152, 219, 0.2)',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    callback: function (value, index, values) {
                        return '₹' + value.toLocaleString();
                    }
                }
            }
        },
        plugins: {
            legend: {
                position: 'bottom'
            },
            title: {
                display: true,
                text: 'Monthly Spendings',
                font: {
                    size: 20,
                    weight: 'bold'
                }
            }
        }
    }
});







// Function to add a new reminder
// function addReminder(title, time) {
//     const notificationContainer = document.getElementById('notificationContainer');
//     const newNotification = document.createElement('div');
//     newNotification.classList.add('notification');
//     newNotification.innerHTML = `
//         <div class="icon">
//             <span class="material-icons-sharp">
//                 volume_up
//             </span>
//         </div>
//         <div class="content">
//             <div class="info">
//                 <h3>${title}</h3>
//                 <small class="text_muted">
//                     ${time}
//                 </small>
//             </div>
//             <span class="material-icons-sharp">
//                 more_vert
//             </span>
//         </div>
//     `;
//     notificationContainer.insertBefore(newNotification, notificationContainer.firstChild);
// }

// // Event listener for adding a new reminder
// document.getElementById('addReminder').addEventListener('click', function() {
//     const title = prompt('Enter reminder title:');
//     const time = prompt('Enter reminder time:');
//     if (title && time) {
//         addReminder(title, time);
//     }
// });







// Function to add a new reminder
function addReminder(title, time) {
    const notificationContainer = document.getElementById('notificationContainer');
    const newNotification = document.createElement('div');
    newNotification.classList.add('notification');
    newNotification.innerHTML = `
        <div class="icon">
            <span class="material-icons-sharp">
                volume_up
            </span>
        </div>
        <div class="content">
            <div class="info">
                <h3>${title}</h3>
                <small class="text_muted">
                    ${time}
                </small>
            </div>
            <span class="material-icons-sharp">
                more_vert
            </span>
        </div>
    `;
    notificationContainer.insertBefore(newNotification, notificationContainer.firstChild);
}

// Event listener for adding a new reminder
document.getElementById('addReminder').addEventListener('click', function () {
    const title = prompt('Enter reminder title:');
    const time = prompt('Enter reminder time:');
    if (title && time) {
        addReminder(title, time);
    }
});

// Event listener for adding a new reminder tab
document.getElementById('newReminderTab').addEventListener('click', function () {
    const title = prompt('Enter reminder title:');
    const time = 'Now';
    if (title) {
        addReminder(title, time);
    }
});


