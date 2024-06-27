document.addEventListener('DOMContentLoaded', () => {
  fetch('http://localhost:8000/queue/queue')
      .then(response => response.json())
      .then(data => {
          const tableBody = document.querySelector('#queue-table-body');
          tableBody.innerHTML = '';  // Clear existing rows

          data.forEach(item => {
              const row = document.createElement('tr');
              row.innerHTML = `
                  <td>${item.name}</td>
              `;
              tableBody.appendChild(row);
          });
      })
      .catch(error => console.error('Error fetching queue data:', error));
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