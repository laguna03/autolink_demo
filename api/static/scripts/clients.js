// clients.js
document.addEventListener('DOMContentLoaded', () => {
    fetchClientsData();
});

function fetchClientsData() {
    fetch('http://localhost:8080/client/clients')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#clients-table-body');
            tableBody.innerHTML = '';  // Clear existing rows

            data.forEach(client => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${client.first_name}</td>
                    <td>${client.model}</td>
                    <td>${client.license_plate}</td>
                    <td>
                        <button class="add-to-queue-button" data-client-info='${JSON.stringify(client)}'>Add to Queue</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });

            document.querySelectorAll('.add-to-queue-button').forEach(button => {
                button.addEventListener('click', () => {
                    const clientInfo = JSON.parse(button.getAttribute('data-client-info'));
                    const queueItem = {
                        name: clientInfo.first_name,
                        model: clientInfo.model,
                        license_plate: clientInfo.license_plate
                    };
                    addToQueue(queueItem);
                });
            });
        })
        .catch(error => console.error('Error fetching clients data:', error));
}

function addToQueue(queueItem) {
    fetch('http://localhost:8080/queue/queue/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(queueItem)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => console.error('Error adding client to queue:', error));
}
