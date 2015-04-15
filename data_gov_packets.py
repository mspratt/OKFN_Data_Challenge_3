"""
data_gov_packets.py

This program is the 2nd of 3
you got here from data-gov-publisher

Thus, we have a publisher's name and
want to get the list of their publications

and write it to the output csv file

"""

#*************************************************
#  Initialize
import sys, os, urllib3, json, html
#import data_gov_output

# write to the csv file
outputfile = open("data_gov_publisher_results.csv", 'w')

#*************************************
#
#  We have a department/publisher what have they got on-line?
#

#  select a larger publisher from the 1ist of 5 - for testing
publisher_returned = "adur-district-council.json"

    
with open(publisher_returned) as data_file_2: 
  publisher_data = json.load(data_file_2)


#_______________________________
#  retrieve one-time elements.

publisher_title     = publisher_data["result"]["title"]
publisher_type      = publisher_data["result"]["type"]
publisher_web_site  = publisher_data["result"]["foi-web"]
publisher_email     = publisher_data["result"]["foi-email"]
publisher_category  = publisher_data["result"]["category"]
publisher_id        = publisher_data["result"]["id"]

#  approval_status, phone numbers, etc. ??


#************************************
#  loop throught the results.packages of the publisher's page and
#  get the title, id, name and ???


cntr_2 = 0
for y in publisher_data["result"]:

    if cntr_2 > 5:
        break

    #****************************************
    #  create an output line, element by element
    #  next time I'm going to print using
    #  just publisher_data["result"]["packages"][0]["title"]

    print("publisher_returned = ", publisher_returned)   
    print("publisher_type     = ", publisher_type)

    #.....................
    #  packets

    publisher_package_title = publisher_data["result"]["packages"][cntr_2]["title"]
    print("publisher_title = ", publisher_title)

    publisher_package_id = publisher_data["result"]["packages"][cntr_2]["id"]
    print("publisher_package_id = ", publisher_id)

    publisher_package_link = "http://data.gov.uk/api/3/action/package_show?id=" + publisher_package_id
    print ("publisher_package_link = ",  publisher_package_link)
   
    publisher_package_name= publisher_data["result"]["packages"][cntr_2]["name"]
    print("publisher_package_name = ", publisher_package_name)


    #**************************************************
    #   Build another query and go get the link
    #   to the actual data.
    #   ie. "b1f2f7be-d024-425f-b6ff-5d8f45d86738"

   
    
    url_3 = "http://data.gov.uk/api/3/action/package_show?id=" + publisher_package_id
    http_3= urllib3.PoolManager()
    page_returned_3 = http_3.request('GET', url_3)

    print("page returned=", page_returned_3)
    print("page status  =", page_returned_3.status)
    print("    ")
    f_3 = open("publisher_package_id.json", 'wb')
    f_3.write(page_returned_3.data)
    with open(f_3) as data_file_3:    
    publisher_actual_data = json.load(data_file_3)


    # *******************  loop through publisher Data  ******
    print("********   loop through publishers package ID   ************")
    cntr_3=0
    for z in publisher_actual_data["resources"] :

        if cntr_3 > 5:  # normally there is only on link to the data
            break

            publisher_data_url= publisher_actual_data["result"]["resources"][cntr_3]["url"]
            print("publisher_package_id = ", publisher_data_url)

            cntr += 1
    






    #**************************************************
    #  start writing one record with all the required elements

    output_line =''
    spacer = ','
    
    output_line = output_line + publisher_title     + spacer       # beginning

    output_line = output_line + publisher_type      + spacer
    output_line = output_line + publisher_web_site  + spacer
    output_line = output_line + publisher_email     + spacer
    output_line = output_line + publisher_category  + spacer
    output_line = output_line + publisher_id        + spacer

    output_line = output_line + publisher_package_title     + spacer
    output_line = output_line + publisher_package_id        + spacer
    output_line = output_line + publisher_package_link      + spacer

    output_line = output_line + publisher_package_name      + spacer
    output_line = output_line + publisher_data_url          #  end

    print(output_line, file=outputfile)
    
    
    #   python data_gov_output

    print("********************")

    cntr_2 += 1
    
print ("end of packets")
outputfile.close()





