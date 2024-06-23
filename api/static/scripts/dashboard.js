document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:8000/client/dashboard-data')
        .then(response => response.json())
        .then(data => {
            const clientsTable = document.getElementById('clients-table');
            clientsTable.innerHTML = '';
            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${item.first_name}</td><td>${item.license_plate}</td><td>${item.date}</td>`;
                clientsTable.appendChild(row);
            });
        })
        .catch(error => console.error('Error al obtener datos:', error));
});

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
