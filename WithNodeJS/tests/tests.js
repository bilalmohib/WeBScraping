const { By, Key, Builder } = require("selenium-webdriver");
require("chromedriver");
const puppeteer = require('puppeteer');


async function example() {
    var searchString = "Automation testing with Selenium and JavaScript";

    //To wait for browser to build and launch properly
    let driver = await new Builder().forBrowser("chrome").build();

    //To fetch http://google.com from the browser with our code.
    await driver.get("http://google.com");

    //To send a search query by passing the value in searchString.
    await driver.findElement(By.name("q")).sendKeys(searchString, Key.RETURN);
    // let element = await driver.findElement(By.id("input"));
    //  console.log("Element is equal to : ",element)
    //  driver.sleep(2000);

    //Verify the page title and print it
    var title = await driver.getTitle();
    console.log('Title is:', title);

    // //It is always a safe practice to quit the browser after execution
    await driver.quit();
}

async function check() {
    const browser = await puppeteer.launch({ headless: true })
    const page = await browser.newPage()
    await page.goto('https://github.com/login')
    await page.type('#login_field', 'Muhammad-Bilal-7896')
    await page.type('#password', "123321123BiLaL")
    await page.click('[name="commit"]')
    await page.waitForNavigation()
    await page.screenshot({ path: screenshot })
    browser.close()
    console.log('See screenshot: ' + screenshot)
}

//example()

check()
