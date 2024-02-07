import csv

def save_csv(images_urls:list, name_file:str):
    '''
    Función que guarda la lista de urls en un `.csv` en la carpeta `outputs`
    '''
    with open(f'outputs/{name_file}.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for enlace in images_urls:
            csv_writer.writerow([enlace])