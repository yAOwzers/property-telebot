import json
from unicodedata import category
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import logging

MAX_COUNT = 5

scrapeUrl = "https://www.channelnewsasia.com/latest-news"
cnaUrl = "https://www.channelnewsasia.com/"

# logging.basicConfig(filename="scrapper.log", level=logging.DEBUG,
#                     format="%(asctime)s:%(levelname)s:%(message)s")


propertyUrl = "https://www.99.co/singapore/rent?autocom=true&created_at=1660982172438&isFilterUnapplied=false&listing_type=rent&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&name=Singapore&page_num=1&page_size=35&price_max=3000&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&rooms=4%2C5&show_cluster_preview=true&show_description=true&show_future_mrts=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=15"

listingString = []

propertyWebsite = "99.co"

# url scrapper for CNA, get top 5 articales
def scrape():
  # create url
  url = propertyUrl
  # define headers
  headers = { 'User-Agent': 'Generic user agent' }
  # get page
  page = requests.get(url, headers=headers)
  # let's soup the page
  soup = BeautifulSoup(page.text, 'html.parser')

  # output = soup.find_all('script').find(type="application/ld+json")
  output = soup.find(id="__REDUX_STORE__").get_text() # json
  # pprint(output)

  jsonOutput = json.loads(output)
  # print(jsonOutput)

  # print(jsonOutput.location)
  listings = jsonOutput['mapSearch']['altStores']['MapSearchStore']['listings']
  # print(listings)

  for list in listings:
    url = list['listing_url']
    photoList = list['photos']
    user = list['user'] #dict
    unitConfiguration = list['unit_configuration'] #str
    attributes = list['attributes'] # dict
    addressLineOne = list['address_line_1'] # string
    addressLineTwo = list['address_line_2'] # string

    listingString.append("Photo Urls: " + getPhoto(photoList) +  "\n" + 
                    "Listing Url: " + propertyWebsite + str(url) + "\n" + 
                    "Number of Rooms: " + str(unitConfiguration) +  "\n" + 
                    "Details: " + getAttributes(attributes) +  "\n" + 
                    "Address: " + str(addressLineTwo) + ", " + str(addressLineOne) +  "\n" + 
                    getAgentDetails(user) +  "\n")


  # print(str(listingString))
  # with open("output3json", "w") as file:
  #   file.write(str(listingString))

  return (listingString)


def getPhoto(listOfPhotos):
  urlString = ""
  for photo in listOfPhotos:
    url = photo['url']
    urlString =  urlString + url + "\n"

  return urlString

def getAgentDetails(userDict):
  phone = userDict['phone']
  name = userDict['name']

  userString = "Agent name: " + name + "\n" + "Agent Contact Number: " + phone
  return userString

def getAttributes(attributeDict):
  areaSize = attributeDict['area_size_formatted']
  bathrooms = attributeDict['bathrooms']
  price = attributeDict['price_formatted']
  areaSizePerSqm = attributeDict['area_size_sqm_formatted']
  bedrooms = attributeDict['bedrooms']
  beds = attributeDict['bedrooms_formatted']
  bathrooms = attributeDict['bathrooms_formatted']
  builtYear = attributeDict['completed_at']

  attributeString = ("Price: " + price + "\n" +
                    "Size of Area: " + areaSize + "\n" +
                    "Bedrooms: " + str(bedrooms) + "\n" +
                    "Beds: " + beds + "\n"
                    "Bathrooms: " + bathrooms + "\n"
                    "Area Size Per Sqm: : " + str(areaSizePerSqm) + "\n"
                    "Built Year: " + str(builtYear) + "\n")

  return attributeString

scrape()