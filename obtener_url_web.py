import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_image_urls(url_page):
    # Se abre el Chrome
    driver = webdriver.Chrome()

    # Se abre la página
    driver.get(url_page)

    # Bucle hasta que ya no carguen más productos
    while True:
        # Se presiona el botón hasta que ya no aparezca
        try:
            # Se obtiene el botón (por id) <- con inspeccionar elemento se obtiene
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="products_feed-btn"]')))
            # Se presiona el botón
            boton.click()
        except:
            break
        
        # Tiempo de espera para que cargue bien la página (se puede aumentar si el internet es un poco lento)
        time.sleep(0.5)
    
    # Se obtiene la página con todos sus elementos
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Se obtiene una lista solo con las url de las imágenes
    image_urls = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]

    # Se cierra el driver
    driver.quit()
    
    # Se retorna la lista
    return image_urls


if __name__ == '__main__':
    # Ejemplo de uso con la categoría 'halloween'
    urls = get_image_urls('https://www.casafito.com.ar/halloween')
    print(urls)