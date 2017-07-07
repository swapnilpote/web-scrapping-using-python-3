# In this we are going to find all nav link for creating links related to each cities.
import soup as sp
import cities as cty

cities = cty.find_cities()

def each_cat_links():
	single_nav_soup = sp.make_soup('http://www.mydala.com/')
	nav_list = single_nav_soup.find('ul', {'class':'nav-list'})

	categories = []
	for category in nav_list.findAll('a'):
		category = category.get('href').split('/')[-1]
		categories.append(category)

	del categories[5]

	categories_cities_links = []

	for city in cities:
		for category in categories:
			link = 'http://www.mydala.com/' + city + '/' + category
			categories_cities_links.append(link)

	# we returning all category links of individual cities
	return categories_cities_links
