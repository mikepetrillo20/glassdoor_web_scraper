# GlassDoor Web Scraper

This is a web scraper project I am currently working on. 

### Current Features

* Scrape Name, Title, Location, Salary, and Days Active data for Software Engineer positions near Raleigh, NC.
* Currently only scrapes first page. Adding multiple page functionality soon.


### Planned Features

* Write the scraped data to a csv file
* Multiple Page scraping
* Ability to change search criteria
* Automatically remove duplicates from file

### Why I am building this

I am graduating from college at the end of 2020. I scraper for every popular job board that feeds into a sql database that I can then query to access potential jobs I would be interested in.

This is the first step to that project.

### Problems and Solutions

**Problem**: When initially scraping sets of data, some values dont exist. For example: Some companies dont have a glassdoor estimate salary, this is bringing up errors.
**Solution**: I plan to setup a few try except blocks that will help me continue scraping the data I need.

