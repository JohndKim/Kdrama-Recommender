// THIS IS ACTUALLY NOT NECESSARY

const puppeteer = require('puppeteer'); // moves-through-the-site-for-you library

(async () => {
    const browser = await puppeteer.launch({ headless: false }); // launches site
    const page = await browser.newPage(); // website page
    await page.goto('https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top&page=1'); // goes to kdrama page

    await page.waitForSelector('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div');
    let urls = await page.$$eval('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div', (links) => {
        // Make sure the book to be scraped is in stock
        // Extract the links from the data
        links = links.map((el) => el.querySelector('h6 > a').href);
        return links;
    });
    console.log(urls);
    // let urls = await page.$$eval('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div', (links) => {
    //   // Extract the links from the data
    //   links = links.map((el) => el.querySelector('h6 > a').href);
    //   return links;
    // });

    // console.log(urls);

    //   while (await page.$('ul.pagination > li.page-item.next > a')) {
    //     await page.click('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li:nth-child(6) > a');
    //     await page.waitForTimeout(5000);
    //   }
})();

console.log('next page');

// <a class="page-link" href="/search?adv=titles&amp;ty=68&amp;co=3&amp;st=3&amp;so=top&amp;page=2"></a>
// #content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li.page-item.next > a
// document.querySelector("#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li.page-item.next > a")
// #content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li.page-item.next > a

// const puppeteer = require('puppeteer'); // moves-through-the-site-for-you library

// (async () => {
//   const browser = await puppeteer.launch({ headless: false }); // launches site
//   const page = await browser.newPage(); // website page
//   await page.goto('https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top&page=1'); // goes to kdrama page

//   let urls = await page.$$eval('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div', (links) => {
//     // Extract the links from the data
//     links = links.map((el) => el.querySelector('h6 > a').href);
//     return links;
//   });

//   console.log(urls);
//   console.log('next page');

//   //   while (await page.$('ul.pagination > li.page-item.next > a')) {
//   //     await page.click('#content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li:nth-child(6) > a');
//   //     await page.waitForTimeout(5000);
//   //   }
// })();
