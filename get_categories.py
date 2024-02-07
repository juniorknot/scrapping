from selenium import webdriver
from bs4 import BeautifulSoup

def get_categories(url_page):
    '''
    Función que retorna un lista de las categorias de la página usando la clase: `products-feed__categories-list`
    '''
    driver = webdriver.Chrome()

    driver.get(url_page)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    ul_etiqueta = soup.find('ul', {'class': 'products-feed__categories-list'})

    if ul_etiqueta:
        enlaces_etiqueta = ul_etiqueta.find_all('a')
        urls = [enlace['href'] for enlace in enlaces_etiqueta if 'href' in enlace.attrs]
    
    driver.quit()
    return urls

if __name__ ==  '__main__':
    urls_cat = get_categories()
    print(urls_cat)