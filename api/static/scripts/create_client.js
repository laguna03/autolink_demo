document.getElementById('create-client-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const clientData = {
        client_id: uuidv4(),
        first_name: document.getElementById('first-name').value,
        last_name: document.getElementById('last-name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone-number').value
    };

    const vehicleData = {
        vehicle_id: Math.floor(Math.random() * 100000),
        client_id: clientData.client_id,
        license_plate: document.getElementById('license-plate').value,
        vin_number: document.getElementById('vin-number').value,
        make: document.getElementById('make').value,
        mileage: parseInt(document.getElementById('mileage').value),
        model: document.getElementById('model').value,
        year: parseInt(document.getElementById('year').value)
    };

    const response = await fetch('http://localhost:8080/create/create-client', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ client_data: clientData, vehicle_data: vehicleData })
    });

    const result = await response.json();
    if (response.ok) {
        alert(result.message);
    } else {
        alert(`Error: ${result.detail}`);
    }
})
.then(response => response.json())
.then(data => {
    if (data.status === 'success') {
        window.location.href = `/static/html/Success.html?client_id=${data.client_id}&vehicle_id=${data.vehicle_id}`;
    } else {
        alert(data.message);
    }
})

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0,
              v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}
