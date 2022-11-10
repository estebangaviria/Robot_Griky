from logging import exception
import subprocess
import robot
import time
import Consolidar
import robot_usuarios


def run():
    
    def llamado_robot(url, path_destino, incremento, lim_inf, lim_sup):

        Consolidar.borrar()
        contador = 1
        descarga_exitosa = True
        while contador <= 3:
                try:
                    robot.robot(url, incremento, lim_inf, lim_sup)
                    print('Descarga exitosa Classrun')
                    descarga_exitosa = True
                    break
                except:
                    print("Un error ha ocurrido con la instancia Classrun")
                    descarga_exitosa = False
                    pass
                contador += 1
        contador = 1

        
        time.sleep(1)
        try:   
            if descarga_exitosa == True:
                Consolidar.generar_archivo(path_destino)
        except:
            pass

    def llamado_robot_usuarios(url, path_destino, lim_sup):

        Consolidar.borrar()
        contador = 1
        descarga_exitosa = True
        while contador <= 3:
                try:
                    robot_usuarios.robot(url, lim_sup)
                    print('Descarga exitosa ')
                    descarga_exitosa = True
                    break
                except:
                    print("Un error ha ocurrido con la instancia ")
                    descarga_exitosa = False
                    pass
                contador += 1
        contador = 1

        time.sleep(1)
        try:   
            if descarga_exitosa == True:
                Consolidar.generar_archivo(path_destino)
        except:
            pass




    #CLASSRUN-------------------------------------------------------------------------------------------------------------     
    llamado_robot(url='https://campus.class-run.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Classrun/Profesionales/', incremento=20, lim_inf=10, lim_sup=60)

    # #UMA-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://umaplus.uma.edu.pe/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Uma/Profesionales/', incremento=25, lim_inf=10, lim_sup=45)


    # #OCF-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://educatubolsillo.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Ocf/Profesionales/', incremento=5, lim_inf=10, lim_sup=60)

    # #GRIKY
    # llamado_robot(url='https://campus.griky.co/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Griky/Reporte de cursos/Profesionales/', incremento=25, lim_inf=10, lim_sup=60)

    # #ROBINFOOD-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://robinfooduniversity.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Robinfood/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # #AUTONOMA-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://autonomadigital.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Autonoma/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # #CLASE-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://campus.clase.edu.co/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Clase/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # #HOLASTAFF-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://fundacion.holastaffeducacion.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Holastaff/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # #ONCONNECTION-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://onconnection.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Onconnection/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)
    
    # #ISTTE-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://isttezeta.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Istte/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #EDP-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://edpplus.triboolearning.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Edp/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #KONFIO-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://academiakonfio.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Konfio/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #GLOBALI-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://global-i.triboolearning.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Globali/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #SURA-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://sura.learning-tribes.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Sura/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #UMECIT-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://click-umecit.learning-tribes.com//analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Umecit/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #UGB-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://plus.ugb.edu.sv/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Ugb/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #CABLEMAS-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://cursos.amashop.com.co/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Cablemas/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #ISEP-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://campus.uisep.one/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Isep/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # # #CORONA-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://go.coronaaprende.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Corona/Profesionales/', incremento=10, lim_inf=10, lim_sup=280)

    # # #UNE-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://unevirtual.triboolearning.com/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Une/Profesionales/', incremento=20, lim_inf=10, lim_sup=45)

    # #EANX-------------------------------------------------------------------------------------------------------------
    # llamado_robot(url='https://campus.eanx.io/analytics/customized/', path_destino='C:/Users/Administrator/Griky/Griky Dashboard - Documentos/Reporting/Eanx/Profesionales/', incremento=10, lim_inf=10, lim_sup=520)
     
    print("Descarga terminada")
    #exec(open("prueba.py").imprime('sas'))

# def reportes():
#     import Consolidar
#     Consolidar
#     print("Consolidacion  terminada")

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    run()
    #reportes()
    