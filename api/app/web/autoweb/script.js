document.querySelector('.logout').addEventListener('click', function(e) {
    e.preventDefault();
    window.location.href = 'login.html';
});


document.addEventListener('DOMContentLoaded', function () {
    fetchQueueData();
    fetchClientsData();
});

function fetchQueueData() {
    fetch('http://localhost:8000/api/queue')
        .then(response => response.json())
        .then(data => populateQueueTable(data))
        .catch(error => console.error('Error fetching queue data:', error));
}

function fetchClientsData() {
    fetch('http://localhost:8000/api/clients')
        .then(response => response.json())
        .then(data => populateClientsTable(data))
        .catch(error => console.error('Error fetching clients data:', error));
}

function populateQueueTable(data) {
    const tableBody = document.querySelector('#queue-table tbody');
    tableBody.innerHTML = '';

    data.forEach(row => {
        const tr = document.createElement('tr');

        const nameTd = document.createElement('td');
        nameTd.textContent = row.name;
        tr.appendChild(nameTd);

        const statusTd = document.createElement('td');
        const select = document.createElement('select');
        const optionInProcess = document.createElement('option');
        optionInProcess.value = 'in_process';
        optionInProcess.textContent = 'In Process';
        if (row.status === 'in_process') optionInProcess.selected = true;
        const optionPending = document.createElement('option');
        optionPending.value = 'pending';
        optionPending.textContent = 'Pending';
        if (row.status === 'pending') optionPending.selected = true;
        select.appendChild(optionInProcess);
        select.appendChild(optionPending);
        statusTd.appendChild(select);
        tr.appendChild(statusTd);

        const etTd = document.createElement('td');
        etTd.textContent = row.et;
        tr.appendChild(etTd);

        const serviceCodeTd = document.createElement('td');
        serviceCodeTd.textContent = row.service_code;
        tr.appendChild(serviceCodeTd);

        tableBody.appendChild(tr);
    });
}

function populateClientsTable(data) {
    const tableBody = document.querySelector('#clients-table tbody');
    tableBody.innerHTML = '';

    data.forEach(row => {
        const tr = document.createElement('tr');

        const nameTd = document.createElement('td');
        nameTd.textContent = row.name;
        tr.appendChild(nameTd);

        const licensePlateTd = document.createElement('td');
        licensePlateTd.textContent = row.license_plate;
        tr.appendChild(licensePlateTd);

        const dateTd = document.createElement('td');
        dateTd.textContent = row.date;
        tr.appendChild(dateTd);

        tableBody.appendChild(tr);
    });
}
