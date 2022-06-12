from lib2to3.pgen2 import driver
from tabnanny import check
from typing import final
from unicodedata import name
from urllib import response
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import lxml.html as html


credenciales_excel = r"D:\PROYECTOS\ROBOT GRIKY\credenciales.xlsx"

df = pandas.read_excel(credenciales_excel)

user = df["username"][0]
psw = df["password"][0]
# url= 'https://global-i.triboolearning.com/analytics/customized/'
#url = "https://umaplus.uma.edu.pe/analytics/customized/"
# url= 'https://campus.eanx.io/analytics/customized/'
#url='https://go.coronaaprende.com/analytics/customized/'
url = 'https://campus.class-run.com/analytics/customized/'
#url = 'https://robinfooduniversity.learning-tribes.com/analytics/customized/'
#url = 'https://campus.griky.co/analytics/customized/'
#url = 'https://cursos.amashop.com.co/analytics/customized/'
#url = 'https://campus.uisep.one/analytics/customized/'

# Aplicar filtros y descargar

aplicar = '//*[@id="submit-button"]'
nube = '//*[@id="main"]/div/nav/ul/li/a/i'
archivo = '//*[@id="report-file-list"]/div[1]/a'

driver = webdriver.Chrome()

# Maximizar pantalla
driver.maximize_window()
driver.get(url)

# Acciones:
#driver.find_element(By.CSS_SELECTOR, "#login-form > article > div > div.email-login-link > a").click()

# try:
#     driver.find_element(By.CSS_SELECTOR, '#login-form > article > div > div.email-login-link > a').click()
# except :
#     print("error-----------------")
# Login:
driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys(user)
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys(psw)
driver.find_element(By.CSS_SELECTOR, "#login > button").click()
# time.sleep(2)

driver.get(url)
total_cursos = len(driver.find_elements(By.XPATH, '//*[@id="course_section_contents"]/div/div/div[2]/ul/li'))
print(total_cursos)

contador = 1
incremento = 25
ciclos_descarga = incremento
contador2 = contador
ciclos_descarga2 = ciclos_descarga
cant_descargas = int(total_cursos / ciclos_descarga)
residuo = total_cursos % ciclos_descarga
print("total cursos: " + str(total_cursos))
print("cantidad archivos: " + str(cant_descargas + 1))

# Filtros de correo
driver.find_element(By.CSS_SELECTOR, "#user_properties_section").click()
# driver.find_element_by_css_selector(selector_correo).click()

cuenta_filtros = len(driver.find_elements(By.NAME, "selected_properties"))

for i in range(1, cuenta_filtros + 1):
    driver.find_element(
        By.XPATH, '//*[@id="id_selected_properties"]/li[' + str(i) + "]/label"
    ).click()


# driver.find_element_by_xpath(check_correo).click()

# Filtros de formato xls
driver.find_element(By.CSS_SELECTOR, "#format_section").click()
driver.find_element(
    By.CSS_SELECTOR, "#table-export-selection > li:nth-child(2)"
).click()

driver.find_element(By.CSS_SELECTOR, "#course_section").click()
print("ciclos de descarga: " + str(ciclos_descarga))
print("cantidad descargas: " + str(cant_descargas))
# ------------------------------------------------------------------------
# driver.execute_script("window.scrollTo(0, 0)")
# driver.find_element(By.XPATH, nube).click()
# last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
# print("-----------------------------")
# print(type(last_file))
# print(last_file)
# without_files = "No hay informes disponibles"

# if without_files == last_file:
#     while without_files == last_file:
#         time.sleep(5)
#         driver.execute_script("window.scrollTo(0, 0)")
#         driver.find_element(By.XPATH, nube).click()
#         last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
# else:
#     driver.execute_script("window.scrollTo(0, 0)")
#     driver.find_element(By.XPATH, nube).click()
#     last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text

# print(last_file)
# print("-----------------------------")

# ------------------------------------------------------------------------

# INICIO CICLO 1------------------------------------------------------------------------------------------------------------------
while contador <= cant_descargas * incremento:
    print("entré en el ciclo")
    # Filtros de cursos a elegir:
    driver.find_element(By.CSS_SELECTOR, "#course_section_contents > div > div").click()

    while contador <= ciclos_descarga:
        digitar_cursos = (
            "#course_section_contents > div > div > div.panel > ul > li:nth-child("
            + str(contador)
            + ") > label"
        )
        driver.find_element(By.CSS_SELECTOR, digitar_cursos).click()
        contador += 1
    ciclos_descarga += incremento
    #time.sleep(1)

    driver.find_element(By.XPATH, aplicar).click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]')
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]')
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()

    # Borrar cursos seleccionados
    driver.execute_script("window.scrollTo(0, 0)")
    # time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="course_section"]')
    driver.find_element(By.XPATH, '//*[@id="course_section_contents"]/div/div').click()

    while contador2 <= ciclos_descarga2:
        digitar_cursos2 = (
            "#course_section_contents > div > div > div.panel > ul > li:nth-child("
            + str(contador2)
            + ") > label"
        )
        driver.find_element(By.CSS_SELECTOR, digitar_cursos2).click()
        contador2 += 1

    ciclos_descarga2 += incremento
#--------------------------------------------------------------------------
    # driver.execute_script("window.scrollTo(0, 0)")
    # driver.find_element(By.XPATH, nube).click()
    # new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
    # print(new_file)

    # if without_files == new_file or new_file == "":
    #     while without_files == new_file:
    #         time.sleep(5)
    #         driver.execute_script("window.scrollTo(0, 0)")
    #         driver.find_element(By.XPATH, nube).click()
    #         new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
    # print(new_file)

    
    # if new_file == last_file:
    #     while new_file == last_file:
    #         time.sleep(10)
    #         driver.execute_script("window.scrollTo(0, 0)")
    #         driver.find_element(By.XPATH, nube).click()
    #         new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
    #         driver.find_element(By.XPATH, nube).click()
    # else:
    #     last_file=new_file
    #     driver.execute_script("window.scrollTo(0, 0)")
    #     driver.find_element(By.XPATH, nube).click()
    #     driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()

    # time.sleep(2)
    # last_file=new_file


#--------------------------------------------------------------------------

    time.sleep(45)
    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.XPATH, nube).click()
    driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()
#--------------------------------------------------------------------------
    #print('ultima descarga: '+last_file)
    print("ciclos de descargda: " + str(ciclos_descarga))
    print("contador" + str(contador))
    #time.sleep(0)
# FIN CICLO -------------------------------------------------------------------------------------------------------------------

contador3 = contador
limite = residuo + contador - 1
ciclo_final = 1
# INICIO CICLO ------------------------------------------------------------------------------------------------------------------

print(contador)

if residuo >0:
    print("entreé en el if")
    # Filtros de cursos a elegir:
    driver.find_element(By.CSS_SELECTOR, "#course_section_contents > div > div").click()

    while contador <= limite:
        digitar_cursos = (
            "#course_section_contents > div > div > div.panel > ul > li:nth-child("
            + str(contador)
            + ") > label"
        )
        driver.find_element(By.CSS_SELECTOR, digitar_cursos).click()
        contador += 1

    driver.find_element(By.XPATH, aplicar).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]')
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]')
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()

    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(50)
    driver.find_element(By.XPATH, nube).click()
    driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()


# FIN CICLO -------------------------------------------------------------------------------------------------------------------

time.sleep(10)
# Cerrar las acciones:
# driver.quit()
