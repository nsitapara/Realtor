import api_key
import requests
import json
import os
import sys
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	
# sys.path.append(
#     os.path.join(os.path.dirname(__file__), 'housingdata')
# )
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "housingdata.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django
from django.conf import settings

django.setup()
from marketdata.models import HouseDataPoint, HousingQueryData, ListOfCities
# import plotly.express as px
realtor_api_key = api_key.realtor_api_key

city_list = list(ListOfCities.objects.all().values_list('city',flat=True))
# city_list = ['Mountain View']
print(f"CURRENT CITY LIST: {city_list}")
def get_list_for_sale(city,offset=0):
    # url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"
    url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-for-sale"

    querystring = {"city":city,"limit":"200","state_code":"CA","offset":str(offset),"sort":"relevance"}

    headers = {
        'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
        'x-rapidapi-key': "d1535aaabemshbd0fb3ac61c3f3dp1b1a6cjsn1c55333b5724"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)


    return(response)


def getdataforcity(city, offset=0):
    print(f"Getting Data for {city}")
    list_of_sales = get_list_for_sale(city,offset)
    print(f"Got Data for {city}")
    json_sale = json.loads(list_of_sales.text)
    print(f"Json Created for {city}")
    current_total_listing_for_sale = json_sale["meta"]["matching_rows"]
    print(f"Total Records Avaiable {current_total_listing_for_sale}")
    listing_in_current_query = len(json_sale["properties"]) 
    print(f"Total Records in JSON: {listing_in_current_query}")
    
    if offset > 0:
        remaining = current_total_listing_for_sale-offset-listing_in_current_query
    else:
        queryData = HousingQueryData(city = city,total_records = current_total_listing_for_sale)
        queryData.save()
        remaining = (current_total_listing_for_sale-listing_in_current_query)
    # if remaining <= 0:
    #         remaining = 0
    print(f"Remaining Records: {remaining}")

    objs = []
    query_id = HousingQueryData.objects.last().query_id
    for data_point in json_sale["properties"]:
        query_id = query_id
        try:
            property_id = data_point['property_id']
        except:
            property_id = 0
        try:
            listing_id = data_point['listing_id']
        except:
            listing_id = 0
        try: 
            rdc_web_url = data_point['rdc_web_url']
        except:
            rdc_web_url = 0
        try:
            city = data_point['address']["city"]
        except:
            city = 0
        try:
            line = data_point['address']["line"]
        except:
            line = 0
        try:
            postal_code = data_point['address']["postal_code"]
        except:
            postal_code = 0
        try:
            state_code = data_point['address']["state_code"]
        except:
            state_code = 0
        try:
            state = data_point['address']["state"]
        except:
            state = 0
        try:
            county = data_point['address']["county"]
        except:
            county = 0
        try:
            time_zone = data_point['address']["time_zone"]
        except:
            time_zone = 0
        try:
            neighborhood_name = data_point['address']["neighborhood_name"]
        except:
            neighborhood_name = 0
        try:
            prop_type = data_point['prop_type']
        except:
            prop_type = 0
        try: 
            prop_status = data_point['prop_status']
        except:
            prop_status = 0
        try: 
            price = data_point['price']
        except:
            price = 0
        try: 
            baths_full = data_point['baths_full']
        except:
            baths_full = 0
        try: 
            baths = data_point['baths']
        except:
            baths = 0
        try: 
            beds = data_point['beds']
        except:
            beds = 0
        try: 
            size = data_point['building_size']['size']
        except:
            size = 0
        try: 
            units = data_point['building_size']['units']
        except:
            units = 0
        try: 
            agents = data_point['agents']
        except:
            agents = 0
        try: 
            office = data_point['office']
        except:
            office = 0
        try: 
            last_update = data_point['last_update']
        except:
            last_update = 0
        try: 
            client_display_flags = data_point['client_display_flags']
        except:
            client_display_flags = 0
        try: 
            lot_size = data_point['lot_size']['size']
        except:
            lot_size = 0
        try:
            lot_size_units = data_point['lot_size']['units']
        except:
            lot_size_units = 0
        try: 
            mls = data_point['mls']
        except:
            mls = 0
        try: 
            data_source_name = data_point['data_source_name']
        except:
            data_source_name = 0
        try:     
            presentation_status = data_point['client_display_flags']["presentation_status"]
        except:
            presentation_status = 0
        try:
            price_change = data_point['client_display_flags']["price_change"]
        except:
            price_change = 0
        try:
            is_new_listing = data_point['client_display_flags']["is_new_listing"]
        except:
            is_new_listing = 0
        objs.append(
        HouseDataPoint(
        link_id = query_id,
        property_id = property_id,
        listing_id = listing_id,
        rdc_web_url = rdc_web_url,
        city = city,
        line = line,
        postal_code = postal_code,
        state_code = state_code,
        state = state,
        county = county,
        time_zone = time_zone,
        neighborhood_name = neighborhood_name,
        prop_type = prop_type,
        prop_status = prop_status,
        price = price,
        baths_full = baths_full,
        baths = baths,
        beds = beds,
        size = size,
        units = units,
        agents = agents,
        office = office,
        last_update = last_update,
        client_display_flags = client_display_flags,
        lot_size = lot_size,
        lot_size_units = lot_size_units,
        mls = mls,
        data_source_name = data_source_name,
        presentation_status = presentation_status,
        price_change = price_change,
        is_new_listing = is_new_listing))
    HouseDataPoint.objects.bulk_create(objs)
    print(f"ADDED DATA FOR {city}, Total Records:{listing_in_current_query} ADDED")
    return(remaining)


for city in city_list:
    page = 1
    print("================================== NEW CITY ==================================")
    print(city)
    remaning_records = getdataforcity(city)
    print(f"CHECK CONDITION FOR WHILE LOOP: City: {city} Remaning records: {remaning_records}")
    while int(remaning_records) > 0:
        print("WHILE LOOP START")
        offsetvalue = page*200
        print(f"Offset Value for Method: {offsetvalue}")
        remaning_records = getdataforcity(city,offset = offsetvalue)
        if remaning_records <= 0:
            print(f"DONE WHILE LOOP: City: {city} Remaning records: {remaning_records}")
        else:
            page = page + 1
            print(f"Continued WHILE LOOP: City: {city} Remaning records: {remaning_records}")
        print("WHILE LOOP END")
        

# for city in city_list:
#     page = 1
#     print(city)
#     remaning_records = getdataforcity(city)
#     print(f"CHECK CONDITION FOR IF LOOP: City: {city} Remaning records: {remaning_records}")

#     if int(remaning_records) > 0:
#         print("IF LOOP START")
#         offsetvalue = page*200
#         print(f"Offset Value for Method: {offsetvalue}")
#         remaning_records = getdataforcity(city,offset = offsetvalue)
#         if remaning_records <= 0:
#             print(f"DONE IF LOOP: City: {city} Remaning records: {remaning_records}")
#         else:
#             page = page + 1
#             print(f"Continued IF LOOP: City: {city} Remaning records: {remaning_records}")
#         print("IF LOOP END")

