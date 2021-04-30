# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:31:51 2021

@author: mathe
"""

## Importar bibliotecas
from selenium import webdriver
from time import sleep
import pandas as pd

## URL
URL_LINKEDIN_DS = 'https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br'

# CLASS AND XPATHS
DESCRIPTION = 'description'
JOB_CRITERIA='job-criteria__list'
JOB_TITLE = 'topcard__title'
COMPANY = '/html/body/main/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[1]'
LOCATION = '/html/body/main/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[2]'
JOB_RESULTS_BAR = 'result-card'


# Instaciar variável do Google no Selenium
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL_LINKEDIN_DS)

# Definir variáveis que utilizaremos
all_description = []
all_locations = []
all_titles = []
all_company = []
all_criterias = []

# Controlar tamanho dos resultados
len_results = 0

# Pegar as vagas de toda a barra de resultados
all_results = driver.find_elements_by_class_name(JOB_RESULTS_BAR)

# Criar Loop While para execução
while len(all_results)>len_results:
    # Loop for para percorrer cada elemento
    for r in all_results[len_results:]:       
        r.click() # Clicar na descrição
        sleep(2)
        try:
            # Pegar elementos
            description = driver.find_element_by_class_name(DESCRIPTION).text
            location = driver.find_element_by_xpath(LOCATION).text
            company = driver.find_element_by_xpath(COMPANY).text
            title = driver.find_element_by_class_name(JOB_TITLE).text
            criteria = driver.find_element_by_class_name(JOB_CRITERIA).text     
            # Adicionar elementos na lista que criamos
            all_description.append(description)
            all_locations.append(location)
            all_titles.append(title)
            all_company.append(company)
            all_criterias.append(criteria)
        except:         
            print('Erro')
            pass

    # Atualizar resultados
    len_results = len(all_results)
    all_results = driver.find_elements_by_class_name(JOB_RESULTS_BAR)
    print(len_results)
    print(len(all_results))
    print('Alteração de Página')
    
# Exportar dados para CSV
export_data = {'company':all_company, 'title':all_titles, 'location': all_locations, 'criteria':all_criterias, 'description':all_description}
df = pd.DataFrame(export_data)

df.to_csv('linkedin_jobs.csv')