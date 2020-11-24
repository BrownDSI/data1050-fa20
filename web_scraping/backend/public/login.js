const form = document.getElementById('login-form');
const API_URL = window.location.href

document.getElementById('name').select();

form.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log('form successfully submitted');
    const formData = new FormData(form);
    const username = formData.get('name').trim();
    const password = formData.get('password').trim();

    const login = {
        username,
        password
    };
    fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify(login),
        headers: {
            'content-type': 'application/json'
        }
    }).then(res => res.json())
    .then(data => {
        if (!data.isValid) {
            console.log('invalid username and password')
            let node = document.createElement('p'); // Create a <p> node

            // invalid username
            if (!document.getElementById('invalid')){
                node.setAttribute('id', 'invalid');
                let textnode = document.createTextNode('invalid username or password');
                node.appendChild(textnode);
                form.appendChild(node);
            }
        } else {
            window.location.href = '/hidden-page';
        }
    })
});