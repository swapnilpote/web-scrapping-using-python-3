import soup as sp
import nav_links as nl

# Pagination links
categories_links = nl.each_cat_links()

def pagination_links():
	all_cat_page_links = []

	for single_cat in categories_links:
		print(single_cat)
		single_cat_page_soup = sp.make_soup(single_cat.strip())

		last_page_number = single_cat_page_soup.find('div', {'id':'pagination'}).findAll('a')[-2].text

		for page_number in range(1, int(last_page_number)+1):
			single_page_link = single_cat.strip() + '?page=' + str(page_number).lstrip() + '-c'
			print(single_page_link)
			all_cat_page_links.append(single_page_link)

	return all_cat_page_links


def single_product_link():
	page_links = pagination_links()
	product_links = []

	for i in page_links:
		single_page_link_soup = sp.make_soup(i)

		for single_link in single_page_link_soup.findAll('div', {'class':'search-merchant-nugget clearfix'}):
			print(single_link.find('a').get('href'))

	return product_links

single_product_link()
