const API_URL = '/genword';

let jsbtn = document.getElementById('js-render-btn');

jsbtn.addEventListener("click", () => {
    fetch(API_URL)
    .then(res => res.json())
    .then(data => {
        console.log(data);
        if (document.getElementById('js-val')){
            document.getElementById('js-val').innerText = 'product: ' + data.keyword
        } else {
            let node = document.createElement('p'); // Create a <p> node
            node.setAttribute("id", "js-val");
            let textnode = document.createTextNode('product: ' + data.keyword);
            node.appendChild(textnode);
            document.getElementById("main").appendChild(node);
        }
    })
});