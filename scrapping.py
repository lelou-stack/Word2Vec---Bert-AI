import csv
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://best.aliexpress.com/?af=LXKA4UNIg&cn=64566f9248714a3a0f517eea&cv=5&dp=656b3c6d3ea4d80345a25eef&aff_fcid=afeadd876f194f5c92b31a967c375a95-1701526638284-08874-_DEM9iex&tt=CPS_NORMAL&aff_fsk=_DEM9iex&aff_platform=portals-tool&sk=_DEM9iex&aff_trace_key=afeadd876f194f5c92b31a967c375a95-1701526638284-08874-_DEM9iex&terminal_id=01df98161d7c4a7fb1114e2e064cd565'
driver = webdriver.Chrome()  # Assurez-vous d'avoir ChromeDriver installé et dans votre PATH
driver.get(url)

# Attendre que la page soit entièrement chargée (peut nécessiter des ajustements)
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
category_list = soup.find('ul', class_='Categoey--categoryList--2QES_k6')

categories = []

if category_list:
    for item in category_list.find_all('li'):
        category = item.text.strip()
        categories.append(category)

    # Enregistrez les catégories dans un fichier CSV
    with open('categories.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category'])
        writer.writerows(map(lambda x: [x], categories))

    # Enregistrez les catégories dans un fichier texte
    with open('categories.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(categories))
else:
    print("La classe 'Categoey--categoryList--2QES_k6' n'a pas été trouvée.")

driver.quit()  # Fermez le navigateur après utilisation
