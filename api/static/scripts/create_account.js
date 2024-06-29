document.getElementById('create-account-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:8080/user/create_account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "User created successfully") {
            window.location.href = '/login';
        } else {
            document.getElementById('message').textContent = 'Error creating account. Try again.';
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Error creating account. Try again.';
        console.error('Error:', error);
    });
});
