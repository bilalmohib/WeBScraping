# Web Scraping With Google Sheets

There are four main methods used in google sheets to scrap the data
- =importhtml()
- =importdata()
- =importfeed()
- =importxml()

## Using =importhtml()
We can Scrap the Data of a website using below configurations.

### To import Particular Table Data from a website for Example Wikipedia
To import the data from wikipedia table for example.this table

![Wikipedia table](https://raw.githubusercontent.com/Muhammad-Bilal-7896/WeBScraping/crystal/GoogleSheetsWebScraping/Resources/WikipediaTabletoBeScrapped.png "wikipedia table")

Now to know which table it is type the following js command in the console of the page.By opening console of the browser.
```js
 var i = 1; [].forEach.call(document.querySelectorAll('table'), function(x) { console.log(i++, x); });
``` 

It will return all the tables in the page like this.

![Website Tables](https://raw.githubusercontent.com/Muhammad-Bilal-7896/WeBScraping/crystal/GoogleSheetsWebScraping/Resources/TablesList.png "Website Tables")

Now to know which table number we want to get just hover on the table classes names and the table you want will get highlighted as shown below:-

![Highlighted Tables](https://raw.githubusercontent.com/Muhammad-Bilal-7896/WeBScraping/crystal/GoogleSheetsWebScraping/Resources/highlightedtable.png "Highlighted Tables")

So now We know that our table number is = 4

So our command will be something like this in importhtml it takes three arguments.
- The first one is the url from where you want the data.
- Second one is the html tag name
- The third one is the (table) in our case but in general tag number

So the command will become something like this.

```bash
=importhtml("https://en.wikipedia.org/wiki/Lists_of_earthquakes",'table',4)
```
Enter the command here like this

<img src="https://raw.githubusercontent.com/Muhammad-Bilal-7896/WeBScraping/crystal/GoogleSheetsWebScraping/Resources/QueryTable.png" />

This command will give all the table data of table 4 in the specified url so this output will be shown

![Output Data in Google Sheet](https://raw.githubusercontent.com/Muhammad-Bilal-7896/WeBScraping/crystal/GoogleSheetsWebScraping/Resources/TableOutput.png "Output Data in Google Sheet")
