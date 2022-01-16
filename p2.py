#!/usr/bin/python3
#Alvaro Francisco Serrano del Alamo
#Juan Hernandez Sanchez
#Jaime Aleman Moreno
#Equipo 19

import sys, os

port = sys.argv[1]

#Comprobar parámetros
if (not(port.isnumeric()) or int(port)<0 or int(port)>65535):
    print("Debe pasar como parametro un puerto entre 0 y 65535")
    exit()

try:
  group = str(os.environ['GROUP_NUMBER'])
except:
  print("Defina correctamente la variable de entorno GROUP_NUMBER, por ejemplo, Equipo19")
  exit()

#Descargar requisitos

os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2")
fin = open("./practica_creativa2/bookinfo/src/productpage/requirements.txt", "r")
for line in fin:
    os.system("pip install "+line)
    os.system("pip3 install "+line)
fin.close()
os.system("pip3 install flask")

#Sustituir el puerto
os.system("touch ./practica_creativa2/bookinfo/src/productpage/aux.py")
fin2 = open("./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "r") 
fout2 = open("./practica_creativa2/bookinfo/src/productpage/aux.py", "w") 
for line in fin2:
    if "servicesDomain)" in line:
        if "detailsHostname" in line: 
            fout2.write("""    "name": \"http://{0}{1}:"""+str(port)+"""\".format(detailsHostname, servicesDomain),\n""")
        if "ratingsHostname" in line:
            fout2.write("""    "name": \"http://{0}{1}:"""+str(port)+"""\".format(ratingsHostname, servicesDomain),\n""")
        if "reviewsHostname" in line:
            fout2.write("""    "name": \"http://{0}{1}:"""+str(port)+"""\".format(reviewsHostname, servicesDomain),\n""")
    else:
        fout2.write(line)
fin2.close()
fout2.close()
os.system("rm ./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py")
os.system("mv ./practica_creativa2/bookinfo/src/productpage/aux.py ./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py ")
#Sustituir el Título
os.system("touch ./practica_creativa2/bookinfo/src/productpage/templates/aux.html")
fin3 = open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r") 
fout3 = open("./practica_creativa2/bookinfo/src/productpage/templates/aux.html", "w") 
for line in fin3:
    if "navbar-brand" in line:
        fout3.write("""   <a class=\"navbar-brand\" href=\"#\">"""+os.environ['GROUP_NUMBER']+"""</a> \n""")
    else:
        fout3.write(line)
fin3.close()
fout3.close()
os.system("rm ./practica_creativa2/bookinfo/src/productpage/templates/productpage.html")
os.system("mv ./practica_creativa2/bookinfo/src/productpage/templates/aux.html ./practica_creativa2/bookinfo/src/productpage/templates/productpage.html")
#Ejecutar
os.system("python3 ./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py "+port)