# PCPartScraper  
#### Author: Jeet Chugh  

###### PCPartScraper is a simple, yet powerful pcpartpicker.com WebScraper that extracts Data from Part URL's.

**Features:**  

  - Search for Parts from String Queries
  - View: **name, type, sale_link, price, specifications, url, rating, reviews, queries**
  - Install easily with pip
  - Lightweight, only uses Requests and BS4 BeautifulSoup
#### [Github Link](https://github.com/Jeet-Chugh/pcpartscraper) | [PyPi Link](https://pypi.org/project/pcpartscraper/) | [Example Code Link](https://raw.githubusercontent.com/Jeet-Chugh/pcpartscraper/master/example.py)  

  Quick and Easy Installation via PIP: `pip install pcpartscraper`  

Import Statement:  ``from pcpartscraper.scraper import Part,Query``  

Dependencies: *bs4, requests, python 3*  

#### Code License: MIT  

# Documentation  

###### Documentation is split into 2 sections. First is the 'Part' Class and second is the 'Query' Function.  

---  

#### 'Part' Class:  

Part takes in an input of a URL as a string, and has many methods that return specific chunks of data.  

Example1 Part:    *'/product/jxJwrH/intel-cpu-bx80623i52400' is a WD Blue 1tb Hard drive*  

Example2 Part:   *'/product/jxJwrH/intel-cpu-bx80623i52400'* is an Intel i5-2400 Proccesor  

**Import:**  

``from pcpartscraper.scraper import Part``  

**Instantiation:**  

``part1 = Part('/product/jxJwrH/intel-cpu-bx80623i52400') # Takes in url string (no .com)``  

``part2 = Part('/product/jxJwrH/intel-cpu-bx80623i52400') # Organize different parts in variables``  

#### **'Part' Methods:**  

##### methods return None if encountering Errors  

---  

``Part('url').name()``  

returns a string containing the name of the part.  

 (Western Digital 1 TB 3.5" Hard Drive, etc.)  

---  

``Part('url').type()``  

returns a string containing the type of the part  

(Storage, Memory, Video Card, CPU Cooler, etc.)  

---  

`Part('url').amazon_link()`  

returns a string containing the URL to the amazon listing for the product, if available. returns None if unavailable.  

('https://www.amazon.com/dp/B004EBUXIA?tag=pcpapi-20&linkCode=ogi&th=1&psc=1', etc)  

---  

`Part('url').price()`  

returns a float value for the cheapest price available for the part.  

(34.99, 93.01, 45.62, etc.)  

---  

`Part('url').advanced_specs()`  

returns a dictionary containing key/value pairs that correspond to the "specifications" sidebar for the part  

Example Dictionary:`{'model':'Intel','Core Clock':'3.2Ghz','TDP':'95W','Socket':'LGA1155'}`  

---  

`Part('url').url()`  

returns a string containing the runnable link for the part.  

(https://pcpartpicker.com/product/jxJwrH/intel-cpu-bx80623i52400, etc.)  

---  

`Part('url').rating()`  

returns a float value containing the review rating score, out of 5, for the part.  

(3.6, 4.7, 1.3, 5.0, etc.)  

---  

`Part('url').reviews(results=1)`  

inputs = results. The number of reviews that you want to pull from the part page.  

returns a list containing x amount of text-reviews for a part. Reviews are from the part page, and are unfiltered.  

(['really fast and good looking!','runs a little hot, but runs games extremely well!','Not good, waste of money.'], etc.)  

---  

#### 'Query' Function:  

Query takes in (url as a string), (results as an int), (exclude_laptops as a bool), (pages as an int)

**Import:**  

``from pcpartscraper.scraper import Query``  

**Instantiation:**  

``result_list = Query(search_term='ryzen 5',results=1,exclude_laptops=True,pages=1)``  

#### **'Query' Inputs:**  

##### returns a list containing 'Part' classes pertaining to results.  

---  

``Query(search_term='')``  

search_term is the keywords for finding a part through query. Main "searching" input.  

 (Western Digital , G-SKill, Cooler Master Hyper, 8gb RAM, etc.)  

---  

``Query(results=3)``  

results is the number of results that you want to be returned in the returning list  

The default value for result is 3, and the max is 20. > Results = More time usage  

 (6, 11, 3, 5, 1, 20, 13, etc.)  

---  

``Query(exclude_laptops='search for a part')``  

Because of the laptop update to pcpartpicker.com, searching for parts often only result in laptops  

exclude_laptops will ensure that no elements in the returning list contain instances of laptops.  

The default value for exclude_laptops is True  

 (True, False)  

---

``Query(pages=1)``  

Searching for popular parts ends up with many pages to navigate through  

pages is the number of pages that you want to span across. If 5, it will navigate the (results) # of top results for (pages)

The default value for pages is 1, as it greatly increases script execution timing.

 (True, False)  

---    

`Query('ryzen 5',3,True,1)`  

This example would return a list containing 3 'Part' objects for the top 3 searches on the first page pertaining to 'ryzen',excluding laptops.  

A return would look like this  

`print(Query('ryzen',3,True,1))` --> [Part Object at x,Part Object at y,Part Object at z]  

---  

Thank you for reading the documentation. If you need an example using all these methods, go to [link]  


If you have issues, report them to the github project link.
