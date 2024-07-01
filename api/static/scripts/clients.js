// clients.js
document.addEventListener('DOMContentLoaded', () => {
    fetchClientsData();
});

function fetchClientsData() {
    fetch('http://localhost:8080/client/clients')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#clients-table tbody');
            tableBody.innerHTML = '';  // Clear existing rows

            data.forEach(client => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${client.first_name}</td>
                    <td>${client.model}</td>
                    <td>${client.license_plate}</td>
                    <td>
                        <button class="add-to-queue-button" data-client-id="${client.client_id}">Add to Queue</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });

            document.querySelectorAll('.add-to-queue-button').forEach(button => {
                button.addEventListener('click', () => {
                    const clientId = button.getAttribute('data-client-id');
                    const client = data.find(c => c.client_id === clientId);
                    if (client) {
                        const queueItem = {
                            name: client.first_name,
                            model: client.model,
                            license_plate: client.license_plate
                        };
                        addToQueue(queueItem);
                    }
                });
            });
        })
        .catch(error => console.error('Error fetching clients data:', error));
}

function addToQueue(queueItem) {
    fetch('http://localhost:8080/queue/queue/add_client', {
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
