import requests
site_map = 'http://www.pngmart.com/sitemap.xml/'
response = requests.get(site_map)
response.text
