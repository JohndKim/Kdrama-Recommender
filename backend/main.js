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

const searchInput = document.querySelector('[kdrama-serach]');

searchInput.addEventListener('input', (e) => {
  const value = e.target.value;
});

const fs = require('fs');
const Papa = require('papaparse');

const csvFilePath = 'C:UsersJohn KimDesktopkdrama_data.csv';

// Function to read csv which returns a promise so you can do async / await.

const readCSV = async (filePath) => {
  const csvFile = fs.readFileSync(filePath);
  const csvData = csvFile.toString();
  return new Promise((resolve) => {
    Papa.parse(csvData, {
      header: true,
      complete: (results) => {
        console.log('Complete', results.data.length, 'records.');
        resolve(results.data);
      },
    });
  });
};

const test = async () => {
  let parsedData = await readCSV(csvFilePath);
};

test();

// function search_kdrama() {
//   let input = document.getElementById('userInput').value;
//   input = input.toLowerCase();
//   // this is where the python should come in or smth (see re_sys.py)
//   // search for matching kdramas:
// }
