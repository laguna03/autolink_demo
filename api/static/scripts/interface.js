document.addEventListener('DOMContentLoaded', () => {
    fetchQueueData();
});

function fetchQueueData() {
    fetch('http://localhost:8080/queue/queue')
        .then(response => response.json())
        .then(data => {
            const queueTableBody = document.querySelector('#queue-table-body');
            queueTableBody.innerHTML = '';  // Clear existing rows

            let totalTime = 0;

            // Calculate total time from ongoing services
            data.ongoingServices.forEach(service => {
                const serviceTime = parseInt(service.time);
                if (!isNaN(serviceTime)) {
                    totalTime += serviceTime;
                }
            });

            // Populate Queue Table
            data.queue.forEach((item, index) => {
                const estimatedTime = totalTime + (index * 15); // Assuming each service takes 15 minutes
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.name}</td>
                    <td>${item.model}</td>
                    <td>${item.license_plate}</td>
                    <td>${formatTime(estimatedTime)}</td>
                `;
                queueTableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching queue data:', error));
}

function formatTime(minutes) {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
}
