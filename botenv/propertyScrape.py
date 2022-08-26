from bs4 import BeautifulSoup
import requests
from pprint import pprint

scrapeUrl = "https://www.99.co/singapore/rent?autocom=false&listing_type=rent&map_bounds=1.134089%2C103.562254%2C1.525489%2C103.964747&page_num=1&page_size=35&price_max=3000&property_segments=residential&query_coords=1.2261091378444768%2C103.72545750351733&query_ids=zobukit_batok%2Czobukit_merah%2Czochoa_chu_kang%2Czoclementi%2Czojurong_east%2Czojurong_west&query_limit=radius&query_type=zone&radius_max=1000&rental_type=&show_cluster_preview=true&show_description=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11"

def getMeaning():
   # create url
        url = scrapeUrl
        # define headers
        headers = { 'User-Agent': 'Generic user agent' }
        # get page
        page = requests.get(url, headers=headers)
        # let's soup the page
        soup = BeautifulSoup(page.text, 'html.parser')
        pprint(soup)


        # <li class="list-price pull-left">
          # <span class="price">
	
getMeaning()
