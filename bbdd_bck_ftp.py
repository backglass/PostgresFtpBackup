from ftplib import FTP
import time
import subprocess



#Obtenemos la fecha del dia y la hora. Se la agregamos al nombre del archivo de backup

day = time.strftime("%d-%m-%y") #Dia con formato
hour =time.strftime("%H_%M_%S") #Hora con formato
now_date = day +"," + hour
file_name = "pfbbdd" +now_date + ".backup"  #Crea el nombre del archivo con now_date
print (file_name)
#Dado que para ejecutar un programa con parámetros se necita usar una lista, ["para1","para2"]

#Creo una variable con el texto de el comando y sus parámetros
pg = f"pg_dump.exe -h localhost -p 5432 -U postgres -w -F c -v -d namebbdd -f c:/bck/{file_name}"
#Creo una lista de pg con cada elemento como parámetro
lst = [a for a in pg.split( )]

#LLamo a ejecutar la lista al sistema operativo.
subprocess.run(lst)

#Subimos el archivo al ftp
ftp = FTP(host='ftp_server_addres', user='your_user', passwd='your_ftp_password') #Conexión
ftp.set_pasv(False)  #Modo activo
print (ftp.getwelcome()) 
file = open(f'{file_name}', 'rb')  #Abrimos el archivo con modo binario
ftp.storbinary(f'STOR {file_name}', file) #
ftp.close()
