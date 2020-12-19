# Projeto exercicio Localiza Ler e armazenar 5 categorias e 5 links do site da localiza
from selenium import webdriver
import pandas as pd
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.localiza.com/brasil/pt-br/grupos-de-carros"
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)
    time.sleep(1)  # Aguarde o carregamento dos dados
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # rola a pagina pro final ( 1 rolagem resolve)
    time.sleep(2)  # aguarde o carregamento dos dados
    classes_list = driver.find_elements_by_class_name("ds-car-group-text__group-name")
    # pega o link da primeira imagem do carrousel de cada categoria
    link_list = []
    link_list.append(driver.find_elements_by_xpath('//*[@id="main-content"]/app-frota-carros/div/div/div[2]/ds-car-group[1]/div/ds-car-group-content/ds-car-group-carousel/div/ngx-hm-carousel/div/section/article[1]/img')[0])
    link_list.append(driver.find_elements_by_xpath('//*[@id="main-content"]/app-frota-carros/div/div/div[2]/ds-car-group[2]/div/ds-car-group-content/ds-car-group-carousel/div/ngx-hm-carousel/div/section/article[1]/img')[0])
    link_list.append(driver.find_elements_by_xpath('//*[@id="main-content"]/app-frota-carros/div/div/div[2]/ds-car-group[3]/div/ds-car-group-content/ds-car-group-carousel/div/ngx-hm-carousel/div/section/article[1]/img')[0])
    link_list.append(driver.find_elements_by_xpath('//*[@id="main-content"]/app-frota-carros/div/div/div[2]/ds-car-group[4]/div/ds-car-group-content/ds-car-group-carousel/div/ngx-hm-carousel/div/section/article[1]/img')[0])
    link_list.append(driver.find_elements_by_xpath('//*[@id="main-content"]/app-frota-carros/div/div/div[2]/ds-car-group[5]/div/ds-car-group-content/ds-car-group-carousel/div/ngx-hm-carousel/div/section/article[1]/img')[0])
    for i, link_ext in enumerate(link_list):
        classes_list[i] = classes_list[i].text #extrai o texto do elemento
        link_list[i] = link_ext.get_attribute("src") #extrai o link do elemento
    # Criar dataframe Pandas
    pd.set_option( 'max_colwidth', 1000)  # colunas mais largas para nao truncar os links
    dic = {'Grupos': classes_list[:5],'Links_Img': link_list} #cria um dicionario python
    data = pd.DataFrame(data=dic, dtype=str)  # (columns=classes_list[:5])
    print(dic)
    print(data)


