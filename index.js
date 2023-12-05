const select = document.getElementById('fruits');
const add = document.getElementById('add-fruit');

fetch("http://localhost:8882/fruits")
.then(response => response.json())
.then(jsonResponse => {
  jsonResponse.forEach(response => {
    let option = document.createElement('option');
    option.textContent = response;
    select.appendChild(option);
  })
})