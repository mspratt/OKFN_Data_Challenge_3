# OKFN_Data_Challenge_3
Project to scrap UK spending data

This is a Python project to scrap and spider dtat.gov.uk
run the 
scrape_data_gov_publishers.py program.

The output is to data_gov_publisher_results.csv

Before I finish the program I need to ask several questions?
  1st is this what you are looking for?
  2nd what other data do you want?  (I haven't saved any of the dates and someother elements yet)
  3rd is the CSV file in the "right" format, element titles, sequence in the output line, etc?

The program does a lot of printing to the screen but that
is mostly for me to see how it is executing.

I stop processing after the first 25 publishers

Some publisher like the agri-food-and-biosciences-institute don't have the same json
format as the other publishers.  This publisher doen't have a key "foi-web" which is a url to their site.
For now I'll just cooment out the line but latter I'll test for the presents of keys


I'm a beginning Python programmer and had to learn the API, json, Git
and a few other "technical" tools.

This problem also justifies me dumping Windows for Lunix

