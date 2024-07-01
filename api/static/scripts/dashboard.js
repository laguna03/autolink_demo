document.addEventListener('DOMContentLoaded', () => {
	fetchQueueData();

	document.getElementById('add-client-button').addEventListener('click', function() {
			const clientName = document.getElementById('client-name').value;
			if (clientName) {
					fetch(`http://localhost:8080/queue/queue/add`, {
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
	fetch('http://localhost:8080/queue/queue')
			.then(response => response.json())
			.then(data => {
					if (!data.queue || !data.ongoingServices) {
							throw new Error('Invalid response structure');
					}

					const queueTableBody = document.querySelector('#queue-table-body');
					const ongoingServicesTableBody = document.querySelector('#ongoing-services-table-body');
					queueTableBody.innerHTML = '';  // Clear existing rows
					ongoingServicesTableBody.innerHTML = '';  // Clear existing rows

					// Populate Queue Table
					data.queue.forEach(item => {
							const row = document.createElement('tr');
							row.innerHTML = `
									<td>${item.name}</td>
									<td>${item.model}</td>
									<td>${item.license_plate}</td>
									<td>
											<button class="start-service-button">Start Service</button>
									</td>
							`;
							queueTableBody.appendChild(row);
					});

					// Populate Ongoing Services Table
					data.ongoingServices.forEach(item => {
							const row = document.createElement('tr');
							row.innerHTML = `
									<td>${item.name}</td>
									<td>${item.model}</td>
									<td>${item.license_plate}</td>
									<td>
											<select class="service-dropdown">
													<option value="Select Service">Select Service</option>
													<option value="Oil Change" data-time="35">Oil Change</option>
													<option value="Front Train" data-time="90">Front Train</option>
													<option value="ABS" data-time="30">ABS</option>
													<option value="Check Engine" data-time="40">Check Engine</option>
													<option value="Grace Time" data-time="15">Grace Time</option>
											</select>
									</td>
									<td class="timer-cell">00:00</td>
									<td>
											<select class="status-dropdown">
													<option value="Pending">Pending</option>
													<option value="In Process">In Process</option>
													<option value="Completed">Completed</option>
											</select>
									</td>
									<td>
											<button class="update-button">Update</button>
									</td>
							`;
							ongoingServicesTableBody.appendChild(row);
					});

					document.querySelectorAll('.start-service-button').forEach((button, index) => {
							button.addEventListener('click', () => {
									const row = queueTableBody.rows[index];
									const clientName = row.querySelector('td').innerText;
									const model = row.cells[1].innerText;
									const license_plate = row.cells[2].innerText;
									fetch(`http://localhost:8080/queue/start_service`, {
											method: 'POST',
											headers: {
													'Content-Type': 'application/json'
											},
											body: JSON.stringify({ name: clientName, model: model, license_plate: license_plate })
									})
									.then(response => response.json())
									.then(data => {
											console.log(data.message);
											fetchQueueData();
									})
									.catch(error => console.error('Error starting service:', error));
							});
					});

					document.querySelectorAll('.service-dropdown').forEach((dropdown, index) => {
							dropdown.addEventListener('change', () => {
									const selectedOption = dropdown.options[dropdown.selectedIndex];
									const time = selectedOption.getAttribute('data-time');
									const timerCell = ongoingServicesTableBody.rows[index].querySelector('.timer-cell');
									if (time) {
											timerCell.innerText = `00:${time}`;
									}
							});
					});

					document.querySelectorAll('.update-button').forEach((button, index) => {
							button.addEventListener('click', () => {
									const statusDropdown = ongoingServicesTableBody.rows[index].querySelector('.status-dropdown');
									const serviceDropdown = ongoingServicesTableBody.rows[index].querySelector('.service-dropdown');
									const timerCell = ongoingServicesTableBody.rows[index].querySelector('.timer-cell');

									if (statusDropdown.value === 'In Process') {
											const selectedOption = serviceDropdown.options[serviceDropdown.selectedIndex];
											const time = selectedOption.getAttribute('data-time');
											if (time) {
													timerCell.innerText = `00:${time}`;
													startTimer(timerCell, time);
											}
									}

									if (statusDropdown.value === 'Completed') {
											const clientName = ongoingServicesTableBody.rows[index].querySelector('td').innerText;
											fetch(`http://localhost:8080/queue/queue/${clientName}`, {
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
