async function analyze() {
    const userData = document.getElementById('user_data').value;
    const response = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_data: [userData] })
    });
    const data = await response.json();
    document.getElementById('traits').innerText = JSON.stringify(data);
}

async function respond() {
    const prompt = document.getElementById('prompt').value;
    const response = await fetch('/respond', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, user_style: 'friendly' })
    });
    const data = await response.json();
    document.getElementById('response').innerText = data.response;
}
