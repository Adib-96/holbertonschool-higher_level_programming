window.addEventListener('DOMContentLoaded', function() {
  const readHeader = document.querySelector('#red_header');
  const header = document.querySelector('header');

  readHeader.addEventListener('click', function() {
    header.setAttribute('class', 'red');
  });
});
