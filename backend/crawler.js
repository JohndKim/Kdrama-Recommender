const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto('https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top&page=1');

  while (await page.$('ul > li.page-item.next > a')) {
    await page.click('ul > li.page-item.next > a');
  }
})();
// <a class="page-link" href="/search?adv=titles&amp;ty=68&amp;co=3&amp;st=3&amp;so=top&amp;page=2"></a>
// #content > div > div.container-fluid > div > div.col-lg-8.col-md-8 > div > ul > li.page-item.next > a
