document.getElementById('create-account-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    fetch('http://localhost:8000/create-account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, role })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = 'Cuenta creada exitosamente!';
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Error al crear la cuenta.';
        console.error('Error:', error);
    });
});
