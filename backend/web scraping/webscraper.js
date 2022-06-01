/**
 * Scrapes the website for the titles of the kdrama
 *
 * @author Kayak
 * @author Prof.K
 * @version 1.0
 */

const axios = require('axios'); // HTTP request library
const cheerio = require('cheerio'); // web scraping library
const URL = 'https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top&page=1'; // kdrama site url
const kdramaSites = []; // a list of all kdrama sites (ranks in ascending order, e.g. 1 -> 10)

/**
 * Function that updates the page URL to go to the next page
 *
 * @param {*} URL
 * @returns
 */
function updatePageURL(URL) {
  const regexThreeDigits = new RegExp('\\d{3}'); // regex for three digits
  const regexTwoDigits = new RegExp('\\d{2}'); // regex for two digits
  const regexOneDigit = new RegExp('\\d{1}'); // regex for one digit

  var threeDigits = URL.slice(URL.length - 3); // three digit page num
  var twoDigits = URL.slice(URL.length - 2); // two digit page num
  var oneDigit = URL.slice(URL.length - 1); // one digit page num

  // 100-999 case
  if (regexThreeDigits.test(threeDigits)) {
    threeDigits++;
    return URL.slice(0, URL.length - 3) + threeDigits;
  }

  // 10-99 case
  if (regexTwoDigits.test(twoDigits)) {
    twoDigits++;
    return URL.slice(0, URL.length - 2) + twoDigits;
  }

  // 1-9 case
  if (regexOneDigit.test(oneDigit)) {
    oneDigit++;
    return URL.slice(0, URL.length - 1) + oneDigit;
  }
}

/**
 * gets a kdrama site url in a page
 *
 * @param {*} URL url
 * @returns all kdrama sites on a page (20)
 */
const getKdramaSites = async (URL) => {
  try {
    const response = await axios.get(URL); // makes an HTTP get request to kdrama site

    const html = response.data;

    const $ = cheerio.load(html); // result of request loaded here

    // searches for elements with this jquery selector and takes the text and pushes it into 'kdramaSites'
    $('div > div.col-xs-9.row-cell.content > h6 > a:nth-child(1)').each((_idx, el) => {
      const kdramaSite = 'https://mydramalist.com' + $(el).attr('href'); // gets link
      kdramaSites.push(kdramaSite); // adds to kdrama list
    });

    return kdramaSites;
  } catch (error) {
    throw error;
  }
};

/**
 * Gets all the URLs of the kdramas on mydramalist
 *
 * @param {*} URL url
 * @returns nothing
 */
const getAllURLs = async (URL) => {
  const resultBefore = kdramaSites.length; // length of list BEFORE adding
  const result = await getKdramaSites(URL, kdramaSites); // length of list AFTER adding
  const addedDramas = result.length - resultBefore; // difference between the two (should be 20)

  // this only happens when it reaches the end of all kdramas on mydramalist
  if (addedDramas != 20) {
    console.log(kdramaSites);
    return kdramaSites;
  }

  // recursively calls this to continue adding to the list
  return getAllURLs(updatePageURL(URL));
};

console.log(getAllURLs(URL));
