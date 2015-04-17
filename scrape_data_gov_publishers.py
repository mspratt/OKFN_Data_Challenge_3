"""
scrape_data_gov_publishers.py

This program access the http://data.gov.uk/api/ in order to
scrap the list of publishers. the returned data is in json
format.

Using the names obtained from the publisher's
list we create a new url string by concatenating 
"http://data.gov.uk/api/3/action/organization_show?id="
with the publisher_name.

With this new query we then access the site again and save
the publsiher's data to new json file.
We read through the new json file on "packages in order to get the
title, id and name of the publication.



We then create the output file


"""


#*************************************************
#  Initialize
import sys, os, urllib3, json, html
#import data_gov_packets

# write to the csv file
outputfile = open("data_gov_publisher_results.csv", 'a')
printheader = 1  #true

#*********************   get the orgainsation list

url_0 = "http://data.gov.uk/api/3/action/organization_list"
http_0= urllib3.PoolManager()
page_returned_0 = http_0.request('GET', url_0)

#print("page returned=", page_returned_0)
#print("page status  =", page_returned_0.status)
#print("    ")


f = open("organization_list.json", 'wb')
f.write(page_returned_0.data)


with open('organization_list.json') as data_file_0:    
    organization_data = json.load(data_file_0)

f.close()
os.remove("organization_list.json")


# *******************  loop through publisher   ******
print("********   loop through publishers   ************")
cntr=0
for x in organization_data["result"] :
     #if cntr > 150:  # get only the first 25 publishers
         #break

     publisher_name = organization_data["result"][cntr]
     cntr += 1
     
     #**********  for testing  *************************
     #publisher_name = "2gether-nhs-foundation-trust"
     #publisher_name = "aberdeen-city-council"
     #publisher_name = "adur-district-council"
     #publisher_name = "agri-food-and-biosciences-institute"
     #publisher_name = "air-accident-investigation-branch"
     #***************************************************


     if cntr <= 1307:    #  to skip to a certain record
         continue


      
  
     #------------------------------------
     # these publishers have problems with
     # my code.... they point to a data set,
     # but once we access there is no data...
     #
     #  I thought there were only going to be a few
     #  if I had know I would have written the
     #  conditional that checks for this...

     """
     if publisher_name == "air-accident-investigation-branch":
          continue   
     if publisher_name == "animal-health-and-veterinary-laboratories-agency":
          continue   
     if publisher_name == "appointments-commission":
          continue
     if publisher_name == "architects-registration-board":
          continue
     if publisher_name == "british-film-institute":
          continue
     if publisher_name == "british-tourist-authority":
          continue
     if publisher_name == "businesslink":
          continue
     if publisher_name == "centre-for-ecology-hydrology":
          continue
     if publisher_name == "centre-for-environment-fisheries-aquaculture-science":
          continue
     if publisher_name == "charnwood-borough-council":
          continue
     if publisher_name == "chartered-institute-of-public-finance-and-accountancy":
          continue    
     if publisher_name == "collections-trust":
          continue    
     if publisher_name == "companies-investigation-branch":
          continue    
     if publisher_name == "consumer-focus":
          continue    
     if publisher_name == "crawley-borough-council":
          continue    
     if publisher_name == "crc-energy-efficiency-scheme":
          continue    
     if publisher_name == "cycle-streets":
          continue    
     if publisher_name == "defence-academy-of-the-united-kingdom":
          continue    
     if publisher_name == "defence-support-group":
          continue    
     if publisher_name == "department-for-work-and-pensions":
          continue    
     if publisher_name == "department-of-justice":
          continue    
     if publisher_name == "driver-and-vehicle-licensing-agency":
          continue    
     if publisher_name == "driving-standards-agency":
          continue    
     if publisher_name == "east-cheshire-nhs-trust":
          continue    
     if publisher_name == "education-funding-agency":
          continue    
     if publisher_name == "energy-saving-trust":
          continue    
     if publisher_name == "fco-services":
          continue    
     if publisher_name == "general-register-office-for-scotland":
          continue    
     if publisher_name == "general-teaching-council-for-england":
          continue    
     if publisher_name == "government-car-and-despatch-agency":
          continue    
     if publisher_name == "great-britain-china-centre":
          continue    
     if publisher_name == "hm-inspectorate-of-probation":
          continue    
     if publisher_name == "hm-passport-office":
          continue    
     if publisher_name == "independent-housing-ombudsman":
          continue  
     if publisher_name == "independent-living-fund":
          continue  
     if publisher_name == "isle-of-wight-council":
          continue  
     if publisher_name == "joint-nature-conservation-committee":
          continue  
     if publisher_name == "judicial-appointments-commission":
          continue  
     if publisher_name == "judicial-office":
          continue  
     if publisher_name == "lake-district-national-park":
          continue
     if publisher_name == "learning-and-skills-council-skills-funding-agency":
          continue
     if publisher_name == "marine-accident-investigation-branch":
          continue
     if publisher_name == "maritime-and-coastguard-agency":
          continue
     if publisher_name == "marshall-aid-commemoration-commission":
          continue
     if publisher_name == "musgrove-park-hospital":
          continue
     if publisher_name == "national-college-for-teaching-and-leadership":
          continue
     if publisher_name == "national-employment-savings-trust":
          continue
     if publisher_name == "national-health-service":
          continue
     if publisher_name == "nhs-bedfordshire":
          continue
     if publisher_name == "pensions-ombudsman":
          continue
     if publisher_name == "nhs-east-cheshire-ccg":
          continue
     if publisher_name == "nhs-liverpool-ccg":
          continue
     if publisher_name == "oag":
          continue
     if publisher_name == "prisons-and-probation-ombudsman":
          continue
     if publisher_name == "public-health-england":
          continue
     if publisher_name == "remploy-limited":
          continue
     if publisher_name == "royal-borough-of-greenwich":
          continue
     if publisher_name == "olympic-delivery-authority":
          continue
     if publisher_name == "royal-botanic-gardens-kew":
          continue
     if publisher_name == "royal-borough-of-greenwich":
          continue
     if publisher_name == "rugby-borough-council":
          continue
     if publisher_name == "rural-payments:-agency":
          continue
     if publisher_name == "rural-payments-agency":
          continue
     if publisher_name == "rsecurity-industry-authority":
          continue
     if publisher_name == "security-industry-authority":
          continue
     if publisher_name == "service-personnel-and-veterans-agency":
          continue

     if publisher_name == "sport-england":
          continue
     if publisher_name == "standards-and-testing-agency":
          continue
     if publisher_name == "stockton-on-tees-borough-council":
          continue
     if publisher_name == "teignbridge-district-council":
          continue
     if publisher_name == "the-food-and-environment-research-agency":
          continue
     if publisher_name == "the-northern-lighthouse-board":
          continue
     if publisher_name == "the-pensions-regulator":
          continue
     if publisher_name == "valuation-office-agency":
          continue
     if publisher_name == "vehicle-and-operator-services-agency":
          continue
     if publisher_name == "vehicle-certification-agency":
          continue
     if publisher_name == "visit-england":
          continue
     if publisher_name == "westminster-foundation-for-democracy":
          continue
     if publisher_name == "wilton-park-executive-agency":
          continue

     """
    
     if publisher_name == "wolverton-and-greenleys-town-council":
          continue

     """  foi-web tag missing
     if publisher_name == "agri-food-and-biosciences-institute":
          continue   
     if publisher_name == "belfast-city-council":
          continue     
     if publisher_name == "birmingham-childrens-nhs-foundation-trust":
          continue    
     """


     url_1 = "http://data.gov.uk/api/3/action/organization_show?id="+ publisher_name
     http_1 = urllib3.PoolManager()
     publisher_returned = http_1.request('GET', url_1)

     print("*************************************************************")
     print("publisher number=", cntr-1)
     print("publisher name  =", publisher_name)
     print("page status     =", publisher_returned.status)
     #print("page returned   =", publisher_returned )
     #print("page data=",(publisher_returned.data))


     #****************************************
     #  read the save json file
     f_1 = open(publisher_name + ".json", 'wb')
     f_1.write(publisher_returned.data)
     f_1.close()

     

     #********************************
     #  go read through all the packets
     #  for this publisher

     with open(publisher_name + ".json") as data_file_2: 
            publisher_data = json.load(data_file_2)

        
     #********************************
     # delete the current publisher file
     os.remove(publisher_name + ".json")     # delete the publisher's source file

     #_______________________________
     #  retrieve one-time publisher elements.

     publisher_title     = publisher_data["result"]["title"]
     publisher_type      = publisher_data["result"]["type"]

     #publisher_web_site  = publisher_data["result"]["foi-web"]
     publisher_web_site  = ""

     publisher_email     = publisher_data["result"]["foi-email"]

     publisher_category  = ""     #publisher_data["result"]["category"]
     publisher_id        = publisher_data["result"]["id"]

     #  Do you want anything else ie.  approval_status, phone numbers, etc. ??
     

     #***************************************************
     #  does this organisation publish anything?

     if len(publisher_data["result"]["packages"]) == 0:    #"result""packages" 
          print ("No publications - WHAT?")
          continue


     #****************************************************
     #  look through the Publisher's site for pointers
     #  to the data, via the publisher_id key
     print("    ")
     cntr_2 = 0
     for y in publisher_data["result"]:

         #if cntr_2 > 5:
         #    break
         #cntr_2 += 1

         #****************************************
         #  create an output line, element by element
         #  next time I'm going to print using
         #  just publisher_data["result"]["packages"][0]["title"]

         print("publisher_returned = ", publisher_returned)   
         print("publisher_type     = ", publisher_type)

         
         #.....................
         #  packets

         publisher_package_title = publisher_data["result"]["packages"][cntr_2]["title"]
         publisher_package_id    = publisher_data["result"]["packages"][cntr_2]["id"]
         publisher_package_link  = "http://data.gov.uk/api/3/action/package_show?id=" + publisher_package_id
         publisher_package_name  = publisher_data["result"]["packages"][cntr_2]["name"]

         """
         print("publisher_title = ", publisher_title)
         print("publisher_package_id = ", publisher_id)
         print ("publisher_package_link = ",  publisher_package_link)
         print("publisher_package_name = ", publisher_package_name)
         """

         #**************************************************
         #   Build another query and go get the link
         #   to the actual data.
         #   ie. "b1f2f7be-d024-425f-b6ff-5d8f45d86738"
   
    
         url_3 = "http://data.gov.uk/api/3/action/package_show?id=" + publisher_package_id
         http_3= urllib3.PoolManager()
         page_returned_3 = http_3.request('GET', url_3)

         print("page returned=", page_returned_3)
         #print("page status  =", page_returned_3.status)
         print("    ")

         f_3 = open("publisher_package_id.json", 'wb')
         f_3.write(page_returned_3.data)
         f_3.close()
    
         with open("publisher_package_id.json") as data_file_3:    
              publisher_actual_data = json.load(data_file_3)

         # ---------------------------------
         #  I need a conditional to verify that the
         #  publisher actually has a resources url
         #  
         publisher_data_url= publisher_actual_data["result"]["resources"][0]["url"]
         print("publisher_package_id = ", publisher_data_url)

         #**************************************************
         #  sPrint a header record for the CSV file

         if printheader == 1:
              printheader = 0  # false  we only need to print the header once
              header = "Data Source URL, Publisher Title, Package Name, Type, Site URL, email,"
              header = header + "Category), Publisher ID, Package Title, Package ID, Package URL"
              print(header, file=outputfile)
         
         #**************************************************
         #  start writing one record with all the required elements

         output_line =''
         spacer = ', '

         # beginning
    
         output_line = output_line + publisher_data_url  + spacer
         output_line = output_line + publisher_title     + spacer       
         output_line = output_line + publisher_package_name    + spacer
             
         output_line = output_line + publisher_type      + spacer
         output_line = output_line + publisher_web_site  + spacer
         output_line = output_line + publisher_email     + spacer
         output_line = output_line + publisher_category  + spacer
         output_line = output_line + publisher_id        + spacer

         output_line = output_line + publisher_package_title     + spacer
         output_line = output_line + publisher_package_id        + spacer
         output_line = output_line + publisher_package_link   


         #  end

         print(output_line, file=outputfile)
         #print("  ", file=outputfile)

 
     
    
print ("end of packets")
outputfile.close()

     
