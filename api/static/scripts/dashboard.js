document.addEventListener('DOMContentLoaded', () => {
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
													<select class="status-dropdown" data-name="${item.name}">
															<option value="">...</option>
															<option value="In Process">In Process</option>
															<option value="Pending">Pending</option>
															<option value="Completed">Completed</option>
													</select>
											</td>
											<td>
													<button class="update-button" data-name="${item.name}">Update</button>
											</td>
									`;
									tableBody.appendChild(row);
							});

							// Add event listeners to update buttons
							const updateButtons = document.querySelectorAll('.update-button');
							updateButtons.forEach(button => {
									button.addEventListener('click', function() {
											const itemName = this.getAttribute('data-name');
											const dropdown = document.querySelector(`.status-dropdown[data-name="${itemName}"]`);
											const selectedValue = dropdown.value;

											if (selectedValue === 'Completed') {
													fetch(`http://localhost:8000/queue/${itemName}`, {
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
													.catch(error => console.error('Error deleting item:', error));
											} else {
													// Lógica para manejar otros estados
													console.log(`Status for ${itemName} updated to ${selectedValue}`);
													// Aquí puedes agregar lógica para manejar otros estados
													// Por ejemplo, actualizar el estado en el servidor
													// Y luego refrescar los datos del queue
											}
									});
							});
					})
					.catch(error => console.error('Error fetching queue data:', error));
	}

	// Fetch queue data initially
	fetchQueueData();
});


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
});