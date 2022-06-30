// whenever a user clicks on the site, it checks if it clicked the dropdown button
document.addEventListener('click', (e) => {
  const isDropdownButton = e.target.matches('[data-dropdown-button]');
  // if we aren't in a drop down, ignore
  if (!isDropdownButton && e.target.closest('[data-dropdown]') != null) return;
  // if user clicked on the dropdown
  let currentDropdown;
  if (isDropdownButton) {
    currentDropdown = e.target.closest('[data-dropdown]');
    currentDropdown.classList.toggle('active');
  }

  // closes all dropdowns already opened except the one just opened
  document.querySelectorAll('[data-dropdown].active').forEach((dropdown) => {
    if (dropdown === currentDropdown) return;
    dropdown.classList.remove('active');
  });
});

// function searchFunction() {
//   // Declare variables
//   var input, filter, ul, li, a, i, txtValue;
//   input = document.getElementById('user_input');
//   filter = input.value.toUpperCase().trim();
//   ul = document.getElementById('list');
//   li = ul.getElementsByTagName('li');

//   // if there is no input, show nothing
//   const inputDisplay = input.value.length > 1 ? 'list-item' : 'none';
//   ul.style.display = inputDisplay;

//   // Loop through all list items, and hide those who don't match the search query
//   for (i = 0; i < li.length; i++) {
//     a = li[i].getElementsByTagName('a')[0];
//     txtValue = a.textContent || a.innerText;
//     if (txtValue.toUpperCase().indexOf(filter) > -1) {
//       li[i].style.display = 'list-item';
//     } else {
//       li[i].style.display = 'none';
//     }
//   }

//   let num_of_matches = get_match_num(li);
//   let max_entries_shown = 5;

//   remove_rounded_corners(li);
//   limit_searches_shown(li, num_of_matches, max_entries_shown);
// }

// // gets number of search results
// function get_match_num(li) {
//   let num_of_matches = 0;
//   for (const element of li) {
//     if (element.style.display == 'list-item') num_of_matches++;
//   }
//   return num_of_matches;
// }

// function remove_rounded_corners(li) {
//   for (const element of li) {
//     let a = element.getElementsByTagName('a')[0];
//     if (a.classList.contains('rounded-top')) a.classList.remove('rounded-top');
//     if (a.classList.contains('rounded-bottom')) a.classList.remove('rounded-bottom');
//     if (a.classList.contains('round-boi')) a.classList.remove('round-boi');
//   }
// }

// // limits the number of search results shown
// function limit_searches_shown(li, num_of_matches, limit) {
//   let count = 0;
//   for (const element of li) {
//     let a = element.getElementsByTagName('a')[0];
//     // adds rounded corners to the top
//     if (num_of_matches == 1 && element.style.display == 'list-item') {
//       a.classList.add('round-boi');
//       break;
//     }
//     if (count == 0 && element.style.display == 'list-item') a.classList.add('rounded-top');
//     if (element.style.display == 'list-item') count++;
//     if (count > limit && element.style.display == 'list-item') element.style.display = 'none';
//     if (count == limit || num_of_matches == count) a.classList.add('rounded-bottom');
//   }
// }
