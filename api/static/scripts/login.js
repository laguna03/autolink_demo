document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.access_token) {
            document.getElementById('message').textContent = 'Login exitoso!';
            localStorage.setItem('token', data.access_token);
            // Redirigir al dashboard u otra página
        } else {
            document.getElementById('message').textContent = 'Nombre de usuario o contraseña incorrectos';
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Error al iniciar sesión.';
        console.error('Error:', error);
    });
});
