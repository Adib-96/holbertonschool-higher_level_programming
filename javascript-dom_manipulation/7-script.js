const ulBox = document.querySelector('#list_movies');

async function fetchingData () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await response.json();

  let n = 0;
  while (n < data.results.length) {
    const liChild = document.createElement('li');
    liChild.textContent = data.results[n].title;
    ulBox.appendChild(liChild);
    n++;
  }
}

fetchingData();
