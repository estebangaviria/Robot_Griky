from lib2to3.pgen2 import driver
from tabnanny import check
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

#Selectores inicio:
inicio = '#login-form > article > div > div.email-login-link > a'
selector_user = '#login-email'
selector_pass = '#login-password'
selector_login = '#login > button'

#Selectores de filtros:

selector_correo = '#user_properties_section'
# Necesito función que busque la lapabra correo y le de click

check_correo ='#id_selected_properties_2'
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
#driver.find_element(by=By.CSS_SELECTOR, value= user)
#Login:
driver.find_element_by_css_selector(selector_user).send_keys(user)
#time.sleep(2)
driver.find_element_by_css_selector(selector_pass).send_keys(psw)
driver.find_element_by_css_selector(selector_login).click()
#time.sleep(2)
#Filtros:
driver.get(url)
#Filtros de correo
driver.find_element_by_css_selector(selector_correo).click()
driver.find_element_by_css_selector(check_correo).click()
#time.sleep(2)
#Filtros de formato xls
driver.find_element_by_css_selector(formato).click()
driver.find_element_by_css_selector(check_formato).click()
#time.sleep(2)

#Filtros de cursos a elegir:
driver.find_element_by_css_selector(cursos).click()
driver.find_element_by_css_selector(elegir_cursos).click()

numero_cursos = 10

for i in range(numero_cursos):
    if i >0 :
        digitar_cursos = '#course_section_contents > div > div > div.panel > ul > li:nth-child('+str(i)+') > label'
        driver.find_element_by_css_selector(digitar_cursos).click()

#driver.find_element_by_css_selector(aplicar).click()
driver.find_element_by_xpath(aplicar).click()
driver.get(url)
time.sleep(10)
driver.find_element_by_xpath(nube).click()
driver.find_element_by_xpath(archivo).click()

# Cerrar las acciones:
#driver.quit()

