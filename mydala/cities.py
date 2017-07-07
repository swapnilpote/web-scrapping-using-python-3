# In this we are going to find all cities for using them inside our urls.
import soup as sp

soup = sp.make_soup('http://www.mydala.com/')

# Find all cities

def find_cities():
	cities_links = []

	cities_box = soup.find('div', {'class':'change-city-fields-wrapper clearfix round-8'})

	for city in cities_box.findAll('option'):
		if city.text == '--Select--':
			pass
		elif city.text == 'Greater Noida':
			pass
		elif city.text == 'Yamuna Nagar':
			city = city.text.replace(' ', '').lower()
			cities_links.append(city)
		else:
			city = city.text.replace(' ', '-').lower()
			cities_links.append(city)

	# cities_links.remove('greater-noida')
	return cities_links

city = find_cities()
print(city)
