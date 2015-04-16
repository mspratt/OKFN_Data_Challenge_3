# OKFN_Data_Challenge_3
Project to scrap UK spending data

This is a Python project to scrap and spider data.gov.uk
run the 

scrape_data_gov_publishers.py program.

The output is to data_gov_publisher_results.csv

Before I finish the program I need to ask several questions?
  1st is this what you are looking for?
  2nd what other data do you want?  (I haven't saved any of the dates/time stamps and someother elements yet)
  3rd is the CSV file in the "right" format, element titles, column sequence in the output line, etc?

The program does a lot of printing to the screen but that
is mostly for me to see how it is executing.

I stop processing after the first xxx publishers

Some publisher like the 
agri-food-and-biosciences-institute doesn't have the same json
format as the other publishers.  This publisher (its not the only one)  doesn't have a key "foi-web" which is a url to their site.

For now I'll just cooment out the line but latter I'll test for the presents of keys

air-accident-investigation-branch also has a unique structure for it's packets.  It doesn't have a 
"result"]["resources"][0]["url"] key.  Why?  The publisher points to this data package, but the json structure
for this publisher doesn( have the key...  I'll figure it out...

As a beginning Python programmer means also learning API, json, Git
and a few other "technical" tools.

This problem also justifies me dumping Windows for Lunix

