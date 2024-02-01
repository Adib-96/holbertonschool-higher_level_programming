window.addEventListener('DOMContentLoaded', function () {
  const toggleHeader = document.querySelector('#toggle_header');
  const header = document.querySelector('header');

  toggleHeader.addEventListener('click', function () {
    if (header.getAttribute('class') === 'green') {
      header.setAttribute('class', 'red');
    } else {
      header.setAttribute('class', 'green');
    }
  });
});
