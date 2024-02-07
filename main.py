from get_categories import get_categories
from obtener_url_web import get_image_urls
from save_csv import save_csv

categories = get_categories('https://www.casafito.com.ar/productos')

for url_cat in categories:
    categorie_name = str(url_cat).split('/')[-1]
    images_url = get_image_urls(url_cat)
    
    # Se guarda en CSV con los urls
    save_csv(images_url, categorie_name)
