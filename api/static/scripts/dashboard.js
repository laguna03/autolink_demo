document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:8000/client/dashboard-data') // Replace '/your-endpoint' with the URL to fetch data
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('table-container').getElementsByTagName('tbody')[0];
        data.forEach(item => {
            const row = tableBody.insertRow();
            const firstNameCell = row.insertCell(0);
            firstNameCell.textContent = item.first_name;
            const licensePlateCell = row.insertCell(1);
            licensePlateCell.textContent = item.license_plate;
            const dateCell = row.insertCell(2);
            dateCell.textContent = item.date;
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});



// document.addEventListener('DOMContentLoaded', function() {
//     fetch('http://localhost:8000/client/dashboard-data')
//         .then(response => response.json())
//         .then(data => {
//             const clientsTable = document.getElementById('clients-table');
//             clientsTable.innerHTML = '';
//             data.forEach(item => {
//                 const row = document.createElement('tr');
//                 row.innerHTML = `<td>${item.first_name}</td><td>${item.license_plate}</td><td>${item.date}</td>`;
//                 clientsTable.appendChild(row);
//             });
//         })
//         .catch(error => console.error('Error retrieving data:', error));
// });

var button = document.getElementById('toggle-sidebar');
var buttonImage = button.querySelector('.button-image');
var buttonImageClicked = button.querySelector('.button-image-clicked');

button.addEventListener('click', function() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');

    if (sidebar.classList.contains('open')) {
        buttonImage.style.display = 'none';
        buttonImageClicked.style.display = 'block';
    } else {
        buttonImage.style.display = 'block';
        buttonImageClicked.style.display = 'none';
    }
});
