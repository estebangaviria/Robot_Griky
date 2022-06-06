from lib2to3.pgen2 import driver
from tabnanny import check
from unicodedata import name
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

credenciales_excel = r'D:\PROYECTOS\ROBOT GRIKY\credenciales.xlsx'

df = pandas.read_excel(credenciales_excel)

user= df['username'][0]
psw= df['password'][0]
#url= 'https://global-i.triboolearning.com/analytics/customized/'
url= 'https://umaplus.uma.edu.pe/analytics/customized/'
#url= 'https://campus.eanx.io/analytics/customized/'

#Selectores inicio:
inicio = '#login-form > article > div > div.email-login-link > a'
selector_user = '#login-email'
selector_pass = '#login-password'
selector_login = '#login > button'

#Selectores de filtros:

selector_correo = '#user_properties_section'
# Necesito función que busque la lapabra correo y le de click

check_correo = '//*[@name="selected_properties" and @value="user_email"]'
formato= '#format_section'
check_formato = '#table-export-selection > li:nth-child(2)'
cursos = '#course_section'
elegir_cursos= '#course_section_contents > div > div'
digitar_cursos = '#course_section_contents > div > div > div.panel > ul > li:nth-child(1) > label'
digitar_cursos2 ='#course_section_contents > div > div > div.panel > ul > li:nth-child(3) > label'

#Aplicar filtros y descargar
aplicar='/html/body/div[2]/div[2]/main/div/section[2]/div/form/input[2]'
nube=     '/html/body/div[2]/div[2]/main/div/nav/ul/li/a'
archivo = '/html/body/div[2]/div[2]/main/div/nav/ul/li/div/div[1]/a'

driver = webdriver.Chrome()

#Maximizar pantalla
driver.maximize_window()
driver.get(url)

#Acciones:
driver.find_element_by_css_selector(inicio).click()

#Login:
driver.find_element_by_css_selector(selector_user).send_keys(user)
#time.sleep(2)
driver.find_element_by_css_selector(selector_pass).send_keys(psw)
driver.find_element_by_css_selector(selector_login).click()
#time.sleep(2)

driver.get(url)
total_cursos = len(driver.find_elements(By.XPATH, '//*[@id="course_section_contents"]/div/div/div[2]/ul/li'))
print(total_cursos)
ciclos_descarga = 10
cant_descargas = int(total_cursos / ciclos_descarga)
residuo = total_cursos%ciclos_descarga
print(cant_descargas)
print(residuo)
contador=1
incremento= 10

#INICIO CICLO ------------------------------------------------------------------------------------------------------------------
while ciclos_descarga <= 30:
    #Filtros:
    driver.get(url)
    #Filtros de correo
    driver.find_element_by_css_selector(selector_correo).click()
    driver.find_element_by_xpath(check_correo).click()

    #Filtros de formato xls
    driver.find_element_by_css_selector(formato).click()
    driver.find_element_by_css_selector(check_formato).click()

    cuenta_filtros = len(driver.find_elements(By.NAME, 'selected_properties'))
    #print(cuenta_filtros)

    #Filtros de cursos a elegir:
    driver.find_element_by_css_selector(cursos).click()
    driver.find_element_by_css_selector(elegir_cursos).click()

    # for i in range(contador,ciclos_descarga+1):
    #     digitar_cursos = '#course_section_contents > div > div > div.panel > ul > li:nth-child('+str(i)+') > label'
    #     driver.find_element_by_css_selector(digitar_cursos).click()

    while contador <= ciclos_descarga:
        digitar_cursos = '#course_section_contents > div > div > div.panel > ul > li:nth-child('+str(contador)+') > label'
        driver.find_element_by_css_selector(digitar_cursos).click()  
        contador +=1
    ciclos_descarga += 10
    print(contador)
    print(ciclos_descarga)
    print('--------------------------------------------------------')
    time.sleep(5)
    driver.find_element_by_xpath(aplicar).click()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 0)") 
    time.sleep(30)
    driver.find_element_by_xpath(nube).click()
    #driver.find_element_by_xpath('archivo').click()  
    driver.find_element(By.XPATH , '//*[@id="report-file-list"]/div[1]/a').click()

 
#FIN CICLO -------------------------------------------------------------------------------------------------------------------

# contador = ciclos_descarga+1
# ciclos_descarga += contador-1
# print(contador)
# print(ciclos_descarga)

time.sleep(10)
# Cerrar las acciones:
#driver.quit()

