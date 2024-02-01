window.addEventListener('DOMContentLoaded', function () {
  const traduction = document.querySelector('#hello');
  async function fetchData (url) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);

    traduction.textContent = data.hello;
  }

  fetchData('https://hellosalut.stefanbohacek.dev/?lang=fr');
});
