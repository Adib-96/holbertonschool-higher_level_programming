window.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const parentUl = document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const liChild = document.createElement('li');
    liChild.textContent = 'Item';
    parentUl.appendChild(liChild);
  });
});
