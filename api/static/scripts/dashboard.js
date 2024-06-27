document.addEventListener('DOMContentLoaded', () => {
	fetchQueueData();

	document.getElementById('add-client-button').addEventListener('click', function() {
			const clientName = document.getElementById('client-name').value;
			if (clientName) {
					fetch(`http://localhost:8000/queue/add`, {
							method: 'POST',
							headers: {
									'Content-Type': 'application/json'
							},
							body: JSON.stringify({ name: clientName })
					})
					.then(response => response.json())
					.then(data => {
							console.log(data.message);
							fetchQueueData();
					})
					.catch(error => console.error('Error adding client to queue:', error));
			}
	});
});

function fetchQueueData() {
	fetch('http://localhost:8000/queue/queue')
			.then(response => response.json())
			.then(data => {
					const tableBody = document.querySelector('#queue-table-body');
					tableBody.innerHTML = '';  // Clear existing rows

					data.forEach(item => {
							const row = document.createElement('tr');
							row.innerHTML = `
									<td>${item.name}</td>
									<td>
											<select class="status-dropdown">
													<option value="Pending">Pending</option>
													<option value="In Process">In Process</option>
													<option value="Completed">Completed</option>
											</select>
									</td>
									<td>
											<select class="service-dropdown">
													<option value="Select Service">Select Service</option>
													<option value="Oil Change" data-time="15">Oil Change</option>
													<option value="Tire Rotation" data-time="20">Tire Rotation</option>
													<option value="Brake Inspection" data-time="30">Brake Inspection</option>
											</select>
									</td>
									<td class="timer-cell">00:00</td>
									<td>
											<button class="update-button">Update</button>
									</td>
									<td>
											<button class="delete-button">Delete</button>
									</td>
							`;
							tableBody.appendChild(row);
					});

					document.querySelectorAll('.update-button').forEach((button, index) => {
							button.addEventListener('click', () => {
									const statusDropdown = tableBody.rows[index].querySelector('.status-dropdown');
									const serviceDropdown = tableBody.rows[index].querySelector('.service-dropdown');
									const timerCell = tableBody.rows[index].querySelector('.timer-cell');

									if (statusDropdown.value === 'In Process') {
											const selectedOption = serviceDropdown.options[serviceDropdown.selectedIndex];
											const time = selectedOption.getAttribute('data-time');
											if (time) {
													timerCell.innerText = `00:${time}`;
													startTimer(timerCell, time);
											}
									}

									if (statusDropdown.value === 'Completed') {
											const clientName = tableBody.rows[index].querySelector('td').innerText;
											fetch(`http://localhost:8000/queue/${clientName}`, {
													method: 'DELETE'
											})
											.then(response => {
													if (response.ok) {
															return response.json();
													}
													throw new Error('Network response was not ok.');
											})
											.then(data => {
													console.log(data.message);
													// Refresh the queue data
													fetchQueueData();
											})
											.catch(error => console.error('Error deleting client from queue:', error));
									}
							});
					});

					document.querySelectorAll('.delete-button').forEach((button, index) => {
							button.addEventListener('click', () => {
									const clientName = tableBody.rows[index].querySelector('td').innerText;
									fetch(`http://localhost:8000/queue/${clientName}`, {
											method: 'DELETE'
									})
									.then(response => {
											if (response.ok) {
													return response.json();
											}
											throw new Error('Network response was not ok.');
									})
									.then(data => {
											console.log(data.message);
											// Refresh the queue data
											fetchQueueData();
									})
									.catch(error => console.error('Error deleting client from queue:', error));
							});
					});
			})
			.catch(error => console.error('Error fetching queue data:', error));
}

function startTimer(cell, minutes) {
	let time = minutes * 60;
	const interval = setInterval(() => {
			const mins = Math.floor(time / 60);
			const secs = time % 60;
			cell.innerText = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
			time--;

			if (time < 0) {
					clearInterval(interval);
					cell.innerText = 'Completed';
			}
	}, 1000);
}


document.addEventListener('DOMContentLoaded', function() {
	var sidebar = document.querySelector('.sidebar');
	var button = document.querySelector('.minimize-button');
	var minImg = document.querySelector('.minimize-button-img');
	var maxImg = document.querySelector('.maximize-button-img');

	button.addEventListener('click', function() {
			sidebar.classList.toggle('minimized');

			if (sidebar.classList.contains('minimized')) {
					minImg.style.display = 'none';
					maxImg.style.display = 'block';
			} else {
					minImg.style.display = 'block';
					maxImg.style.display = 'none';
			}
	});

	document.getElementById('add-client-button').addEventListener('click', function() {
			const clientName = document.getElementById('client-name').value;
			if (clientName) {
					fetch(`http://localhost:8000/queue/add`, {
							method: 'POST',
							headers: {
									'Content-Type': 'application/json'
							},
							body: JSON.stringify({ name: clientName })
					})
					.then(response => response.json())
					.then(data => {
							console.log(data.message);
							fetchQueueData();
					})
					.catch(error => console.error('Error adding client to queue:', error));
			}
	});
});