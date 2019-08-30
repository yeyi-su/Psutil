import os
import psutil

def menu():	
	print ("Seleccione una opcion")
	print("1-Listar los PIDs actuales")
	print("2-Mostrar el nombre de un proceso, seleccionando el PID")
	print("3-Mostrar la ruta de dicho proceso")
	print("4-Mostrar los parametros de consola")
	print("5-Mostrar el PID del proceso seleccionado")
	print("6-Mostrar el PID del proceso padre")
	print("7-Mostrar informacion del proceso padre")
	print("8-Mostrar informacion de los procesos hijos")
	print("9-Mostrar el estado del proceso")
	print("10-Mostrar el usuario que esta ejecutando el proceso")
	print("11-Mostrar los archivos abiertos por el proceso")
	print("12-Terminar el proceso")
	print("13-Cantidad de CPUs (reales y logicas)")
	print("14-Lista de particiones del sistema")
	print("15-Espacio usado por la particion raiz ( / )")
	print("16-Informacion de las interfaces de red")
	print("a-Salir")
	opcion = input ("Opcion seleccionada: ")
	return opcion


def select_PID():
	try:
		pid = input("Seleccione el PID ")
		return pid
	except SyntaxError:
		pass
	
def press_key():
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass
		
selected_pid = 0

while True:
	os.system("clear")
	if (selected_pid == 0):
		print ("No se ha seleccionado ningun proceso")
	else:
		print ("Proceso seleccionado:")
		print (selected_pid)
	opcion = menu()
	if (opcion == "1"):
		print (psutil.pids())	
		press_key()	
	elif (opcion == "2"):
		selected_pid = select_PID()
		print ("PID seleccionado: ")
		print (selected_pid)
		p = psutil.Process(int(selected_pid))
		print ("Nombre:")
		print (p.name())
		press_key()
	elif (opcion == "3"):
		if (selected_pid != 0):
			print ("Ruta:")
			print (p.exe())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "4"):
		if (selected_pid != 0):
			print ("Ruta:")
			print (p.cwd())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "5"):
		if (selected_pid != 0):
			print ("PID:")
			print (p.pid)
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "6"):
		if (selected_pid != 0):
			print ("PID del proceso padre:")
			print (p.ppid())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "7"):
		if (selected_pid != 0):
			print ("Info del proceso padre:")
			print (p.parent())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "8"):
		if (selected_pid != 0):
			print ("Procesos hijos:")
			print (p.children())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "9"):
		if (selected_pid != 0):
			print ("Estado del proceso:")
			print (p.status())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "10"):
		if (selected_pid != 0):
			print ("Usuario:")
			print (p.username())
		else:
			print ("no hay PID seleccionado")
		press_key()	
	elif (opcion == "11"):
		if (selected_pid != 0):
			print ("Archivos en uso:")
			print (p.open_files())
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "12"):
		if (selected_pid != 0):
			print ("Terminando el proceso...")
			p.terminate()
		else:
			print ("no hay PID seleccionado")
		press_key()
	elif (opcion == "13"):
		print ("CPUs logicas:")
		print (psutil.cpu_count())
		print ("CPUs fisicas:")
		print (psutil.cpu_count(logical=False))
		press_key()
	elif (opcion == "14"):
		print ("Particiones del sistema:")
		print(psutil.disk_partitions())
		press_key()
	elif (opcion == "15"):
		print ("Espacio usado por la particion raiz:")
		print(psutil.disk_usage('/'))
		press_key()
	elif (opcion == "16"):
		print ("Info de las interfaces de red:")
		print (psutil.net_if_addrs())
		press_key()
	elif (opcion == "a"):
		exit()
	else:
		print ("Opcion no valida")
		press_key()
