# Proyecto 2: Futoshiki
# Fecha de creación: 11 de julio, 2020
# Última modificación: 25 de julio, 2020
# Desarrollado por: Pamela Dinarte

from tkinter import *
from tkinter import messagebox
import pickle
import os
from random import randint
import time

#Configuración-----------------------------------------------------------------

def regresarCF(ventanaConfig):
    ventanaConfig.destroy()
    menuPrincipal()

def activar_timer(horas, minutos, segundos):
    horas['state'] = NORMAL
    minutos['state'] = NORMAL
    segundos['state'] = NORMAL

def desactivar_timer(horas, minutos, segundos):
    horas['state'] = DISABLED
    minutos['state'] = DISABLED
    segundos['state'] = DISABLED
    
    
def comprobar_datos(nivel, reloj, panel, horas, minutos, segundos,\
                    ventanaConfig):
    '''Verifica que los datos de la configuración que el usuario
    quiere guardar sean correctos y guarda los datos; de lo
    contario retorna el mensaje.
    Entradas:
            - nivel: 0, 1, 2 ó 3
            - reloj: 0, 1, 2 ó 3
            - panel: 0, 1 ó 2
            - horas, minutos, segundos: string con un número
    Salidas: mensajes de error si algún dato no cumple.'''
    #verifica que se hayan hecho todas las configuraciones
    if nivel == 0 or reloj == 0 or panel == 0:
        messagebox.showerror(message = 'Debe escoger una opción para todas '+\
                             'las configuraciones. No se guardaron los datos.')
    #verifica que se haya llenado el tiempo si marcó timer
    elif reloj == 3:
        if horas == "" or minutos == "" or segundos == "":
            messagebox.showerror(message = 'Deben ingresar todo: las horas, '+\
                                 'los minutos y los segundos. No se '+\
                                 'guardaron los datos.')
        elif not horas.isdigit() or not minutos.isdigit() or \
             not segundos.isdigit():
            messagebox.showerror(message = 'Las horas, minutos y segundos '+\
                                 'deben ser números enteros. No se '+\
                                 'guardaron los datos.')
        elif not 0 <= int(horas) <= 2 or not 0 <= int(minutos) <= 59 or not\
             0 <= int(segundos) <= 59:
            messagebox.showerror(message = 'Las horas deben estar entre '+\
                                 '0 y 2, los minutos entre 0 y 59 y los '+\
                                 'segundos entre 0 y 59. No se guardaron'+\
                                 ' los datos.')
        elif not 0 < int(horas) and not 0 < int(minutos) and\
             not 0 < int(segundos):
            messagebox.showerror(message = 'Para el uso del Timer, alguna '+\
                                 'de sus partes (horas, minutos, segundos)'+\
                                 ' debe ser mayor a 0.')
        else:
            #si todo está bien, convierte los datos a enteros
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)

            #Guarda los datos de la configuración
            configArchivo = open("futoshiki2020configuración.dat", "wb")
            configUsuario = [nivel, reloj, panel, horas, minutos, segundos]
            pickle.dump(configUsuario, configArchivo)
            configArchivo.close()
            
            #Mensaje de confirmación
            messagebox.showinfo(message = 'Se ha guardado éxitosamente')
    else:
        if horas != "" or minutos != "" or segundos != "":
            messagebox.showerror(message = 'Si no escogió Timer, debe dejar'+\
                                 ' las horas, minutos y segundos en blanco.'+\
                                 ' No se guardaron los datos.')
        else:
            #Guarda los datos de la configuración
            configArchivo = open("futoshiki2020configuración.dat", "wb")
            configUsuario = [nivel, reloj, panel, horas, minutos, segundos]
            pickle.dump(configUsuario, configArchivo)
            configArchivo.close()
            
            #Mensaje de confirmación
            messagebox.showinfo(message = 'Se ha guardado éxitosamente')

    
def configurar(ventanaMenu):
    '''Despliega la ventana de configuración y todos los
    widgets dentro de ella.'''
    #cierra la ventana anterior
    ventanaMenu.destroy()

    #despliega la ventana Configuración
    ventanaConfig = Tk()
    ventanaConfig.geometry('600x600+350+20')
    ventanaConfig.title('Configuración')
    ventanaConfig.resizable(width=False, height=False)
    ventanaConfig.config(bg='white')

    labelConfig = Label(ventanaConfig, text='Configuración')
    labelConfig.place(relx=0.5, rely=0.1, anchor=CENTER)
    labelConfig.config(bg='white', font=('Cooper Black', 23),
                       fg='indian red')

    #Lee la lista de configuración para mostrar los datos marcados
    configArchivo = open("futoshiki2020configuración.dat", "rb")
    config = pickle.load(configArchivo)
    configArchivo.close()

    #NIVEL
    labelNivel = Label(ventanaConfig, text='Nivel: ', anchor=W, justify=LEFT)
    labelNivel.place(relx=0.3, rely=0.18)
    labelNivel.config(bg='white', font=('Nunito Black', 12), fg='indian red')
    
    nivel = IntVar(value=config[0])
    nivelBoton1 = Radiobutton(ventanaConfig, text='Fácil', width=8, anchor=W,\
                              justify=LEFT, variable=nivel, value=1)
    nivelBoton1.place(relx=0.4, rely=0.22)
    nivelBoton2 = Radiobutton(ventanaConfig, text='Intermedio', width=8,\
                              anchor=W, justify=LEFT, variable=nivel, value=2)
    nivelBoton2.place(relx=0.4, rely=0.27)
    nivelBoton3 = Radiobutton(ventanaConfig, text='Difícil', width=8,\
                              anchor=W, justify=LEFT, variable=nivel, value=3)
    nivelBoton3.place(relx=0.4, rely=0.32)

    #TIMER
    labelHoras = Label(ventanaConfig, text='Horas: ', anchor=W, justify=LEFT)
    labelHoras.place(relx=0.6, rely=0.5)
    horas = Entry(ventanaConfig, state=DISABLED)
    horas.place(relx=0.6, rely=0.55, width='40')

    labelMin = Label(ventanaConfig, text='Min: ', anchor=W, justify=LEFT)
    labelMin.place(relx=0.7, rely=0.5)
    minutos = Entry(ventanaConfig, state=DISABLED)
    minutos.place(relx=0.7, rely=0.55, width='40')

    labelSeg = Label(ventanaConfig, text='Seg: ', anchor=W, justify=LEFT)
    labelSeg.place(relx=0.8, rely=0.5)
    segundos = Entry(ventanaConfig, state=DISABLED)
    segundos.place(relx=0.8, rely=0.55, width='40')
    if config[1] == 3:  #activa el timer y muestra el tiempo configurado
        activar_timer(horas, minutos, segundos)
        horas.insert(0, config[3])
        minutos.insert(0, config[4])
        segundos.insert(0, config[5])

    #Configuración visual Timer
    listaEntradas = [horas, minutos, segundos]
    for entrada in listaEntradas:
        entrada.config(bg='papaya whip')
    listaTimer = [labelHoras, labelMin, labelSeg]
    for etiqueta in listaTimer:
        etiqueta.config(bg='white', font=('Nunito', 10),
                        fg='indian red')

    #RELOJ
    labelReloj = Label(ventanaConfig, text='Reloj: ', anchor=W, justify=LEFT)
    labelReloj.place(relx=0.3, rely=0.4)
    labelReloj.config(bg='white', font=('Nunito Black', 12), fg='indian red')
    
    reloj = IntVar(value=config[1])
    relojBoton1 = Radiobutton(ventanaConfig, text='Sí', width=8, anchor=W,\
                              justify=LEFT, variable=reloj, value=1,
                              command=lambda:desactivar_timer(horas,\
                                                              minutos,\
                                                              segundos))
    relojBoton1.place(relx=0.4, rely=0.45)
    relojBoton2 = Radiobutton(ventanaConfig, text='No', width=8, anchor=W,\
                              justify=LEFT, variable=reloj, value=2,
                              command=lambda:desactivar_timer(horas,\
                                                              minutos,\
                                                              segundos))
    relojBoton2.place(relx=0.4, rely=0.5)
    relojBoton3 = Radiobutton(ventanaConfig, text='Timer', width=8, anchor=W,\
                              justify=LEFT, variable=reloj, value=3,
                              command=lambda:activar_timer(horas,\
                                                           minutos,\
                                                           segundos))
    relojBoton3.place(relx=0.4, rely=0.55)


    #POSICIÓN PANEL DE DÍGITOS
    labelPanel = Label(ventanaConfig, text='Posición del panel de dígitos: ',\
                       anchor=W, justify=LEFT)
    labelPanel.place(relx=0.3, rely=0.65)
    labelPanel.config(bg='white', font=('Nunito Black', 12), fg='indian red')
    
    panel = IntVar(value=config[2])
    panelBoton1 = Radiobutton(ventanaConfig, text='Derecha', width=8,\
                              anchor=W, justify=LEFT, variable=panel, value=1)
    panelBoton1.place(relx=0.4, rely=0.7)
    panelBoton2 = Radiobutton(ventanaConfig, text='Izquierda',width=8,\
                              anchor=W, justify=LEFT, variable=panel, value=2)
    panelBoton2.place(relx=0.4, rely=0.75)

    #Configuración visual de botones de selección
    listaRadios = [nivelBoton1, nivelBoton2, nivelBoton3, relojBoton1,
                   relojBoton2, relojBoton3, panelBoton1, panelBoton2]
    for boton in listaRadios:
        boton.config(bg='white', font=('Nunito Bold', 10),
                     fg='grey30')


    #GUARDAR CONFIGURACIÓN
    guardarBoton = Button(ventanaConfig, text='Guardar configuración',
                          command=lambda:comprobar_datos(nivel.get(),
                                                         reloj.get(),
                                                         panel.get(),
                                                         horas.get(),
                                                         minutos.get(),
                                                         segundos.get(),
                                                         ventanaConfig))
    guardarBoton.place(relx=0.5, rely=0.9, anchor=CENTER)
    guardarBoton.config(bg='indian red', font=('Nunito Black', 12),
                        fg='papaya whip', width=18, height=1,
                        activebackground='papaya whip', activeforeground='indian red')
    
    #Botón para regresar al Menú Principal
    regresarBoton = Button(ventanaConfig, text='Regresar',\
                           command=lambda:regresarCF(ventanaConfig))
    regresarBoton.place(relx=0.95, rely=0.05, anchor=NE)
    regresarBoton.config(bg='papaya whip', font=('Nunito Black', 10),
                         fg='indian red', width=8, height=1,
                         activebackground='indian red', activeforeground='papaya whip')

    #Mantiene el evento abierto
    ventanaConfig.mainloop()
    
#Ayuda-------------------------------------------------------------------------
    
def ayuda():
    #Despliega el Manual del Usuario
    os.startfile("manual_de_usuario_futoshiki_v2.pdf")
    
#Acerca de---------------------------------------------------------------------

def regresarAD(ventanaAcercaDe):
    '''Cierra la ventana Acerca de y abre el Menú.'''
    ventanaAcercaDe.destroy()
    menuPrincipal()

def acercaDe(ventanaMenu):
    '''Despliega la ventana Acerca De y todo el texto en ella.'''
    #cierra la ventana anterior
    ventanaMenu.destroy()
    
    #despliega la ventana Acerca de
    ventanaAcercaDe = Tk()
    ventanaAcercaDe.geometry('600x600+350+20')
    ventanaAcercaDe.title('Acerca de')
    ventanaAcercaDe.resizable(width=False, height=False)
    ventanaAcercaDe.config(bg='white')

    labelAcercaDe = Label(ventanaAcercaDe, text='Acerca de')
    labelAcercaDe.place(relx=0.5, rely=0.15, anchor=CENTER)
    labelAcercaDe.config(bg='white', font=('Cooper Black', 23),
                         fg='indian red')

    labelInfo = Label(ventanaAcercaDe, text='Futoshiki©\n\nV.1.0\n\nJulio, '+
                      '2020\n\nDesarrollado por: Pamela Dinarte Chavarría')
    labelInfo.place(relx=0.5, rely=0.3, anchor=N)
    labelInfo.config(bg='white', font=('Nunito Bold', 13), fg='grey30')

    #Botón para regresar al Menú Principal
    regresarBoton = Button(ventanaAcercaDe, text='Regresar',\
                           command=lambda:regresarAD(ventanaAcercaDe))
    regresarBoton.place(relx=0.95, rely=0.05, anchor=NE)
    regresarBoton.config(bg='papaya whip', font=('Nunito Black', 10),
                         fg='indian red', width=8, height=1,
                         activebackground='indian red', activeforeground='papaya whip')

    #Mantiene el evento abierto
    ventanaAcercaDe.mainloop()
    
#Salir-------------------------------------------------------------------------
    
def salir(ventanaMenu):
    ventanaMenu.destroy()
    
#Jugar-------------------------------------------------------------------------

def regresarJG(ventanaJugar):
    '''Cierra la ventana Jugar y abre el Menú.'''
    respuesta = messagebox.askyesno(message='¿Está seguro que desea salir? '+
                                    'Si no ha guardado la partida sus datos '+
                                    'se perderán.')
    if respuesta:
        global tiempo_corriendo
        global cronoS
        cronoS.after_cancel(tiempo_corriendo)
        ventanaJugar.destroy()
        menuPrincipal()

def corre_adelante(cronoM, cronoH):
    '''Corre el tiempo hacia adelante mientras la global corriendo
    se lo indique.
    Entradas: referencias a la etiqueta de minutos y a la de horas.
    Salidas: Cambia el valor de las globales de segundos, minutos y horas.'''

    global tiempo_corriendo
    global corriendo
    global h
    global m
    global s 

    if corriendo:   #hace cambios en el tiempo
        #cambia el minuto cuando pasen 60 segundos
        if s == 60:
            s = 0
            m += 1
        cronoM['text'] = str(m)
        
        #cambia la hora cuando pasen 60 minutos
        if m == 60:
            m = 0
            h += 1
        cronoH['text'] = str(h)
        
        #cambia el segundo
        cronoS['text'] = str(s)
        s += 1
        tiempo_corriendo = cronoS.after(1000, corre_adelante, cronoM, cronoH) 
    else:
        tiempo_corriendo = cronoS.after(1000, corre_adelante, cronoM, cronoH)
        

def corre_atras(cronoM, cronoH, hO, mO, sO,
                ventanaJugar, i_faciles, i_interme, i_difiles, i_partida):
    '''Corre el tiempo hacia atrás, como un temporizador mientras la global
    corriendo se lo indique.
    Entradas: referencias a las etiquetas de tiempo; las h, m y s iniciales;
    la ventana donde se despliega y todos los parámetros necesarios para
    llamar a la función jugar.
    Salidas: modifica las globales de h, m y s.'''

    global tiempo_corriendo 
    global corriendo
    global h 
    global m
    global s 

    if corriendo:  #hace cambios en el tiempo
        cronoS['text'] = str(s)
        if h == 0 and m == 0 and s == 0:
            respuesta = messagebox.askyesno(message='Tiempo expirado. ¿Desea '+
                                            'continuar el mismo juego?')
            #revisa la respuesta
            if respuesta == True:
                #comienza a correr el reloj desde el tiempo establecido para Timer
                h = hO
                m = mO
                s = sO
                corre_adelante(cronoM, cronoH)
            else:
                #devuelve a Jugar
                jugar(ventanaJugar, i_faciles, i_interme, i_difiles, False, i_partida, False)
        else:
            cronoM['text'] = str(m)
            cronoH['text'] = str(h)

            if s == 0:
                s = 60
                m -= 1
            if m == -1:
                m = 59
                h -= 1
            if h == -1:
                h = 0
                m = 0

            #cambia el segundo
            s -= 1
            tiempo_corriendo = cronoS.after(1000, corre_atras, cronoM, cronoH, hO, mO, sO,
                                            ventanaJugar, i_faciles, i_interme, i_difiles, i_partida)
    else:
        tiempo_corriendo = cronoS.after(1000, corre_atras, cronoM, cronoH, hO, mO, sO,
                                        ventanaJugar, i_faciles, i_interme, i_difiles, i_partida)

def tiempo_invisible():
    '''Corre el tiempo hacia adelante mientras la global corriendo
    se lo indique pero sin mostarlo en pantalla.
    Entradas: no recibe entradas, pero se declaran las globales que
    serán modificadas.
    Salidas: modifica las globales de h, m, s.'''
    
    #Globales para modificar
    global tiempo_corriendo
    global corriendo
    global cronoS
    global h
    global m
    global s

    if corriendo: #hace cambios 
        #cambia el minuto cuando pasen 60 segundos
        if s == 60:
            s = 0
            m += 1
        
        #cambia la hora cuando pasen 60 minutos
        if m == 60:
            m = 0
            h += 1
        
        #cambia el segundo
        s += 1    #cuando se pare el tiempo va a salir un segundo de más
        tiempo_corriendo = cronoS.after(1000, tiempo_invisible)
    else:
        tiempo_corriendo = cronoS.after(1000, tiempo_invisible)


################################################################################
def detener_tiempo():
    '''Modifica la global corriendo para que se detenga el tiempo.
    Entradas: no recibe.
    Salidas: modifica la global corriendo para que el tiempo pare.'''
    
    #Detiene el tiempo corriendo
    global tiempo_corriendo
    global corriendo

    #pausa el tiempo
    corriendo = False
    #cronoS.after_cancel(tiempo_corriendo)

def reanudar_tiempo():
    '''Modifica la global corriendo para que el tiempo siga.
    Entradas: no recibe.
    Salidas: modifica la global corriendo.'''
    
    #Sigue corriendo el tiempo
    global corriendo
    corriendo = True
################################################################################    

def habilitar_juego(ventanaJugar, nombre, borrarJugadaBoton, terminarBoton,
                    borrarBoton, refCasillas, refDigitos, iniciarBoton,
                    nombreEntry, reloj, i_faciles, i_interme, i_difiles, i_partida,
                    guardarBoton, cargarBoton, hO, mO, sO):
    '''Habilita todas los widgets que pueden ser utilizados durante la partida
    y deshabilita todo lo que no puede ser usado.
    Entradas: referencias a todos los widgets que necesita habilitar/deshabilitar
    y todas los parámetros necesario para llamar a las funciones de tiempo.
    Salidas: mensajes de error y modifica el estado de los widgets de
    la ventanaJugar.'''
    
    if nombre == "":
        messagebox.showerror(message = 'Debe ingresar un nombre antes '+\
                             'de inciar la partida.')
    elif not 1 <= len(nombre) <= 20:
        messagebox.showerror(message = 'El nombre debe tener entre 1 y 20 '+\
                             'caracteres.')
    else:                             
        #habilita los botones que se pueden usar durante la partida
        borrarJugadaBoton['state'] = NORMAL
        terminarBoton['state'] = NORMAL
        borrarBoton['state'] = NORMAL
        guardarBoton['state'] = NORMAL
        for casilla in refCasillas:
            casilla['state'] = NORMAL
        for digito in refDigitos:
            digito['state'] = NORMAL

        #desabilita los que ya no se pueden usar
        iniciarBoton['state'] = DISABLED
        nombreEntry['state'] = DISABLED
        cargarBoton['state'] = DISABLED

        #se declaran las globales para modificarlas por referencia
        global cronoS
        global h
        global m
        global s

        #despliega el reloj
        if reloj != 2:
            hLabel = Label(ventanaJugar, text='Horas')
            hLabel.place(relx=0.05, rely=0.87)
            minLabel = Label(ventanaJugar, text='Min')
            minLabel.place(relx=0.15, rely=0.87)
            segLabel = Label(ventanaJugar, text='Seg')
            segLabel.place(relx=0.23, rely=0.87)

            cronoS = Label(ventanaJugar, text=str(s))
            cronoS.place(relx=0.25, rely=0.92)

            cronoM = Label(ventanaJugar, text=str(m))
            cronoM.place(relx=0.18, rely=0.92)

            cronoH = Label(ventanaJugar, text=str(h))
            cronoH.place(relx=0.09, rely=0.92)

            #Config visual del reloj
            listaLabels = [hLabel, minLabel, segLabel]
            for etiqueta in listaLabels:
                etiqueta.config(bg='papaya whip', font=('Cooper Black', 10),
                                fg='indian red', bd=5, padx=5)
            listaReloj = [cronoS, cronoM, cronoH]
            for etiqueta in listaReloj:
                etiqueta.config(bg='white', font=('Cooper Black', 10),
                                fg='indian red')

            #comienza a correr el tiempo
            if reloj == 1:
                corre_adelante(cronoM, cronoH)
            elif reloj == 3:
                corre_atras(cronoM, cronoH, hO, mO, sO, 
                            ventanaJugar, i_faciles, i_interme, i_difiles,
                            i_partida)
        else:
            #Mide el tiempo pero sin mostrarlo
            cronoS = Label(ventanaJugar)
            tiempo_invisible()


def mensaje_casilla_fija(refCasillas, valorCasilla):
    '''Indica al usuario si la casilla que tocó posee un número fijo.
    Entradas: la lista de referencias de botones casilla para poder
    cambiar el color y el índica de la casilla que debe cambiar.
    Salidas: mensaje de error y modifica el color de la casilla.'''
    
    i_casilla = valorCasilla - 1
    #Aqui se pone roja la casilla
    refCasillas[i_casilla]['selectcolor'] = 'red'

    #Envía el mensaje de error
    messagebox.showerror(message = 'La jugada no es válida porque '+
                         'este es un dígito fijo')

    #Vuelve a su color normal
    refCasillas[i_casilla]['selectcolor'] = 'white'


def revisa_casillas(refCasillas, valorDig, valorCasilla):
    '''Indica si una jugada es válida o no.
    Entradas: la lista de referencias de botones casilla,
    el dígito que se quiere colocar y el índice de la casilla.
    Salidas: True si el dígito que se quiere poner no está ya en la fila
    y columna; si sí está, retorna False.'''
    
    i_casilla = valorCasilla - 1
    
    #Genera los indices de las casillas en la misma FILA
    i_fila = ()
    i_actual = i_casilla
    cant = 0 #el i de la casilla actual no se ha incluido
    while cant < 5:  #agrega todos los índices DE LA FILA
        if i_actual in [4,9,14,19,24]:  #son los límites de las filas
            i_fila += (i_actual,)   #lo agrego a la tupla
            i_actual -= 4 #me devuelvo al inicio de la fila restandole 4
        else:
            i_fila += (i_actual,)   #lo agrego a la tupla
            i_actual += 1 #avanzo al siguiente
        cant += 1
    i_fila = i_fila[1:]  #quito el actual porque no necesito revisarlo

    #Genera los indices de las casillas en la misma COLUMNA
    i_columna = ()
    i_actual = i_casilla
    cant = 0  #el i de la casilla actual no se ha incluido
    while cant < 5:
        if i_actual in [20,21,22,23,24]:  #son los límites de las columnas
            i_columna += (i_actual,)   #lo agrego a la tupla
            i_actual -= 20 #me devuelvo al inicio de la columna
        else:
            i_columna += (i_actual,)   #lo agrego a la tupla
            i_actual += 5
        cant += 1
    i_columna = i_columna[1:]  #quito el actual porque no necesito revisarlo

    #valida si ya está el número en la fila
    for i in i_fila:
        if refCasillas[i]['text'] == str(valorDig):
            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
            messagebox.showerror(message = 'La jugada no es válida porque el '+
                                 'elemento ya está en la fila.')
            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
            return False

    #valida si ya está el número en la columna
    for i in i_columna:
        if refCasillas[i]['text'] == str(valorDig):
            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
            messagebox.showerror(message = 'La jugada no es válida porque el '+
                                 'elemento ya está en la columna.')
            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
            return False
    return True


def revisa_desig(refCasillas, valorDig, valorCasilla, simbolos):
    '''Revisa que se cumplan las desigualdades en la casilla.
    Entradas: la lista de referencias a los botones casilla, el
    dígito a colocar, el índice de la casilla y la lista de símbolos.
    Salidas: si se cumplen desigualdades retorna False, de lo
    contrario True.'''

    i_casilla = valorCasilla - 1

    #indica las coordenadas de la casilla para buscarla en los símbolos
    if i_casilla in [0,1,2,3,4]:
        coord = (0, i_casilla)
    elif i_casilla in [5,6,7,8,9]:
        coord = (1, i_casilla - 5)
    elif i_casilla in [10,11,12,13,14]:
        coord = (2, i_casilla - 10)
    elif i_casilla in [15,16,17,18,19]:
        coord = (3, i_casilla - 15)
    elif i_casilla in [20,21,22,23,24]:
        coord = (4, i_casilla - 20)

    #guarda todos los simbolos de la casilla
    simbolosCasilla = ()
    c = 0
    for tupla in simbolos:
        if tupla[1] == coord:
            simbolosCasilla += (tupla[0],)
            c += 1
        if c == 2:
            break
    
    #revisa las desigualdades de la DER Y ABAJO
    #si no hay, simplemente se salta esta parte
    for simbolo in simbolosCasilla:

        #revisa que si la casilla de la der tiene número, si no, se lo salta
        if simbolo == '>':
            if refCasillas[i_casilla+1]['text'] != '':
                #Compara el dígito que se quiere poner con el de la casilla de la izq
                if valorDig < int(refCasillas[i_casilla+1]['text']):  #está mal
                    refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                    messagebox.showerror(message = 'La jugada no es válida porque no '+
                                         'cumple la restricción de mayor.')
                    refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                    return False

        elif simbolo == '<':
            if refCasillas[i_casilla+1]['text'] != '':
                if valorDig > int(refCasillas[i_casilla+1]['text']):  #está mal
                    refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                    messagebox.showerror(message = 'La jugada no es válida porque no '+
                                         'cumple la restricción de menor.')
                    refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                    return False
    
            #si no hay casilla a la der, tampoco hay simbolo a la der

        #revisa que si la casilla de abajo tiene número, si no, se lo salta
        if simbolo == '˄':
            if refCasillas[i_casilla+5]['text'] != '':
                #Compara el dígito que se quiere poner con el de la casilla de abajo
                if valorDig > int(refCasillas[i_casilla+5]['text']):  #está mal
                    refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                    messagebox.showerror(message = 'La jugada no es válida porque no '+
                                         'cumple la restricción de menor.')
                    refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                    return False

        elif simbolo == '˅':
            if refCasillas[i_casilla+5]['text'] != '':
                if valorDig < int(refCasillas[i_casilla+5]['text']):  #está mal
                    refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                    messagebox.showerror(message = 'La jugada no es válida porque no '+
                                         'cumple la restricción de menor.')
                    refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                    return False
        
                #si no hay casilla abajo, tampoco hay simbolo abajo


    #verifica la desigualdad de la IZQ
    coordIzq = (coord[0], coord[1]-1) #busca la coord anterior
    for tupla in simbolos:  #busca el simbolo
        if tupla[1] == coordIzq:
            if tupla[0] in ['>', '<']:
                simboloIzq = tupla[0]
                
                #revisa el simbolo de la izq
                if simboloIzq == '>':
                    #revisa si hay un número en la casilla de la IZQ
                    if refCasillas[i_casilla-1]['text'] != '':
                        if int(refCasillas[i_casilla-1]['text']) < valorDig:
                            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                            messagebox.showerror(message = 'La jugada no es válida porque no '+
                                                 'cumple la restricción de menor.')
                            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                            return False
                elif simboloIzq == '<':
                    #revisa si hay un número en la casilla de la IZQ
                    if refCasillas[i_casilla-1]['text'] != '':
                        if int(refCasillas[i_casilla-1]['text']) > valorDig:
                            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                            messagebox.showerror(message = 'La jugada no es válida porque no '+
                                                 'cumple la restricción de mayor.')
                            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                            return False
                break


    #verifica la desigualdad de ARRIBA
    coordArriba = (coord[0]-1, coord[1])
    for tupla in simbolos: #busca el simbolo de arriba
        if tupla[1] == coordArriba:
            if tupla[0] in ['˄', '˅']:
                simboloArriba = tupla[0]

                #revisa el simbolo de arriba
                if simboloArriba == '˄':
                    #revisa si hay un número en la casilla de ARRIBA
                    if refCasillas[i_casilla-5]['text'] != '':
                        if int(refCasillas[i_casilla-5]['text']) > valorDig:
                            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                            messagebox.showerror(message = 'La jugada no es válida porque no '+
                                                 'cumple la restricción de mayor.')
                            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                            return False   
                elif simboloArriba == '˅':
                    #revisa si hay un número en la casilla de ARRIBA
                    if refCasillas[i_casilla-5]['text'] != '':
                        if int(refCasillas[i_casilla-5]['text']) < valorDig:
                            refCasillas[i_casilla]['selectcolor'] = 'red' #se pone roja
                            messagebox.showerror(message = 'La jugada no es válida porque no '+
                                                 'cumple la restricción de menor.')
                            refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
                            return False
                break
    return True


def juegoCompletado(ventanaJugar, reloj, hO, mO, sO, nivel, nombre,
                    i_faciles, i_interme, i_difiles, i_partida):
    '''Envía el mensaje de felicitación, calcula el tiempo de juego,
    revisa si el jugador entra en el top10 y lo guarda.
    Entradas: ventanaJugar para cerrarla, el tipo de reloj escogido y
    el tiempo original para calcular el tiempo de juego y el nivel
    y nombre para registrar en el top10.'''
    
    #Detiene el tiempo completamente
    global tiempo_corriendo
    global cronoS
    global h
    global m
    global s
    cronoS.after_cancel(tiempo_corriendo)

    #Muestra el mensaje de felicitación
    mensajeFinal = messagebox.showinfo(message = '¡Excelente! Juego terminado con éxito.')

    #Calcula el tiempo si era Timer
    if reloj == 3:
        if h > hO or (h == hO and m > mO) or (h == hO and m == mO and s > sO):
            #se acabó el tiempo y corrió el reloj
            #deja el tiempo como está
            s -= 1 #cuando el reloj frene va a tener un s de más

        else:
            #Cuando el timer frene va a tener un s de más
            s += 1
            
            #convierte el tiempo original a segundos
            inicio = hO*3600 + mO*60 + sO

            #convierte el tiempo final a segundos
            final = h*3600 + m*60 + s


            #se resta para saber cuantos segundos transcurrieron
            total = inicio - final

            #se convierte de nuevo a h, m y s
            h = total // 3600
            total = total % 3600
            m = total // 60
            s =  total % 60
    else:
        s -= 1 #cuando el reloj frene va a tener un s de más

    #Lee el archivo donde se registra el top10
    registro = open('futoshiki2020top10.dat', 'rb')
    registroDific = pickle.load(registro)
    registroInter = pickle.load(registro)
    registroFacil = pickle.load(registro)
    registro.close()

    #Indica en que lista se debe registrar
    if nivel == 1:
        listaMarcas = registroFacil
    elif nivel == 2:
        listaMarcas = registroInter
    else:
        listaMarcas = registroDific

    #Busca si el jugador entra en el registro
    posicion = 0
    huboCambios = False
    
    for marca in listaMarcas:
        #revisa si superó a alguien
        if h < marca[1] or (h == marca[1] and m < marca[2]) or (h == marca[1] and m == marca[2] and s <= marca[3]):
            listaMarcas.insert(posicion, (nombre, h, m, s))  #inserta la nueva marca
            huboCambios = True
            break
        posicion += 1
        
    #Si no superó a nadie, la inserta al final
    if not huboCambios:
        listaMarcas.insert(11, (nombre, h, m, s))  #inserta la nueva marca
        huboCambios = True
        
    #Revisa si hay que eliminar uno
    if len(listaMarcas) > 10:
        del listaMarcas[-1]

    #Se graban las 3 listas de vuelta en el archivo
    if huboCambios:
        if nivel == 1:
            registroFacil = listaMarcas
        elif nivel == 2:
            registroInter = listaMarcas
        else:
            registroDific = listaMarcas
        
        registro = open('futoshiki2020top10.dat', 'wb')
        pickle.dump(registroDific, registro)
        pickle.dump(registroInter, registro)
        pickle.dump(registroFacil, registro)
        registro.close()

    #Vuelve a ventana Jugar
    jugar(ventanaJugar, i_faciles, i_interme, i_difiles, False, i_partida, False)


def poner_numero(ventanaJugar, refCasillas, valorDig, valorCasilla, simbolos, pJ,
                 reloj, hO, mO, sO, nivel, nombre, i_faciles, i_interme,
                 i_difiles, i_partida):
    '''Llama a las funciones que validan si el dígito se puede colocar,
    coloca el número y revisa si se completó el juego y llama a la función
    juegoCompletado.
    Entradas: la lista de referencias de casillas, el dígito y el índice
    de la casilla y todos los parámetros necesarios para llamar a las funciones
    casillasCorrectas, desigCorrectas y juegoCompletado.
    Salidas: mensaje de error y modifica el texto o color de la casilla.'''
    
    i_casilla = valorCasilla - 1
    #valida si ya se seleccionó un dígito
    if valorDig not in [1,2,3,4,5]:
        refCasillas[i_casilla]['selectcolor'] = 'red'  #se pone roja
        messagebox.showerror(message = 'Debe seleccionar un dígito antes '+
                             'de marcar la casilla.')
        refCasillas[i_casilla]['selectcolor'] = 'white' #vuelve el color a la normalidad
        return

    #llama a la función que revisa columna y fila
    casillasCorrectas = revisa_casillas(refCasillas, valorDig, valorCasilla)
    if not casillasCorrectas:  #si hubo error, sale de la función
        return

    #llama a la función que revisa las desigualdades
    desigCorrectas = revisa_desig(refCasillas, valorDig, valorCasilla, simbolos)
    if not desigCorrectas:  #si hubo error, sale de la función
        return
    
    #aparece el dígito ya validado
    refCasillas[i_casilla]['text'] = str(valorDig)

    #agrega la jugada en la pila de jugadas
    if i_casilla in pJ: #en caso de que la casilla ya estuviera llena
        pJ.remove(i_casilla)
    pJ.append(i_casilla)

    #revisa si se completó el juego y envía mensaje
    if len(pJ) == cantCasillas:
        juegoCompletado(ventanaJugar, reloj, hO, mO, sO, nivel, nombre,
                        i_faciles, i_interme, i_difiles, i_partida)


def borrarJugadaAnt(pJ, refCasillas):
    '''Elimina la última jugada en la pila de jugadas.
    Entradas, la pila de jugadas y la lista de referencias a casillas.
    Salidas: mensaje de error si ya no hay jugadas o modifica el
    texto de la casilla.'''
    
    #verifica si hay jugadas para borrar
    if pJ == []:
        #envía mensaje de error
        messagebox.showerror(message = 'No hay más jugadas para borrar.')
    else:
        #borra la última jugada
        i_casilla = pJ[-1]
        refCasillas[i_casilla]['text'] = ""
        del pJ[-1]


def terminarJuego(ventanaJugar, i_faciles, i_interme, i_difiles, i_partida, reinicio):
    '''Abre una nueva ventana de juego. Si es reinicio, se abre la misma partida,
    si no, se abre una partida diferente.
    Entradas: todos los parámetros necesarios para llamar a la funcipon jugar.
    Salidas: mensajes de confirmación.'''
    
    if reinicio:
        #Envía mensaje de SI/NO
        respuesta = messagebox.askyesno(message = '¿Está seguro de borrar el juego?')
    else:
        #Envía mensaje de SI/NO
        respuesta = messagebox.askyesno(message = '¿Está seguro de terminar el juego?')

    #revisa la respuesta
    if respuesta == True:
        jugar(ventanaJugar, i_faciles, i_interme, i_difiles, reinicio, i_partida, False)


############################################
def cerrarTop10(ventanaTop10, ventanaJugar):
    '''Cierra la ventana del top10 y reanuda el tiempo.
    Entradas: recibe la ventana que cierra y la ventana
    que abre de nuevo.'''
    
    #Cierra la ventana
    ventanaTop10.destroy()

    #Sube la ventana Jugar
    ventanaJugar.deiconify()
    
    #Reanuda el tiempo
    reanudar_tiempo()
############################################

def mostrar_registro(ventanaTop10, niveles, listaRegistro, posx, i):
    #itera los niveles y los muestra
    if niveles == ():
        return
    else:
        nivel = niveles[0]
        nivelLabel = Label(ventanaTop10, text=nivel)
        nivelLabel.place(rely=0.2, relx=posx, anchor=CENTER)
        nivelLabel.config(bg='papaya whip', font=('Cooper Black', 16),
                          fg='indian red')
        
        nombreLabel = Label(ventanaTop10, text='Jugador')
        nombreLabel.place(rely=0.26, relx=(posx-0.06), anchor=CENTER)
        nombreLabel.config(bg='white', font=('Nunito Black', 14),
                           fg='grey30')
        
        tiempoLabel = Label(ventanaTop10, text='Tiempo')
        tiempoLabel.place(rely=
                          0.26, relx=(posx+0.06), anchor=CENTER)
        tiempoLabel.config(bg='white', font=('Nunito Black', 14),
                           fg='grey30')

        #Llama a las funciones recursivas que generan el texto
        nombres = unir_nombres(listaRegistro[i], 0, 1)
        tiempos = unir_tiempos(listaRegistro[i], 0)

        #Coloca el texto
        nombreTexto = Label(ventanaTop10, text=nombres)
        nombreTexto.place(rely=0.3, relx=(posx-0.11), anchor=NW)
        nombreTexto.config(bg='white', font=('Nunito', 13),
                           fg='grey30', justify=LEFT)

        tiempoTexto = Label(ventanaTop10, text=tiempos)
        tiempoTexto.place(rely=0.3, relx=(posx+0.03), anchor=NW)
        tiempoTexto.config(bg='white', font=('Nunito', 13),
                           fg='grey30')

        #se llama de nuevo
        return mostrar_registro(ventanaTop10, niveles[1:], listaRegistro, posx+0.3, i+1)


def unir_nombres(marcas, i, posicion):
    if marcas == []:
        return ''
    elif i >= len(marcas):
        return ''
    else:
        nombre = str(posicion) + '. ' + marcas[i][0]
        return nombre + '\n' + unir_nombres(marcas, i+1, posicion+1)

def unir_tiempos(marcas, i):
    #itera las marcas
    if marcas == []:
        return ''
    elif i >= len(marcas):
        return ''
    else:
        h = marcas[i][1]
        m = marcas[i][2]
        s = marcas[i][3]
        if 0 <= h <= 9:
            h = '0' + str(h)
        else:
            h = str(h)
            
        if 0 <= m <= 9:
            m = '0' + str(m)
        else:
            m = str(m)

        if 0 <= s <= 9:
            s = '0' + str(s)
        else:
            s = str(s)
            
        tiempo = h + ':' + m + ':' + s
        return tiempo + '\n' + unir_tiempos(marcas, i+1)


def desplegarTop10(ventanaJugar):
    '''Abre la ventana del top10, detiene el tiempo y llama a la función
    recursiva que despliega los datos.
    Entradas: la ventana que hay que bajar.'''
    
    #Detiene el tiempo
    detener_tiempo()

    #Baja la ventana Jugar
    ventanaJugar.withdraw()

    #Despliega la ventana Top10
    ventanaTop10 = Tk()
    ventanaTop10.geometry('1200x600+80+20')
    ventanaTop10.title('Top 10')
    ventanaTop10.resizable(width=False, height=False)
    ventanaTop10.config(bg='white')

    labelTop10 = Label(ventanaTop10, text='Top 10')
    labelTop10.place(relx=0.5, y=60, anchor=CENTER)
    labelTop10.config(bg='white', font=('Cooper Black', 23),
                      fg='indian red')

    #Pone las etiquetas de nivel
    niveles = ('Nivel Difícil', 'Nivel Intermedio', 'Nivel Fácil')

    #Lee el archivo top10
    registro = open('futoshiki2020top10.dat', 'rb')
    registroDific = pickle.load(registro)
    registroInter = pickle.load(registro)
    registroFacil = pickle.load(registro)
    registro.close()

    #Llama a la función recursiva
    listaRegistro = (registroDific, registroInter, registroFacil)
    posx = 0.2
    i = 0
    mostrar_registro(ventanaTop10, niveles, listaRegistro, posx, i)

    #Le cambia la función al botón X de la ventana
    ventanaTop10.protocol('WM_DELETE_WINDOW', lambda:cerrarTop10(ventanaTop10, ventanaJugar))
    
    #Mantiene el evento abierto
    ventanaTop10.mainloop()


def guardarPartida(nivel, reloj, panel, h, m, s, nombre,
                   i_partida, pJ, refCasillas, hO, mO, sO):
    '''Graba los datos de la partida en el siguiente orden:
            configuración: [nivel, reloj, panel, h, m, s]
            tiempo original:(hO, mO, sO)
            nombre: string con el nombre
            partida: entero con el indice de la partida en la lista de partidas predeterminadas
            jugadas: [(digito, indice_casilla), (3, 21), (5, 16)...]'''

    #Crea la lista de jugadas
    jugadas = []
    for i in pJ:  #toma la casilla que se llenó
        digito = refCasillas[i]['text']  #extrae el str(dígito) que se colocó en la jugada
        jugadas += [(digito, i)] #agrega el dígito y el índice de la casilla

    #Verifica si el Timer pasó a ser reloj
    if reloj == 3:
        s += 1
        if h > hO or (h == hO and m > mO) or (h == hO and m == mO and s >= sO):
            #significa que se acabó el Timer y comenzó el reloj,
            #hay que cambiar a modalidad reloj
            reloj = 1
            s -= 2
    else:
        s -= 1

    #Agrupa los datos de la config y tiempo original
    config = [nivel, reloj, panel, h, m, s]
    tiempoO = (hO, mO, sO)

    #Graba los datos de la partida
    partidaArchivo = open('futoshiki2020juegoactual.dat', 'wb')
    pickle.dump(config, partidaArchivo)
    pickle.dump(tiempoO, partidaArchivo)
    pickle.dump(nombre, partidaArchivo)
    pickle.dump(i_partida, partidaArchivo)
    pickle.dump(jugadas, partidaArchivo)
    partidaArchivo.close()


def cargarPartida(ventanaJugar, pJ, refNombre):
    '''Revisa si hay una partida guardada, extrae sus datos y llama
    a la función jugar para que los despliegue, indicándole que
    cargado = True. '''

    #Carga la info. de la partida
    try:
        partidaArchivo = open('futoshiki2020juegoactual.dat', 'rb')
    except:
        messagebox.showerror(message = 'No hay partida guardada.')
        return
    
    config = pickle.load(partidaArchivo)
    pickle.load(partidaArchivo) #no necesito el tiempo original aún
    pickle.load(partidaArchivo) #no necesito nombre
    i_partida = pickle.load(partidaArchivo)
    pickle.load(partidaArchivo) #no necesito jugadas
    partidaArchivo.close()

    #Graba la configuración en el archivo
    configArchivo = open('futoshiki2020configuración.dat', 'wb')
    pickle.dump(config, configArchivo)
    configArchivo.close()

    #Abre la ventana con el juego cargado
    jugar(ventanaJugar, i_faciles, i_interme, i_difiles, True, i_partida, True)

    
def jugar(ventanaMenu, i_faciles, i_interme, i_difiles, reinicio, i_partida, cargado):
    '''Despliega la ventana de juego con todos su widgets. Si reinicio = True,
    carga la partida que se le envía, si cargado = True, carga los datos de la
    partida guardada.
    Entradas:
            - la ventana anterior(para cerrarla)
            - las listas con los índices de las partidas ya utilizadas en la
            misma corrida del programa
            - reinicio: True/False si es necesario utilizar la misma partida
            - el índice de la partida en la lista de partidas
            - cargado: True/False si hay que cargar datos de una
            partida guardada. '''
    
    #cierra la ventana anterior
    ventanaMenu.destroy()
    
    #despliega la ventana Jugar
    ventanaJugar = Tk()
    ventanaJugar.geometry('600x600+350+20')
    ventanaJugar.title('Futoshiki')
    ventanaJugar.resizable(width=False, height=False)
    ventanaJugar.config(bg='white')

    labelJugar = Label(ventanaJugar, text='FUTOSHIKI')
    labelJugar.place(relx=0.5, rely=0.06, anchor=CENTER)
    labelJugar.config(bg='white', font=('Cooper Black', 15),
                      fg='indian red')


    #Si el juego está siendo cargado, obtiene los datos de la partida
    if cargado:
        #Carga la info. de la partida
        partidaArchivo = open('futoshiki2020juegoactual.dat', 'rb')
        configCargado = pickle.load(partidaArchivo)
        tiempoOCargado = pickle.load(partidaArchivo)
        nombreCargado = pickle.load(partidaArchivo)
        pickle.load(partidaArchivo) # no necesito i_partidaCargado
        jugadasCargado = pickle.load(partidaArchivo)
        partidaArchivo.close()

    #la pila de jugadas comienza vacía
    pJ = []
    if cargado:   #Recupera la pila de jugadas
        for jugada in jugadasCargado:
            pJ += [jugada[1]]

    #lee los datos de la configuración
    configArchivo = open("futoshiki2020configuración.dat", "rb")
    lista_config = pickle.load(configArchivo)
    configArchivo.close()

    #indica el nivel
    nivel = lista_config[0]
    if nivel == 1:
        nivel_config = "NIVEL FÁCIL"
    elif nivel == 2:
        nivel_config = "NIVEL INTERMEDIO"
    elif nivel == 3:
        nivel_config = "NIVEL DIFÍCIL"
    labelNivel = Label(ventanaJugar, text=nivel_config)
    labelNivel.place(relx=0.5, rely=0.12, anchor=CENTER)
    labelNivel.config(bg='white', font=('Nunito', 11),
                      fg='grey30')

    #permite introducir el nombre
    labelNombre = Label(ventanaJugar, text='Nombre del jugador:')
    labelNombre.place(relx=0.05, rely=0.15, anchor=W)
    labelNombre.config(bg='white', font=('Nunito Bold', 10),
                       fg='indian red')
    nombre = Entry(ventanaJugar)
    nombre.place(relx=0.5, rely=0.15, anchor=CENTER, width='250')
    nombre.config(bg='papaya whip')
    if cargado:
        nombre.insert(0, nombreCargado)

    #obtiene la lista de partidas según el nivel de la config
    lista_partidas = open("futoshiki2020partidas.dat","rb")
    for nivel_actual in range(1,4):
        partidas = pickle.load(lista_partidas) #conserva la lista de posibles partidas según el nivel de dificultad
        if nivel_actual == nivel:
            break
    lista_partidas.close()

    #si la ventana se abre desde el menú, toma una nueva partida
    if reinicio == False:
        #selecciona una partida de forma aleatoria    
        while True:
            i_partida = randint(0,2)
            if nivel == 1: #Fácil
                #Revisa si ya se usaron todas las partidas
                if len(i_faciles) == 3:
                    del i_faciles[0]
                    del i_faciles[0]
                    del i_faciles[0]
                    i_faciles += [i_partida]
                    break
                elif i_partida in i_faciles:
                    continue   #para que saque otro índice
                else:
                    i_faciles += [i_partida]
                    break
            elif nivel == 2: #Intermedio
                if len(i_interme) == 3:
                    del i_interme[0]
                    del i_interme[0]
                    del i_interme[0]
                    i_interme += [i_partida]
                    break
                elif i_partida in i_interme:
                    continue   #para que saque otro índice
                else:
                    i_interme += [i_partida]
                    break
            elif nivel == 3: #Difícil
                if len(i_difiles) == 3:
                    del i_difiles[0]
                    del i_difiles[0]
                    del i_difiles[0]
                    i_difiles += [i_partida]
                    break
                elif i_partida in i_difiles:
                    continue   #para que saque otro índice
                else:
                    i_difiles += [i_partida]
                    break
                
    #si se abre desde Boton Borrar Juego, se abre la partida enviada
            
    #extrae la partida random de la lista
    partida = partidas[i_partida]

    #extrae dónde tienen que ir números
    numeros_fijos = ()
    for tupla in partida:
        if isinstance(tupla[0], int):
            numeros_fijos += (tupla,)
            
    #extrae dónde tienen que ir símbolos
    simbolos = ()
    for tupla in partida:
        if isinstance(tupla[0], str):
            simbolos += (tupla,)


    #despliega el panel de dígitos
    panel = lista_config[2]
    if panel == 1: #derecha
        posXpanel = 0.85
    elif panel == 2: #izquierda
        posXpanel = 0.12

    refDigitos = []
    posYboton = 0.21
    valorDig = IntVar() #aquí se guarda el dígito que estoy usando
    for digito in range(1,6):
        digitoBoton = Radiobutton(ventanaJugar, text=str(digito), state=DISABLED,
                                  variable=valorDig, value=digito, selectcolor='DarkOliveGreen3',
                                  indicatoron=False, activebackground='papaya whip',
                                  activeforeground='indian red')
        digitoBoton.place(relx=posXpanel, rely=posYboton)
        digitoBoton.config(bg='indian red', font=('Cooper Black', 14),
                           fg='papaya whip', width=1, height=1)
        refDigitos += [digitoBoton]
        posYboton += 0.1

    #Obtiene los s, m, h para el reloj
    global h
    global m
    global s
    reloj = lista_config[1]
    if reloj == 1 or reloj == 2: #empieza en ceros
        s = 0
        m = 0
        h = 0
    elif reloj == 3:  #empieza en el tiempo especificado
        s = lista_config[5]
        m = lista_config[4]
        h = lista_config[3]
    if cargado: 
        #para que el reloj/ comience donde lo dejaron
        h = configCargado[3]
        m = configCargado[4]
        s = configCargado[5]
        

    #Guarda los valores originales del reloj
    hO = h
    mO = m
    sO = s
    if cargado: 
        hO = tiempoOCargado[0]
        mO = tiempoOCargado[1]
        sO = tiempoOCargado[2]

    #despliega la cuadrícula 5x5
    global cantCasillas
    cantCasillas = 0
    
    refCasillas = []  #aquí se guardan las referencias a las casillas
    valorCasilla = IntVar()
    valorNumericoCas = 1
    relYcasilla = 0.2
    for f in range(0,5):  #obtiene las coordenadas de la casilla
        relXcasilla = 0.27
        for c in range(0,5):
            colocado = False
            for tupla in numeros_fijos:  #busca si en esas coordenadas hay que poner un número fijo
                if (f,c) in tupla:
                    casillaFija = Radiobutton(ventanaJugar, text=str(tupla[0]),
                                              state=DISABLED, width=4, height=2,
                                              variable=valorCasilla,
                                              value=valorNumericoCas,
                                              indicatoron=False,
                                              command=lambda:mensaje_casilla_fija(refCasillas,
                                                                                  valorCasilla.get()))
                    casillaFija.place(relx=relXcasilla, rely=relYcasilla)
                    colocado = True
                    refCasillas += [casillaFija]
                    valorNumericoCas += 1
                    break
            if not colocado:
                casilla = Radiobutton(ventanaJugar, width=4, height=2,
                                      state=DISABLED, variable=valorCasilla,
                                      value=valorNumericoCas,
                                      indicatoron=False,
                                      command=lambda:poner_numero(ventanaJugar,
                                                                  refCasillas,
                                                                  valorDig.get(),
                                                                  valorCasilla.get(),
                                                                  simbolos,
                                                                  pJ,
                                                                  reloj,
                                                                  hO, mO, sO,
                                                                  nivel,
                                                                  nombre.get(),
                                                                  i_faciles,
                                                                  i_interme,
                                                                  i_difiles,
                                                                  i_partida))###################################################
                casilla.place(relx=relXcasilla, rely=relYcasilla)
                cantCasillas += 1
                refCasillas += [casilla]
                valorNumericoCas += 1
            relXcasilla += 0.1
        relYcasilla += 0.11

    #Config visual de casillas
    for casilla in refCasillas:
        casilla.config(bg='papaya whip', font=('Nunito', 9),
                       fg='indian red', height=2)


    #coloca los símbolos en la cuadrícula
    for tupla in simbolos:
        caracter = tupla[0]
        numFil = tupla[1][0]
        numCol = tupla[1][1]
        
        if caracter == '>' or caracter == '<':
            if numFil == 0:   #obtiene la pos en Y
                relYsimbolo = 0.218
            elif numFil == 1:
                relYsimbolo = 0.32
            elif numFil == 2:
                relYsimbolo = 0.435
            elif numFil == 3:
                relYsimbolo = 0.55
            elif numFil == 4:
                relYsimbolo = 0.65

            if numCol == 0:   #obtiene la pos en X
                relXsimbolo = 0.34
            elif numCol == 1:
                relXsimbolo = 0.44
            elif numCol == 2:
                relXsimbolo = 0.54
            elif numCol == 3:
                relXsimbolo = 0.64
            elif numCol == 4:
                relXsimbolo = 0.74

        elif caracter == '˅' or caracter == '˄':
            if numFil == 0:   #obtiene la pos en Y
                relYsimbolo = 0.272
            elif numFil == 1:
                relYsimbolo = 0.382
            elif numFil == 2:
                relYsimbolo = 0.491
            elif numFil == 3:
                relYsimbolo = 0.6
            elif numFil == 4:
                relYsimbolo = 0.707

            if numCol == 0:   #obtiene la pos en X
                relXsimbolo = 0.29
            elif numCol == 1:
                relXsimbolo = 0.39
            elif numCol == 2:
                relXsimbolo = 0.49
            elif numCol == 3:
                relXsimbolo = 0.59
            elif numCol == 4:
                relXsimbolo = 0.69

        simbolo = Label(ventanaJugar, text=caracter)
        simbolo.place(relx=relXsimbolo, rely=relYsimbolo)
        simbolo.config(bg='white', font=(12), fg='grey30')

    if cargado: 
        #Coloca los números que se habían colocado en el juego que se cargó
        for jugada in jugadasCargado:
            digito = jugada[0]
            casilla = jugada[1]
            refCasillas[casilla]['text'] = digito  #ya viene como str
        
            
    #despliega los botones de la parte inferior
    iniciarBoton = Button(ventanaJugar, text='Iniciar juego',
                          command=lambda:habilitar_juego(ventanaJugar,
                                                         nombre.get(),
                                                         borrarJugadaBoton,
                                                         terminarBoton,
                                                         borrarBoton,
                                                         refCasillas,
                                                         refDigitos,
                                                         iniciarBoton,
                                                         nombre,
                                                         reloj,
                                                         i_faciles,
                                                         i_interme,
                                                         i_difiles,
                                                         i_partida,
                                                         guardarBoton,
                                                         cargarBoton,
                                                         hO, mO, sO))
    iniciarBoton.place(relx=0.05, rely=0.78, anchor=W)


    borrarJugadaBoton = Button(ventanaJugar, text='Borrar jugada',
                               state=DISABLED,
                               command=lambda:borrarJugadaAnt(pJ,
                                                              refCasillas))
    borrarJugadaBoton.place(relx=0.25, rely=0.78, anchor=W)


    terminarBoton = Button(ventanaJugar, text='Terminar juego',
                           state=DISABLED,
                           command=lambda:terminarJuego(ventanaJugar,
                                                        i_faciles,
                                                        i_interme,
                                                        i_difiles,
                                                        i_partida,
                                                        False))
    terminarBoton.place(relx=0.45, rely=0.78, anchor=W)


    borrarBoton = Button(ventanaJugar, text='Borrar juego',
                         state=DISABLED,
                         command=lambda:terminarJuego(ventanaJugar,
                                                      i_faciles,
                                                      i_interme,
                                                      i_difiles,
                                                      i_partida,
                                                      True))
    borrarBoton.place(relx=0.67, rely=0.78, anchor=W)



    top10Boton = Button(ventanaJugar, text='Top 10',
                        command=lambda:desplegarTop10(ventanaJugar))
    
    top10Boton.place(relx=0.95, rely=0.78, anchor=E)


    guardarBoton = Button(ventanaJugar, text='Guardar Juego',
                          state=DISABLED,
                          command=lambda:guardarPartida(nivel,
                                                        reloj,
                                                        panel,
                                                        h, m, s,
                                                        nombre.get(),
                                                        i_partida,
                                                        pJ,
                                                        refCasillas,
                                                        hO, mO, sO))
    guardarBoton.place(relx=0.45, rely=0.92, anchor=W)


    cargarBoton = Button(ventanaJugar, text='Cargar Juego',
                         command=lambda:cargarPartida(ventanaJugar,
                                                      pJ,
                                                      nombre))
    cargarBoton.place(relx=0.67, rely=0.92, anchor=W)

    
    #config visual de los botones de abajo
    listaBotones = [iniciarBoton, borrarJugadaBoton, terminarBoton,
                    borrarBoton, top10Boton, guardarBoton, cargarBoton]
    for boton in listaBotones:
        boton.config(bg='indian red', font=('Nunito Black', 10), fg='papaya whip',
                     activebackground='papaya whip', activeforeground='indian red')



    regresarBoton = Button(ventanaJugar, text='Regresar',
                           command=lambda:regresarJG(ventanaJugar))
    regresarBoton.place(relx=0.95, rely=0.05, anchor=NE)
    regresarBoton.config(bg='papaya whip', font=('Nunito Black', 10),
                         fg='indian red', width=8, height=1,
                         activebackground='indian red', activeforeground='papaya whip')
    
    #Mantiene el evento abierto
    ventanaJugar.mainloop()
    
#------------------------------------------------------------------------------

def menuPrincipal():
    '''Abre la ventana del manú y despliega todos los widgets dentro
    de ella.'''
    #Ventana del Menú Principal
    ventanaMenu = Tk()
    ventanaMenu.geometry('600x600+350+20')
    ventanaMenu.title('Menú Principal')
    ventanaMenu.resizable(width=False, height=False)
    ventanaMenu.config(bg='white')

    #Título
    labelMenu = Label(ventanaMenu, text='Menú Principal')
    labelMenu.place(relx=0.5, rely=0.15, anchor=CENTER)
    labelMenu.config(bg='white', font=('Cooper Black', 23),
                     fg='indian red')

    #Botones del Menú Principal
    #1) JUGAR
    jugarBoton = Button(ventanaMenu, text='Jugar', command=lambda:
                        jugar(ventanaMenu, i_faciles, i_interme, i_difiles,
                              False, 'sin partida', False))
    #2) CONFIGURACIÓN
    configBoton = Button(ventanaMenu, text='Configuración', command=lambda:
                         configurar(ventanaMenu))
    #3) AYUDA
    ayudaBoton = Button(ventanaMenu,  text='Ayuda', command=ayuda)
    #4) ACERCA DE
    acercaDeBoton = Button(ventanaMenu, text='Acerca de', command=lambda:\
                           acercaDe(ventanaMenu))
    #4) SALIR
    salirBoton = Button(ventanaMenu, text='Salir', command=lambda:
                        salir(ventanaMenu))

    #Despliega los botones en el Menú
    listaBotones = [jugarBoton, configBoton, ayudaBoton, acercaDeBoton,
                    salirBoton]
    pos_y=175
    for boton in listaBotones:
        boton.place(relx=0.5, y=pos_y, anchor=CENTER)
        boton.config(bg='indian red', font=('Nunito Black', 13),
                     fg='papaya whip', width='12', height='1',
                     activebackground='papaya whip', activeforeground='indian red')
        pos_y += 75

    #Mantiene el evento abierto
    ventanaMenu.mainloop()


###############################################################################
#Programa Principal
###############################################################################

#Guarda la configuración por default cada vez que se ejecuta el programa
configArchivo = open("futoshiki2020configuración.dat", "wb")
configDefalt = [1, 1, 1, "", "", ""]
pickle.dump(configDefalt, configArchivo)
configArchivo.close()

#listas para las partidas ya jugadas/usadas en una misma corrida
i_faciles = []
i_interme = []
i_difiles = []

tiempo_corriendo = 0
corriendo = True 
cronoS = ''
h = ''
m = ''
s = ''

cantCasillas = 0 

#Despliega el Menú Principal
menuPrincipal()
