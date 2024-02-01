const character = document.querySelector('#character');

async function fetchingData () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  character.textContent = data.name;
}

fetchingData();
