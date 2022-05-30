/**
 * Scrapes the website for the titles of the kdrama
 *
 * @author Kayak
 * @version 1.0
 */

const axios = require('axios'); // HTTP request library
const cheerio = require('cheerio'); // web scraping library

const getTitles = async () => {
  try {
    const response = await axios.get('https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top'); // makes an HTTP get request

    const html = response.data;

    const $ = cheerio.load(html); // result of request loaded here

    const titles = [];

    $('div > div.col-xs-9.row-cell.content > h6 > a:nth-child(1)').each((_idx, el) => {
      const title = $(el).text(); // el = current element
      titles.push(title);
    });

    return titles;
  } catch (error) {
    throw error;
  }
};

getTitles().then((titles) => console.log(titles));
