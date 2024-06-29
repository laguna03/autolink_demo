document.getElementById('clientForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const clientData = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        email: document.getElementById('email').value,
        dob: document.getElementById('dob').value,
        phoneNumber: document.getElementById('phoneNumber').value,
        licensePlate: document.getElementById('licensePlate').value,
        vinNumber: document.getElementById('vinNumber').value,
        make: document.getElementById('make').value,
        mileage: document.getElementById('mileage').value,
        model: document.getElementById('model').value,
        year: document.getElementById('year').value,
        appointmentTime: document.getElementById('appointmentTime').value
    };

    try {
        const response = await fetch('/api/clients', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(clientData)
        });

        if (response.ok) {
            alert('Client added to queue');
        } else {
            alert('Failed to add client');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error adding client');
    }
});
