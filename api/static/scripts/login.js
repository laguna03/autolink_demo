document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch("http://localhost:8080/user/token", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.detail) });
        }
        return response.json();
    })
    .then(data => {
        if (data.access_token) {
            console.log('Login successful, token received:', data.access_token);
            document.getElementById('message').textContent = 'Login successful!';
            localStorage.setItem('token', data.access_token);
            window.location.href = '/home';  // Redirige a la página de inicio
        } else {
            document.getElementById('message').textContent = 'Username or password incorrect. Try again.';
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = `Error: ${error.message}`;
        console.error('Error:', error);
    });
});
