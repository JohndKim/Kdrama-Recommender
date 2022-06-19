function searchTitles(titles) {
  var input, filter, count, title_list, item, title;
  input = document.getElementById('user_input');
  filter = input.value.toUpperCase().trim();
  count = 0;
  title_list = document.getElementById('list');
  title_list.innerHTML = '';

  if (filter.length <= 2) {
    return;
  }

  for (const element of titles) {
    if (element.toUpperCase().indexOf(filter) > -1) {
      item = document.createElement('li');
      item.classList.add('k-title');

      if (count == 0) item.classList.add('rounded-top');
      if (count == 4) item.classList.add('rounded-bottom');

      title = document.createTextNode(element);

      item.appendChild(title);
      // autocomplete function
      item.setAttribute('onclick', 'select(this)');
      title_list.append(item);
      count++;
    }

    if (count == 5) break;
  }
  if (count > 1) item.classList.add('rounded-bottom');
  if (count == 1) item.classList.add('round-boi');
}

function select(element) {
  // gets the kdrama name from the list
  let selectUserData = element.textContent;
  const form = document.getElementById('form');
  const searchWrapper = document.querySelector('.searchbar');
  const inputBox = searchWrapper.querySelector('input');
  const searchResult = searchWrapper.querySelector('#list');
  inputBox.value = selectUserData; // pass title into search bar

  // clicking a result will submit the form
  searchResult.onclick = () => {
    form.submit();
  };
}
