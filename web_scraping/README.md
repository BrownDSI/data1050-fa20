# Web scraping

To scrape, make sure you've installed selenium:

## example scraper ##

``` pip install selenium ```

in order to ensure that this runs please download your local version
of chromedriver from https://chromedriver.chromium.org/downloads and add it
to your local directory (in the local case we are using chromedriver86)

## shopping scraper ##

the shopping scraper is slightly more involved, and requires the user
to download additionaly dependencies

for the shopping-scraper example, please look into the mongodb atlas program
and install the necessary requiremnets

whats needed:
- ` $ pip install pymongo `
- look deeper into mongodb atlas and create an account at https://www.mongodb.com/cloud/atlas 
	from there, adjust lines 38 to 45 to work with your database
	(note, you will also need to create a dotenv file with the 
	necessary requirements using ` pip install -U python-dotenv `
	and then adding the respective password and database_name to
	a dotenv file to get this running)  


#### backend

the backend folder shows the code for what is necessary to properly
read and write to a server - while this may seem confusing feel free
to give this a look for examples on what a RESTful api may look lie
