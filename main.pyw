# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from decimal import Decimal
from gui import *
import random
from decimal import Decimal
import math
from datetime import datetime, date, time, timedelta


class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
     QtGui.QWidget.__init__(self, parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     
     self.ui.mdiArea.addSubWindow(self.ui.PRINCIPAL)
     self.ui.mdiArea.addSubWindow(self.ui.UNO)
     self.ui.mdiArea.addSubWindow(self.ui.TRES)
     self.ui.mdiArea.addSubWindow(self.ui.DOS)  
     self.ui.mdiArea.addSubWindow(self.ui.CUATRO)   
     self.ui.mdiArea.addSubWindow(self.ui.CINCO)
     self.ui.mdiArea.addSubWindow(self.ui.SEIS)
     self.ui.mdiArea.addSubWindow(self.ui.SIETE)
     self.ui.mdiArea.addSubWindow(self.ui.OCHO)
     self.ui.mdiArea.addSubWindow(self.ui.NUEVE)
     self.ui.mdiArea.addSubWindow(self.ui.DIEZ)
     self.ui.mdiArea.addSubWindow(self.ui.ONCE) 
     self.ui.mdiArea.addSubWindow(self.ui.DOCE) 
     
     

     #    self.ui.mdiArea.activateNextSubWindow()
     self.ui.mdiArea.activateNextSubWindow()

 
     self.TabbedView()

     self.Zo =0
     self.Zalpha=0

    


 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   

     QtCore.QObject.connect(self.ui.linea_mix, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.linexo_mix, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.linec_mix, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.linem_mix, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.btngenerar_mix, QtCore.SIGNAL('clicked()'),
self.Generarmixto)

 # # # # # # # # #     
 # # # # # # # # #     
 # # # # # # # # #     

     QtCore.QObject.connect(self.ui.linea_mul, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.linexo_mul, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.linem_mul, QtCore.SIGNAL("editingFinished()"),
self.Validar)
     QtCore.QObject.connect(self.ui.btngenerar_mul, QtCore.SIGNAL('clicked()'),
self.Generarmulti)
 # # # # # # # # #   

 # # # # # # # # #     
#ALEATORIOS
 # # # # # # # # #  
     QtCore.QObject.connect(self.ui.btngenerar_alea, QtCore.SIGNAL('clicked()'),
self.Generarrand)

 # # # # # # # # #  
     QtCore.QObject.connect(self.ui.btngen_prom, QtCore.SIGNAL('clicked()'),
self.Generpprome)
     QtCore.QObject.connect(self.ui.tabla_promedio, QtCore.SIGNAL('doubleClicked(QModelIndex)'),
      self.Generpprome2)





 # # # # # # # # #  

 # # # # # # # # #   
 # PROMEDIO
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btncalcular_prom, QtCore.SIGNAL('clicked()'),
      self.calcularesta)
     QtCore.QObject.connect(self.ui.btncalcular_prom, QtCore.SIGNAL('clicked()'),
      self.compararesta)



 # # # # # # # # #   

 # # # # # # # # #   
 # KOLMOGOROV AMIRNOV
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btngen_kolm, QtCore.SIGNAL('clicked()'),
      self.Generkolm)
    
     QtCore.QObject.connect(self.ui.btncalcular_kolm, QtCore.SIGNAL('clicked()'),
      self.compararkolm)   






 # # # # # # # # #   



 # # # # # # # # #   
 # FRECUENCIAS
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btn_generar_frec, QtCore.SIGNAL('clicked()'),
      self.Generfrec)
    
     #QtCore.QObject.connect(self.ui.linen_frec, QtCore.SIGNAL('editingFinished()'),
     # self.compararfrec)   
  
     QtCore.QObject.connect(self.ui.linen_frec, QtCore.SIGNAL('editingFinished()'),
      self.generarrangos) 


     QtCore.QObject.connect(self.ui.lineesta_frec, QtCore.SIGNAL('editingFinished()'),
      self.compararfrec)   



 # # # # # # # # #




 # # # # # # # # #   
 # SERIE
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btn_generar_seri, QtCore.SIGNAL('clicked()'),
      self.Generseri)
    
     #QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     # self.compararseri)   
  
     QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     self.generarrangosseri)   



 # # # # # # # # #






 # # # # # # # # #   
 # EXPONENCIAL
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btngen_expo, QtCore.SIGNAL('clicked()'),
      self.Generexpo)
    
     #QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     # self.compararseri)   
  
     QtCore.QObject.connect(self.ui.btncalcular_expo, QtCore.SIGNAL('clicked()'),
     self.calculosexpo)   



 # # # # # # # # #





 # # # # # # # # #   
 # UNIFORME
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.btngen_unif, QtCore.SIGNAL('clicked()'),
      self.Genereunif)
    
     #QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     # self.compararseri)   
  
     QtCore.QObject.connect(self.ui.btn_calcunif, QtCore.SIGNAL('clicked()'),self.calculosunif)


 # # # # # # # # #








 # # # # # # # # #   
 # POISON
 # # # # # # # # # 
     QtCore.QObject.connect(self.ui.lineval_pois, QtCore.SIGNAL('editingFinished()'),
      self.Generpois)
    
     #QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     # self.compararseri)   
  
     QtCore.QObject.connect(self.ui.linen_epois, QtCore.SIGNAL('editingFinished()'),
     self.calculospois) 



 # # # # # # # # #






 # # # # # # # # #   
 # volados
 # # # # # # # # # 
     #QtCore.QObject.connect(self.ui.lineval_vola, QtCore.SIGNAL('editingFinished()'),
     # self.Genervola)
    
     #QtCore.QObject.connect(self.ui.linen_seri, QtCore.SIGNAL('editingFinished()'),
     # self.compararseri)   
  
     QtCore.QObject.connect(self.ui.btn_calcular_vola, QtCore.SIGNAL('clicked()'),self.Genervola)
    
     QtCore.QObject.connect(self.ui.btn_calcular_vola, QtCore.SIGNAL('clicked()'),self.calcularvola)



 # # # # # # # # #

 # # # # # # # # #   
 # COLAS 
 # # # # # # # # # 

    
     QtCore.QObject.connect(self.ui.btngenerar_colas3p, QtCore.SIGNAL('clicked()'),self.Generarcolas3p)
    
     QtCore.QObject.connect(self.ui.btncalcular_colas3p, QtCore.SIGNAL('clicked()'),self.calcularcolas3p)


     QtCore.QObject.connect(self.ui.btngenerar_colas4p, QtCore.SIGNAL('clicked()'),self.Generarcolas4p)
    
     QtCore.QObject.connect(self.ui.btncalcular_colas4p, QtCore.SIGNAL('clicked()'),self.calcularcolas4p)



     QtCore.QObject.connect(self.ui.btngenerar_colas5p, QtCore.SIGNAL('clicked()'),self.Generarcolas5p)
    
     QtCore.QObject.connect(self.ui.btncalcular_colas5p, QtCore.SIGNAL('clicked()'),self.calcularcolas5p)



     QtCore.QObject.connect(self.ui.btngenerar_colas6p, QtCore.SIGNAL('clicked()'),self.Generarcolas6p)
    
     QtCore.QObject.connect(self.ui.btncalcular_colas6p, QtCore.SIGNAL('clicked()'),self.calcularcolas6p)


 # # # # # # # # #





     QtCore.QObject.connect(self.ui.showNext, QtCore.SIGNAL('clicked()'),self.displayNext)
     QtCore.QObject.connect(self.ui.showPrevious, QtCore.SIGNAL('clicked()'),self.displayPrevious)
     QtCore.QObject.connect(self.ui.tileButton, QtCore.SIGNAL('clicked()' ),self.tileArrange)
     QtCore.QObject.connect(self.ui.TabbedViewButton,    QtCore.SIGNAL('clicked()'),self.TabbedView)
     
     #self.connect(self.ui.actionFirst_Window, QtCore.SIGNAL('triggered()' ),self.displayNext)
     #self.connect(self.ui.actionSecond_Window, QtCore.SIGNAL('triggered()'),self.displayPrevious)

  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
     QtCore.QObject.connect(self.ui.commandLinkButton,QtCore.SIGNAL('clicked()'),self.mostrar1)

     QtCore.QObject.connect(self.ui.commandLinkButton_2,QtCore.SIGNAL('clicked()'),self.mostrar2)

     QtCore.QObject.connect(self.ui.commandLinkButton_3,QtCore.SIGNAL('clicked()'),self.mostrar3)

     QtCore.QObject.connect(self.ui.commandLinkButton_4,QtCore.SIGNAL('clicked()'),self.mostrar4)

     QtCore.QObject.connect(self.ui.commandLinkButton_5,QtCore.SIGNAL('clicked()'),self.mostrar5)

     QtCore.QObject.connect(self.ui.commandLinkButton_6,QtCore.SIGNAL('clicked()'),self.mostrar6)

     QtCore.QObject.connect(self.ui.commandLinkButton_7,QtCore.SIGNAL('clicked()'),self.mostrar7)

     QtCore.QObject.connect(self.ui.commandLinkButton_8,QtCore.SIGNAL('clicked()'),self.mostrar8)

     QtCore.QObject.connect(self.ui.commandLinkButton_9,QtCore.SIGNAL('clicked()'),self.mostrar9)

     QtCore.QObject.connect(self.ui.commandLinkButton_10,QtCore.SIGNAL('clicked()'),self.mostrar10)
     QtCore.QObject.connect(self.ui.commandLinkButton_11,QtCore.SIGNAL('clicked()'),self.mostrar11)
     QtCore.QObject.connect(self.ui.commandLinkButton_12,QtCore.SIGNAL('clicked()'),self.mostrar12)

     QtCore.QObject.connect(self.ui.commandLinkButton_13,QtCore.SIGNAL('clicked()'),self.mostrarprincipal)









  def Validar(self):
     
     if len(self.ui.linea_mix.text()) != 0:
      A=int(self.ui.linea_mix.text())
      if A < 0:
        QMessageBox.about(self, "Error A ","No puede ser menor a 0")
        self.ui.linea_mix.setFocus()
     else:
      A=0


     if len(self.ui.linexo_mix.text()) != 0:
      X=int(self.ui.linexo_mix.text())
      if X  < 0:
        QMessageBox.about(self, "Error Xo ","No puede ser menor a 0")
        self.ui.linexo_mix.setFocus()
     else:
      X=0


     if len(self.ui.linec_mix.text()) != 0:
      C=int(self.ui.linec_mix.text())
      if C < 0:
        QMessageBox.about(self, "Error C ","No puede ser menor a 0")
        self.ui.linec_mix.setFocus()
     else:
      C=0


     if len(self.ui.linem_mix.text()) != 0:
      m=int(self.ui.linem_mix.text())
      if m  > 0 and  m > A and  m > X and  m > C:
        print 'ok'
      else:
        QMessageBox.about(self, "Error m ","No puede ser menor a 0  , A , Xo  o  C")
        self.ui.linem_mix.setFocus()
     else:
      m=0


# # # # multiplicativo
     if len(self.ui.linea_mul.text()) != 0:
      A=int(self.ui.linea_mul.text())
      if A < 0:
        QMessageBox.about(self, "Error A ","No puede ser menor a 0")
        self.ui.linea_mul.setFocus()
     else:
      A=0


     if len(self.ui.linexo_mul.text()) != 0:
      X=int(self.ui.linexo_mul.text())
      if X  < 0:
        QMessageBox.about(self, "Error Xo ","No puede ser menor a 0")
        self.ui.linexo_mul.setFocus()
     else:
      X=0


     if len(self.ui.linem_mul.text()) != 0:
      m=int(self.ui.linem_mul.text())
      if m  > 0 and  m > A and  m > X and  m > C:
        print 'ok'
      else:
        QMessageBox.about(self, "Error m ","No puede ser menor a 0  , A  o Xo")
        self.ui.linem_mul.setFocus()
     else:
      m=0


# # # #

  def Generarmixto(self):

    A=int(self.ui.linea_mix.text())
    X=int(self.ui.linexo_mix.text())
    C=int(self.ui.linec_mix.text())
    m=int(self.ui.linem_mix.text())


    inicial=X
    self.ui.tabla_mix.setRowCount(m)
    for i in range(1, m+1):
      print i
      div=(A*X+C)/m
      resi=(A*X+C)%m
      nog=Decimal(resi)/Decimal(m)

      self.ui.tabla_mix.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_mix.setItem(i-1,1, QtGui.QTableWidgetItem(str(X)))
      self.ui.tabla_mix.setItem(i-1,2, QtGui.QTableWidgetItem(str(div)+" + "+str(resi)+" / "+str(m)))
      self.ui.tabla_mix.setItem(i-1,3, QtGui.QTableWidgetItem(str(resi)))
      self.ui.tabla_mix.setItem(i-1,4, QtGui.QTableWidgetItem(str(nog)))

      X=resi
      final=resi
      if inicial==final:
         break


    if  i == m and inicial==final:
     QMessageBox.about(self, "Mensaje ","::Por lo tanto es un Generador\nCongruencial mixto  Confiable\no\nGenerador con periodo Completo::")
     self.ui.lblresultado_mix.setText("::Por lo tanto es un Generador\nCongruencial mixto  Confiable\no\nGenerador con periodo Completo::")

     
    else :
     QMessageBox.about(self, "Mensaje ","::Por lo tanto No es un Generador\nCongruencial mixto  Confiable\no\nGenerador con periodo Incompleto::")
     self.ui.lblresultado_mix.setText("::Por lo tanto No es un Generador\nCongruencial mixto  Confiable\no\nGenerador con periodo Incompleto::")


# # # # # # # # # # # #

  def Generarmulti(self):

    tipo = QMessageBox.question(self, "Valor de m",
                   "Que tipo de valor contiene  <b>m </b>?\n",
                   "DECIMAL","BINARIO");

    print tipo
    A=int(self.ui.linea_mul.text())
    X=int(self.ui.linexo_mul.text())
    m=int(self.ui.linem_mul.text())

  


    if tipo==1 :
      print "es binario"
      pe=m/4

    elif tipo==0:
      print "es decimal"
      cant=str(m).count('0')

      if(cant<1): 
        print "Error"
        base= input('Introduzca la Base : ')
        expo= input('Introduzca el Exponente : ')
      else:
        expo=cant
        print 'numero de ceros %i' %cant

      if(expo >= 5):
        print "mayor o igual a 5"
        print "Periodo Esperado = 5x10^d-2"
        pe=5*10**(expo-2)
        expo=expo-2
        print "Periodo Esperado = 5x10^%i = %i" %(expo,pe)

      else:
        print "menor a 5"
        print "Periodo Esperado = m.c.m { λ(2^d) ,λ(5^d) } "
        lamd=2**(expo-2)
        lamc=(5**(expo-1))*4
        expo=expo-2
        print "λ(2^%i) = %i" %(expo,lamd)
        print "λ(5^%i) = %i" %(expo,lamc)
        print "Periodo Esperado = %i" %lamc
        pe=lamc




    print "PE",pe   

    inicial=X
    final=X
    self.ui.tabla_mul.setRowCount(m)
    for i in range(1, pe+1):
      print i
      div=(A*X)/m
      resi=(A*X)%m
      nog=Decimal(resi)/Decimal(m)

      self.ui.tabla_mul.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_mul.setItem(i-1,1, QtGui.QTableWidgetItem(str(X)))
      self.ui.tabla_mul.setItem(i-1,2, QtGui.QTableWidgetItem(str(div)+" + "+str(resi)+" / "+str(m)))
      self.ui.tabla_mul.setItem(i-1,3, QtGui.QTableWidgetItem(str(resi)))
      self.ui.tabla_mul.setItem(i-1,4, QtGui.QTableWidgetItem(str(nog)))

      X=resi
      final=resi
      if inicial==final:
         break


    if  i == pe and inicial==final:
     QMessageBox.about(self, "Mensaje ","::Por lo tanto es un Generador\nCongruencial Multiplicativo  Confiable\no\nGenerador con periodo Completo::")
     self.ui.lblresultado_mul.setText("::Por lo tanto es un Generador\nCongruencial Multiplicativo  Confiable\no\nGenerador con periodo Completo::")

     
    else :
     QMessageBox.about(self, "Mensaje ","::Por lo tanto No es un Generador\nCongruencial Multiplicativo  Confiable\no\nGenerador con periodo Incompleto::")
     self.ui.lblresultado_mul.setText("::Por lo tanto No es un Generador\nCongruencial Multiplicativo  Confiable\no\nGenerador con periodo Incompleto::")


# # # # # # # # # # # #
  def Generarrand(self):
    print "genero"
    no=int(self.ui.lineval_rand.text())
    self.ui.tabla_rand.setRowCount(no)
    for i in range(1, no+1):
      self.ui.tabla_rand.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_rand.setItem(i-1,1, QtGui.QTableWidgetItem(str(random.uniform(0,1))))


# # # # # # # # # # # #


  def Generpprome(self):
    print "genero"
    no=int(self.ui.lineval_prom.text())
    self.ui.tabla_promedio.setRowCount(no)
    suma=0
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_promedio.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_promedio.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))
      valor=str(self.ui.tabla_promedio.item(i-1,1).text())
      suma=suma+Decimal(valor)

    prom=suma/no

    self.ui.lblsumprom.setText(str(round(suma,5)))
    self.ui.lblpromprom.setText(str(round(prom,5)))


    print "Estadistico de Tablas"
    raiz=math.sqrt(no)
    val=0.083333333
    print val
    raizdoce=math.sqrt(Decimal(val))
    print raizdoce
    print raiz
    self.Zo=((Decimal(prom)-Decimal(.50))*Decimal(raiz))/Decimal(raizdoce)

    if(self.Zo<0):
      self.Zo=self.Zo*-1
      self.ui.lblpromzo.setText(str(round(self.Zo,5)))
    else:
      self.Zo=self.Zo
      print self.Zo
      self.ui.lblpromzo.setText(str(round(self.Zo,5)))

      return self.Zo
# # # # # # # # # # # #


  def Generpprome2(self):
    print "Alimentados"
    no=int(self.ui.lineval_prom.text())
    suma=0
    for i in range(1, no+1):

      valor=str(self.ui.tabla_promedio.item(i-1,1).text())
      suma=suma+Decimal(valor)

    prom=suma/no

    self.ui.lblsumprom.setText(str(suma))
    self.ui.lblpromprom.setText(str(prom))



# # # # # # # # # # # #

  def calcularesta(self):
    print "Estadistico"
    alpha=Decimal(str(self.ui.linealfa_prom.text()))
    print alpha

    self.Zalpha=(alpha / Decimal(100))/Decimal(2)
    print self.Zalpha

    self.ui.lblesta_prom.setText(str(self.Zalpha))


    return self.Zalpha

   
# # # # # # # # # # # #

  def compararesta(self):
    print "Comparar"
    esta=str(self.ui.lineestasum_pro.text())
    print "estadisticos" ,esta

    Zoo=self.Zo
    print "Zoo",Zoo
    if(Zoo < Decimal(esta)):
      self.ui.lblresultado.setText("::Por lo tantos los Numeros Son aceptados::")

    else:
      self.ui.lblresultado.setText("::Por lo tantos los Numeros <b>No </b>Son aceptados::")





   
# # # # # # # # # # # #

  def compararkolm(self):
    print "compararkolm"

    esta_kolm=str(self.ui.lineesta_kolm.text())
    print "estadistico" ,esta_kolm

    no=int(self.ui.lineval_kolm.text())
    suma=0
    maximo=[]
    for i in range(1, no+1):
      valor=str(self.ui.tabla_kolm.item(i-1,4).text())
      maximo.append(valor)


    maximo.sort(reverse=True)
    valmaximo=maximo[0]

    print "valmaximo " ,valmaximo
    print "Decimal kolm" , Decimal(esta_kolm)

    if(Decimal(valmaximo) < Decimal(esta_kolm)):
      print 'menor'
      self.ui.lblresultado_kolm.setText("::Por lo tantos los Numeros Son aceptados::")
    else:
      print 'mayor'
      self.ui.lblresultado_kolm.setText("::Por lo tantos los Numeros <b>No </b>Son aceptados::")




####################################

  def Generkolm(self):
    print "Prueba de KOLMOGOROV"
    no=int(self.ui.lineval_kolm.text())
    self.ui.tabla_kolm.setRowCount(no)
    suma=0
    li=[]
     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_kolm.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_kolm.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))
      instancia=Decimal(i) / Decimal(no)
      self.ui.tabla_kolm.setItem(i-1,3, QtGui.QTableWidgetItem(str(instancia)))
      
      li.append(rand)


    print li
    li.sort(reverse=True)
    print li  
    i=1
    for valores in li:
      self.ui.tabla_kolm.setItem(i-1,2, QtGui.QTableWidgetItem(str(valores)))
      i=i+1


    for i in range(1, no+1):
      valor=str(self.ui.tabla_kolm.item(i-1,2).text())
      valor2=str(self.ui.tabla_kolm.item(i-1,3).text())
      estprue=Decimal(valor2) - Decimal(valor)
      if(estprue < 0):
        print 'menor'
        estprue=estprue* -1
        self.ui.tabla_kolm.setItem(i-1,4, QtGui.QTableWidgetItem(str(estprue)))
        print estprue
      else:
        print 'mayor'
        self.ui.tabla_kolm.setItem(i-1,4, QtGui.QTableWidgetItem(str(estprue)))
        print estprue




####################################
#####################################




##############FRECUENCIA######################
####################################

  def Generfrec(self):
    print "Prueba de FRECUENCIA"
    no=int(self.ui.lineval_frec.text())
    self.ui.tabla_frec.setRowCount(no)
    suma=0

     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_frec.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_frec.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))
      


  def generarrangos(self):
      print "Acomodar los rangos"
      no=int(self.ui.lineval_frec.text())
      numeros=[]
      for i in range(1, no+1):
       valor=float(self.ui.tabla_frec.item(i-1,1).text())
       numeros.append(valor)


      print "numeros",numeros


      intervalo=int(self.ui.linen_frec.text())
      print "intervalo",intervalo
      fei=Decimal (no)/Decimal (intervalo)
      print "fei",fei
      rangosfei=0
      rangos=[]


      for i in range(0, intervalo+1):
        rangosfei=Decimal (i)/Decimal (intervalo) 
        rangos.append(float(rangosfei))
        print  "rangos-",rangosfei


      try:  

        numeros=[.94653 , .42402 , .07405 ,.53845 ,.94747 ,.57260 ,.99382 ,.47744 ,.48893 ,.16993];
        print "valor test",numeros
        print rangos
        


        nombrerango=[]
        for h in range(0, len(rangos)):
          for i in range(0, len(numeros)):
            print i
            print numeros[i] ,rangos[h]  ,"AND", numeros[i] ,rangos[h+1] 

            if(numeros[i] >= rangos[h]  and numeros[i] <= rangos[h+1] ):
              print "true " ,i , " \t \t \t rango=" ,rangos[h] 

              nombrerango.append(rangos[h])
              print nombrerango
            else:
              print "false " ,i 
          print "Termino \n"
          
      except Exception:
        sumaxo=0.00
        print "error"
        print "array de rangos",nombrerango
        print "fei" ,fei
        for r in range(0, len(rangos)-1):
          n=nombrerango.count(rangos[r])
          print  " entre" ,rangos[r]  ,"y", rangos[r+1] ,"existen", n
          sumaxo=Decimal(sumaxo)+(Decimal(n)-Decimal(fei))**2
          print "suma",sumaxo
          #label= " entre" ,rangos[r]  ,"y", rangos[r+1] ,"existen", nombrerango.count(rangos[r]),"\n","mario"
          #print label
          #self.ui.lblresultado_frec.setPlainText(str(label))
        print "suma",sumaxo
        xo2=sumaxo*Decimal(1/fei)
        print "xo2",xo2
        self.ui.line_frexo2.setText(str(xo2))



      #for r in range(0, len(rangos)):
       # if(nombrerango.index(rangos[r])):
       #   variable+r=(variable+r)
       #   print "variable",r"-",variable.r

       #print "en rango",rangos[r] "y" , rango rangos[r+1] ,"tenemos" 


   
# # # # # # # # # # # #

  def compararfrec(self):
    print "compararfrec"

    esta_frec=str(self.ui.lineesta_frec.text())
    print "frecuencia" ,esta_frec

    acomparar=Decimal(str(self.ui.line_frexo2.text()))
    print "Xo2" ,acomparar
    


    if(Decimal(acomparar) < Decimal(esta_frec)):
      print 'menor'
      self.ui.lblresultado_frec.setText("::Por lo tantos los Numeros Son aceptados::")
    else:
      print 'mayor'
      self.ui.lblresultado_frec.setText("::Por lo tantos los Numeros <b>No </b>Son aceptados::")



####################################
#####################################











############## SERIES ######################
####################################





  def Generseri(self):
    print "Prueba de seriUENCIA"
    no=int(self.ui.lineval_seri.text())
    self.ui.tabla_seri.setRowCount(no)
    suma=0

     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_seri.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_seri.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))
      self.ui.tabla_seri.setItem(i-2,2, QtGui.QTableWidgetItem(str(rand)))







  def generarrangosseri(self):
      print "Acomodar los rangos bidimensionales"
      no=int(self.ui.lineval_seri.text())
      numerosx=[]

      for x in range(1, no):
       valorx=float(self.ui.tabla_seri.item(x-1,1).text())
       numerosx.append(valorx)


      print "numerosx ",numerosx

      numerosy=[]
      for y in range(1, no):
       valory=float(self.ui.tabla_seri.item(y-1,2).text())
       numerosy.append(valory)


      print "numerosy ",numerosy


      intervalo=int(self.ui.linen_seri.text())
      print "intervalo",intervalo
      fei=Decimal (no)/Decimal (intervalo)
      print "fei",fei
      rangosfei=0
      rangosx=[]
      rangosy=[]


      for i in range(0, intervalo+1):
        rangosfeix=Decimal (i)/Decimal (intervalo) 
        rangosfeiy=Decimal (i)/Decimal (intervalo) 

        rangosx.append(float(rangosfeix))
        rangosy.append(float(rangosfeiy))
        print  "rangos-x",rangosfeix
        print  "rangos-y",rangosfeiy




      try:  

        #valortest=[.94653 , .42402 , .07405 ,.53845 ,.94747 ,.57260 ,.99382 ,.47744 ,.48893 ,.16993];
       # print "valor test",valortest

        numerosx =  [0.3612203956, 0.957418448494, 0.638198469778, 0.183884932998]
        numerosy =  [0.957418448494, 0.638198469778, 0.183884932998, 0.0469899650869]
        print "valor test \n",numerosx ,"\n",numerosy,"\n \n"
        print rangosx
        print rangosy
        


        nombrerangox=[]
        nombrerangoy=[]
        nombrerangoz=[]
        for h in range(0, len(rangosx)):
          for i in range(0, len(numerosx)):
            print    numerosx[i] ,rangosx[h]  ,"AND", numerosx[i] ,rangosx[h+1] ,"---",      numerosy[i] ,rangosy[h]  ,"AND", numerosy[i] ,rangosy[h+1] 

            if( (numerosx[i] >= rangosx[h]  and numerosx[i] <= rangosx[h+1]) and  (numerosy[i] >= rangosy[h]  and numerosy[i] <= rangosy[h+1]) ):

              print "true " ,i , " \t \t \t pareja =" ,rangosx[h], "y " , rangosx[h+1] ,"AND" ,rangosy[h], "y " , rangosy[h+1]
           
              nombrerangox.append(rangosx[h])
              print nombrerangox

              nombrerangoy.append(rangosx[h])
              print nombrerangoy

              rangosz=str(rangosx[h])+""+str(rangosy[h])
              print rangosz
              nombrerangoz.append(str(rangosz))

            else:
              print "false " ,i 
          print "Termino \n"
          
      except Exception:
        print "error"
        print "array de rangosx",nombrerangox
        print "array de rangosy",nombrerangoy
        print "array de rangos",nombrerangoz

       # print "fei" ,fei
       # for r in range(0, len(rangos)-1):
       #   n=nombrerangox.count(rangos[r])
        #  print  " entre" ,rangos[r]  ,"y", rangos[r+1] ,"existen", n
        

          #sumaxo=Decimal(sumaxo)+(Decimal(n)-Decimal(fei))**2
          #print "suma",sumaxo
          #label= " entre" ,rangos[r]  ,"y", rangos[r+1] ,"existen", nombrerango.count(rangos[r]),"\n","mario"
          #print label
          #self.ui.lblresultado_frec.setPlainText(str(label))
       # print "suma",sumaxo
        #xo2=sumaxo*Decimal(1/fei)
        #print "xo2",xo2
        #self.ui.line_frexo2.setText(str(xo2))


      #for r in range(0, len(rangos)):
       # if(nombrerango.index(rangos[r])):
       #   variable+r=(variable+r)
       #   print "variable",r"-",variable.r

       #print "en rango",rangos[r] "y" , rango rangos[r+1] ,"tenemos" 


   
# # # # # # # # # # # #

  def compararseri(self):
    print "compararseri"

    esta_seri=str(self.ui.lineesta_seri.text())
    print "estadistico" ,esta_seri

    no=int(self.ui.lineval_seri.text())
    suma=0
    maximo=[]
    for i in range(1, no+1):
      valor=str(self.ui.tabla_seri.item(i-1,4).text())
      maximo.append(valor)


    maximo.sort(reverse=True)
    valmaximo=maximo[0]

    print "valmaximo " ,valmaximo
    print "Decimal seri" , Decimal(esta_seri)

    if(Decimal(valmaximo) < Decimal(esta_seri)):
      print 'menor'
      self.ui.lblresultado_seri.setText("::Por lo tantos los Numeros Son aceptados::")
    else:
      print 'mayor'
      self.ui.lblresultado_seri.setText("::Por lo tantos los Numeros <b>No </b>Son aceptados::")



####################################
#####################################









############## EXPONENCIAL ######################
####################################

  def Generexpo(self):
    print "Distribucion Exponencial "
    no=int(self.ui.lineval_expo.text())
    self.ui.tabla_expo.setRowCount(no)
    suma=0

     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_expo.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_expo.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))





####################################

  def calculosexpo(self):
    print "Calculos Exponencial "
    no=int(self.ui.lineval_expo.text()) #5;Clientes
    vln=int(self.ui.linen_lnexpo.text()) #3;Minutos
    print math.log(0.74910) 
    ttot=0
    tprom=0
    for i in range(1, no+1):
          print i
          valor= str(self.ui.tabla_expo.item(i-1,1).text())
          print "valor ",valor
          R=Decimal(valor)
          print "R ", R
          X=Decimal(-1)/Decimal(vln)

          print "X " ,X
          Y=Decimal(math.log(R)) 
          print "Y " ,Y
          XY=X*Y
          print "Total " ,XY
          self.ui.tabla_expo.setItem(i-1,2, QtGui.QTableWidgetItem(str(round(XY,5))))
          ttot=ttot+XY

    print "total-" ,ttot  
    self.ui.linen_expo_ttot.setText(str(round(ttot,5)))

    tprom =Decimal(ttot)/Decimal(no)
    self.ui.linen_expo_tpro.setText(str(round(tprom,5)))
    print "promedio-" ,tprom



















############## UNIFORME ######################
####################################

  def Genereunif(self):
    print "Distribucion uniform "
    no=int(self.ui.lineval_unif.text())
    self.ui.tabla_unif.setRowCount(no)
    suma=0

     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_unif.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))





####################################

  def calculosunif(self):
    print "Calculos uniforme "
    no=int(self.ui.lineval_unif.text()) #5;Clientes

    va=int(self.ui.linen_aunif.text()) #2;Minutos
    vb=int(self.ui.linen_bunif.text()) #4;Minutos

    print va,"--",vb

    ttot=0
    tprom=0
    for i in range(1, no+1):
          print i
          valor= str(self.ui.tabla_unif.item(i-1,1).text())
          R=Decimal(valor)

          X=va+((vb - va)*(R))

          print X
          XY=X
          print "Total " ,XY
          self.ui.tabla_unif.setItem(i-1,2, QtGui.QTableWidgetItem(str(round(XY,5))))
          ttot=ttot+XY

    print "total-" ,ttot  
    self.ui.linen_unif_ttot.setText(str(round(ttot,5)))

    tprom =Decimal(ttot)/Decimal(no)
    self.ui.linen_unif_tpro.setText(str(round(tprom,5)))
    print "promedio-" ,tprom













############## POISON ######################
####################################

  def Generpois(self):
    print "Distribucion POISON "
    print math.exp(1)
    print math.factorial(5)

    vln=int(self.ui.linen_epois.text()) # 5 dias
    print "YESY" ,(math.exp(-5)*(5**1) )/ (math.factorial(1)) ,"\n \n ________________________"


    no=int(self.ui.lineval_pois.text())


    self.ui.tabla_pois.setRowCount(no)
    suma=0
    fx=0
    self.ui.tabla_pois.setRowCount(1000)


    fx=0  
    i=0
    while fx <=0.99995:
      

      self.ui.tabla_pois.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))

      FX=(math.exp(-vln)*(vln**i) )/ (math.factorial(i))
      fx=fx+FX
      self.ui.tabla_pois.setItem(i-1,1, QtGui.QTableWidgetItem(str(FX)))
      self.ui.tabla_pois.setItem(i-1,2, QtGui.QTableWidgetItem(str(fx)))

      print i,"______",(FX) ,"-----",(fx)

      i=i+1






     #li.sort(reverse=True)
   # for i in range(0, no+1):

    #  self.ui.tabla_pois.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))

    #  FX=(math.exp(-vln)*(vln**i) )/ (math.factorial(i))
     # fx=fx+FX

    #  print i,"______",round(FX,5) ,"-----",round(fx,5)
    #  if( fx >=0.99995 ):
     #   print "break"
     #   break

    #print "termino"


      #self.ui.tabla_pois.setItem(i-1,1, QtGui.QTableWidgetItem(str(rand)))





####################################

  def calculospois(self):
    print "Calculos POISON "
    no=int(self.ui.lineval_pois.text()) #5;Clientes
    vln=int(self.ui.linen_epois.text()) #3;Minutos
    print math.log(0.74910) 
    ttot=0
    tprom=0
    for i in range(1, no+1):
          print i
          valor= str(self.ui.tabla_pois.item(i-1,1).text())
          print "valor ",valor
          R=Decimal(valor)
          print "R ", R
          X=Decimal(-1)/Decimal(vln)

          print "X " ,X
          Y=Decimal(math.log(R)) 
          print "Y " ,Y
          XY=X*Y
          print "Total " ,XY
          self.ui.tabla_pois.setItem(i-1,2, QtGui.QTableWidgetItem(str(round(XY,5))))
          ttot=ttot+XY

    print "total-" ,ttot  
    self.ui.linen_pois_ttot.setText(str(round(ttot,5)))

    tprom =Decimal(ttot)/Decimal(no)
    self.ui.linen_pois_tpro.setText(str(round(tprom,5)))
    print "promedio-" ,tprom












############## VOLADOS ######################
####################################


  def Genervola(self):
    print "VOLADOS"
    no=int(self.ui.lineval_vola.text())
    print no
    self.ui.tabla_vola.setRowCount(no)

     #li.sort(reverse=True)
    for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      #self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_vola.setItem(i-1,3, QtGui.QTableWidgetItem(str(rand)))





  def calcularvola(self):
    print "calcularvola"

    no=int(self.ui.lineval_vola.text())

    cantidad= int(self.ui.linen_vola_ini.text()) #default
    cantidad_default=cantidad

    apuesta=int(self.ui.linen_vola_apu.text()) #default
    apuesta_default=apuesta

    valormeta=   int(self.ui.linen_vola_meta.text())

    partida=1
    gano=""
    meta=""
    final=""
    cantidaddes=0

    print no,cantidad,apuesta,valormeta,partida


    resultados=[]
    iteracion=0

    for i in range(1, no+1):

      valor= str(self.ui.tabla_vola.item(i-1,3).text())
      self.ui.tabla_vola.setItem(i-1,0, QtGui.QTableWidgetItem(str(partida)))
      self.ui.tabla_vola.setItem(i-1,1, QtGui.QTableWidgetItem(str(cantidad)))
      self.ui.tabla_vola.setItem(i-1,2, QtGui.QTableWidgetItem(str(apuesta)))
      


      if(Decimal(valor) <= 0.5):
        print Decimal(valor) ,"gana"
        gano="si"
        cantidaddes=cantidad+apuesta
        apuesta=apuesta_default

      else:
        print Decimal(valor),"pierde"
        gano="no"
        cantidaddes=cantidad-apuesta
        apuesta=2*apuesta



      self.ui.tabla_vola.setItem(i-1,4, QtGui.QTableWidgetItem(str(gano)))

      self.ui.tabla_vola.setItem(i-1,5, QtGui.QTableWidgetItem(str(cantidaddes)))


      if(cantidaddes>=valormeta):
        print "llego a meta"
        meta="Meta"
        
        print "nueva partidad"
        print "i" ,i
        print "no" ,no+1
        if(i!=no):
          partida=partida+1
          cantidad=cantidad_default
          apuesta=apuesta_default

      elif(cantidaddes<apuesta):
        print cantidad,cantidaddes ,"menor  o igual a la apuesta"
        meta="Quiebra"
       
        print "nueva partidad"
        print "i" ,i
        print "no" ,no+1

        if(i!=no):
          partida=partida+1
          cantidad=cantidad_default
          apuesta=apuesta_default

      else:
        print "NO llego a meta"
        meta="No"
        cantidad=cantidaddes



      resultados.append(meta)  
      self.ui.tabla_vola.setItem(i-1,6, QtGui.QTableWidgetItem(str(meta)))


      print "---RESET-"


    print "resultados" ,resultados  

    print "meta" ,resultados.count('Meta')
    self.ui.lbl_meta.setText("Veces que se llego a la Meta: "+str(resultados.count('Meta')))

    print "quiebre" ,resultados.count('Quiebra')
    self.ui.lbl_quiebra.setText("Veces en Quiebra: " +str(resultados.count('Quiebra')))

    print "partidas" ,partida
    self.ui.lbl_corridas.setText("Corridas Realizadas: "+str(partida))


    print "Probabilidad" ,partida
    prob=Decimal(resultados.count('Meta'))/Decimal(partida)
    probr=prob*Decimal(100)

    self.ui.lbl_prob.setText("Probabilidad llegar a la meta : "+str(round(probr,2))+"%")





############## VOLADOS ######################
####################################


  def Generarcolas3p(self):
    self.ui.tabla_colas_3.clearContents();
    no=15

    self.ui.tabla_colas_3.setRowCount(no)

    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 
    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 

    for i in range(0, len(numeros1)-2):
      print "i___",i
      self.ui.tabla_colas_3.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
      self.ui.tabla_colas_3.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))



  def calcularcolas3p(self):
    print "calcular 3p" 

    formato = "%I:%M:%S"

    


    print "Colas"
    #no=int(self.ui.lineval_colas.text())
    no=15
    self.ui.tabla_colas_3.setRowCount(no)

     #li.sort(reverse=True)
    """for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      rand2=str(random.uniform(0,1))
      #self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_colas_3.setItem(i-1,0, QtGui.QTableWidgetItem(str(rand)))
      self.ui.tabla_colas_3.setItem(i-1,4, QtGui.QTableWidgetItem(str(rand2)))

    """
    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 

    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
    
    llegada =  [0,40 ,60 ,25 ,35 ,30 ,30 ,30 ,45 ,50 ,40 ,45 ,45 ,60 ,50 ] 

    horas_inicio =  ["11:00:00","11:50:00","12:40:00","1:15:00","2:00:00","2:25:00","3:45:00","4:15:00","4:50:00","5:35:00","6:05:00","6:45:00", "7:15:00", "12:00:00 " ] 

    servicio =  [50,25 ,35 ,45 ,25 ,50 ,30 ,35 ,45 ,30 ,40 ,30 ,25 ,0 ,0 ]

    cola =  [1,1 ,0 ,1 ,1 ,1 ,1 ,2 ,2 ,2 ,2 ,1 ,1]
    
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 
    


    for i in range(0, len(numeros1)-2):
      print "i___",i
      print "numeros___",numeros1[i] ,"____", numeros2[i]
      self.ui.tabla_colas_3.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
      self.ui.tabla_colas_3.setItem(i,1, QtGui.QTableWidgetItem(str(llegada[i])))


      self.ui.tabla_colas_3.setItem(i,3, QtGui.QTableWidgetItem(str(horas_inicio[i])))
      self.ui.tabla_colas_3.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))
      self.ui.tabla_colas_3.setItem(i,5, QtGui.QTableWidgetItem(str(servicio[i])))


      hora = datetime.strptime(horainicio, formato)
      self.ui.tabla_colas_3.setItem(i,2, QtGui.QTableWidgetItem(str(hora.strftime(formato))))#se pasa directo el reformato
      if(i==2):
        self.ui.tabla_colas_3.setItem(i,7, QtGui.QTableWidgetItem(str("25")))#se pasa directo el reformato
      else:
        self.ui.tabla_colas_3.setItem(i,7, QtGui.QTableWidgetItem(str("0")))#se pasa directo el reformato


      self.ui.tabla_colas_3.setItem(i,9, QtGui.QTableWidgetItem(str(cola[i])))






      print "llegada___",int(llegada[i])
      tiempoentre=int(llegada[i]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
      valtiempoe=tiempoentre*60 #lo convertimos en minutos
      mastiempoe= hora + timedelta(seconds=int(valtiempoe)) #lo sumamomos
      print "ya sumado",str(mastiempoe.strftime(formato))


      print "llegada-adelanrado___",int(llegada[i])
      if(i!=len(numeros1)-1):
        tiempoentre2=int(llegada[i+1]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
        valtiempoe2=tiempoentre2*60 #lo convertimos en minutos
        mastiempoe2= hora + timedelta(seconds=int(valtiempoe2)) #lo sumamomos
        print str(mastiempoe2.strftime(formato))

        horainicio=str(mastiempoe2.strftime(formato))
        print "nueva hora de INICIO",hora





      gethoratempo=str(self.ui.tabla_colas_3.item(i,3).text())   
      horatempo=datetime.strptime(gethoratempo, formato)


      print "valor toiempo servicio",int(str(self.ui.tabla_colas_3.item(i,5).text()))
      tiemposervicio=int(str(self.ui.tabla_colas_3.item(i,5).text())) #obtenemos el  valor de la tabla (tiemposervicio entre tiemposervicio)
      valtiempos=tiemposervicio*60 #lo convertimos en minutos


      mastiempos= horatempo + timedelta(seconds=int(valtiempos)) #lo sumamomos
      print "ya sumado",str(mastiempos.strftime(formato))

      self.ui.tabla_colas_3.setItem(i,6, QtGui.QTableWidgetItem(str(mastiempos.strftime(formato)))) # se pasa directo ya sumado


    
      ## 
      ## Tiempo de espera del Camion
      ##

      print "hora llegada" ,self.ui.tabla_colas_3.item(i,2).text()
      print "hora servicio" ,self.ui.tabla_colas_3.item(i,3).text()

      horaobtenida=str(self.ui.tabla_colas_3.item(i,2).text())
      horaobtenida2=str(self.ui.tabla_colas_3.item(i,3).text())

      horainicio_llegada =  datetime.strptime(horaobtenida, formato)
      horainicio_servicio = datetime.strptime(horaobtenida2, formato)
      print llegada
      print horainicio_servicio



      tiempo_espera=horainicio_servicio - horainicio_llegada
      print "tiempo de espera" ,tiempo_espera
      self.ui.tabla_colas_3.setItem(i,8, QtGui.QTableWidgetItem(str(tiempo_espera))) # se pasa directo ya sumado


    
      ##


    print "\n FIN \n"  
 



    trabajado=510 #8:30 to minutos
    valor_normal= Decimal(str(self.ui.line_salario_normal.text())) 
    print valor_normal
    valorxminuto=valor_normal/Decimal(60)
    print valorxminuto

    totalnormal=valorxminuto * Decimal(trabajado)
    print totalnormal
    numeropersonas=3
    total_totalnormal=numeropersonas*totalnormal
    print total_totalnormal
    self.ui.line_normal_3.setText(str(round(total_totalnormal,3)))


    extra=10
    valor_extra= Decimal(str(self.ui.line_salario_extra.text()))
    print valor_extra
    valorxminuto_extra=valor_extra/Decimal(60)
    print valorxminuto_extra

    totalextra=valorxminuto_extra * Decimal(extra)
    print totalextra

    total_totalextra=numeropersonas*totalextra
    print total_totalextra
    self.ui.line_extra_3.setText(str(round(total_totalextra,3)))


    total_salarios=total_totalextra + total_totalnormal
    print total_salarios
    self.ui.line_totals_3.setText(str(round(total_salarios,3)))



    print "OCIO"
    sumatoriaocio=Decimal(385)
    valor_ocio= Decimal(str(self.ui.line_val_camion.text()))
     #obtenemos hora de ocio
    print valor_ocio
    valorxminuto_ocio=valor_ocio/Decimal(60)
    print valorxminuto_ocio
    totalocio=valorxminuto_ocio * Decimal(sumatoriaocio)
    print "total ocio",totalocio
    self.ui.line_camion_3.setText(str(round(totalocio,3)))



    print "Almacem"

    sumatoriaalmacen=Decimal(520)
    valor_almacen= Decimal(str(self.ui.line_val_almacen.text())) 
    print valor_almacen
    valorxminuto=valor_almacen/Decimal(60)
    print valorxminuto

    totalalmacen=valorxminuto * Decimal(sumatoriaalmacen)
    print "total almacen",totalalmacen
    self.ui.line_operacion_3.setText(str(round(totalalmacen,3)))

    

    total_total=total_salarios+ totalocio+ totalalmacen
    print "TOTAL" ,total_total
    self.ui.line_total_3.setText(str(round(total_total,3)))










  def Generarcolas4p(self):
    self.ui.tabla_colas_4.clearContents();
    no=15

    self.ui.tabla_colas_4.setRowCount(no)

    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 
    
    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 

    for i in range(0, len(numeros1)-2):
      print "i___",i
      self.ui.tabla_colas_4.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
      self.ui.tabla_colas_4.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))



  def calcularcolas4p(self):
    print "calcular 3p" 

    formato = "%I:%M:%S"

    


    print "Colas"
    #no=int(self.ui.lineval_colas.text())
    no=15
    self.ui.tabla_colas_4.setRowCount(no)

     #li.sort(reverse=True)
    """for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      rand2=str(random.uniform(0,1))
      #self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_colas_4.setItem(i-1,0, QtGui.QTableWidgetItem(str(rand)))
      self.ui.tabla_colas_4.setItem(i-1,4, QtGui.QTableWidgetItem(str(rand2)))

    """
    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 

    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
    
    llegada =  [0,40 ,60 ,25 ,35 ,30 ,30 ,30 ,45 ,50 ,40 ,45 ,45 ,60 ,50 ] 

    horas_inicio =  ["11:00:00","11:40:00","12:40:00","1:10:00","1:45:00","2:10:00","2:50:00","3:45:00","4:15:00","4:55:00","5:25:00","6:10:00", "6:55:00","" ] 

    servicio =  [40,20 ,30,35 ,20 ,40 ,25 ,30 ,40 ,25 ,35 ,20 ,20 ,50 ,44 ]

    cola =  [1,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0]

    ocio =  [0,0 ,40 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,5 ,10 ,25,0]
    
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 

    try:
      

      for i in range(0, len(numeros1)):
        print "i___",i
        print "numeros___",numeros1[i] ,"____", numeros2[i]
        self.ui.tabla_colas_4.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
        self.ui.tabla_colas_4.setItem(i,1, QtGui.QTableWidgetItem(str(llegada[i])))


        self.ui.tabla_colas_4.setItem(i,3, QtGui.QTableWidgetItem(str(horas_inicio[i])))
        self.ui.tabla_colas_4.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))
        self.ui.tabla_colas_4.setItem(i,5, QtGui.QTableWidgetItem(str(servicio[i])))    

        self.ui.tabla_colas_4.setItem(i,7, QtGui.QTableWidgetItem(str(ocio[i])))


        hora = datetime.strptime(horainicio, formato)
        self.ui.tabla_colas_4.setItem(i,2, QtGui.QTableWidgetItem(str(hora.strftime(formato))))#se pasa directo el reformato       directo el reformato


        self.ui.tabla_colas_4.setItem(i,9, QtGui.QTableWidgetItem(str(cola[i])))






        print "llegada___",int(llegada[i])
        tiempoentre=int(llegada[i]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
        valtiempoe=tiempoentre*60 #lo convertimos en minutos
        mastiempoe= hora + timedelta(seconds=int(valtiempoe)) #lo sumamomos
        print "ya sumado",str(mastiempoe.strftime(formato))


        print "llegada-adelanrado___",int(llegada[i])
        if(i!=len(numeros1)-1):
          tiempoentre2=int(llegada[i+1]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
          valtiempoe2=tiempoentre2*60 #lo convertimos en minutos
          mastiempoe2= hora + timedelta(seconds=int(valtiempoe2)) #lo sumamomos
          print str(mastiempoe2.strftime(formato))

          horainicio=str(mastiempoe2.strftime(formato))
          print "nueva hora de INICIO",hora





        gethoratempo=str(self.ui.tabla_colas_4.item(i,3).text())   
        horatempo=datetime.strptime(gethoratempo, formato)


        print "valor toiempo servicio",int(str(self.ui.tabla_colas_4.item(i,5).text()))
        tiemposervicio=int(str(self.ui.tabla_colas_4.item(i,5).text())) #obtenemos el  valor de la tabla (tiemposervicio entre tiemposervicio)
        valtiempos=tiemposervicio*60 #lo convertimos en minutos


        mastiempos= horatempo + timedelta(seconds=int(valtiempos)) #lo sumamomos
        print "ya sumado",str(mastiempos.strftime(formato))

        self.ui.tabla_colas_4.setItem(i,6, QtGui.QTableWidgetItem(str(mastiempos.strftime(formato)))) # se pasa directo ya sumado


      
        ## 
        ## Tiempo de espera del Camion
        ##

        print "hora llegada" ,self.ui.tabla_colas_4.item(i,2).text()
        print "hora servicio" ,self.ui.tabla_colas_4.item(i,3).text()

        horaobtenida=str(self.ui.tabla_colas_4.item(i,2).text())
        horaobtenida2=str(self.ui.tabla_colas_4.item(i,3).text())

        horainicio_llegada =  datetime.strptime(horaobtenida, formato)
        horainicio_servicio = datetime.strptime(horaobtenida2, formato)
        print llegada
        print horainicio_servicio



        tiempo_espera=horainicio_servicio - horainicio_llegada
        print "tiempo de espera" ,tiempo_espera
        self.ui.tabla_colas_4.setItem(i,8, QtGui.QTableWidgetItem(str(tiempo_espera))) # se pasa directo ya sumado


        ##

      
        ##



    except Exception, e:
      print e





    print "\n FIN \n"  
 



    trabajado=510 #8:30 to minutos
    valor_normal= Decimal(str(self.ui.line_salario_normal.text())) 
    print valor_normal
    valorxminuto=valor_normal/Decimal(60)
    print valorxminuto

    totalnormal=valorxminuto * Decimal(trabajado)
    print totalnormal
    numeropersonas=4
    total_totalnormal=numeropersonas*totalnormal
    print total_totalnormal
    self.ui.line_normal_9.setText(str(round(total_totalnormal,3)))


    extra=0
    valor_extra= Decimal(str(self.ui.line_salario_extra.text()))
    print valor_extra
    valorxminuto_extra=valor_extra/Decimal(60)
    print valorxminuto_extra

    totalextra=valorxminuto_extra * Decimal(extra)
    print totalextra

    total_totalextra=numeropersonas*totalextra
    print total_totalextra
    self.ui.line_extra_9.setText(str(round(total_totalextra,3)))


    total_salarios=total_totalextra + total_totalnormal
    print total_salarios
    self.ui.line_totals_9.setText(str(round(total_salarios,3)))



    print "OCIO"
    sumatoriaocio=Decimal(85)
    valor_ocio= Decimal(str(self.ui.line_val_camion.text()))
     #obtenemos hora de ocio
    print valor_ocio
    valorxminuto_ocio=valor_ocio/Decimal(60)
    print valorxminuto_ocio
    totalocio=valorxminuto_ocio * Decimal(sumatoriaocio)
    print "total ocio",totalocio
    self.ui.line_camion_9.setText(str(round(totalocio,3)))



    print "Almacem"

    sumatoriaalmacen=Decimal(495)
    valor_almacen= Decimal(str(self.ui.line_val_almacen.text())) 
    print valor_almacen
    valorxminuto=valor_almacen/Decimal(60)
    print valorxminuto

    totalalmacen=valorxminuto * Decimal(sumatoriaalmacen)
    print "total almacen",totalalmacen
    self.ui.line_operacion_9.setText(str(round(totalalmacen,3)))

    

    total_total=total_salarios+ totalocio+ totalalmacen
    print "TOTAL" ,total_total
    self.ui.line_total_9.setText(str(round(total_total,3)))
















  def Generarcolas5p(self):
    self.ui.tabla_colas_5.clearContents();
    no=15

    self.ui.tabla_colas_5.setRowCount(no)

    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 
    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 

    for i in range(0, len(numeros1)-2):
      print "i___",i
      self.ui.tabla_colas_5.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
      self.ui.tabla_colas_5.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))



  def calcularcolas5p(self):
    print "calcular 3p" 

    formato = "%I:%M:%S"

    

    print "Colas"
    #no=int(self.ui.lineval_colas.text())
    no=15
    self.ui.tabla_colas_5.setRowCount(no)

     #li.sort(reverse=True)
    """for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      rand2=str(random.uniform(0,1))
      #self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_colas_5.setItem(i-1,0, QtGui.QTableWidgetItem(str(rand)))
      self.ui.tabla_colas_5.setItem(i-1,4, QtGui.QTableWidgetItem(str(rand2)))

    """
    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 

    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
    
    llegada =  [0,40 ,60 ,25 ,35 ,30 ,30 ,30 ,45 ,50 ,40 ,45 ,45 ,60 ,50 ] 

    horas_inicio =  ["11:00:00","11:40:00","12:40:00","1:05:00","1:40:00","2:10:00","2:45:00","3:35:00","4:00:00","4:45:00","5:25:00","6:10:00", "6:55:00", "12:00:00 " ] 

    servicio =  [35,15 ,25 ,30 ,10 ,35 ,20 ,25 ,30 ,20 ,25 ,15 ,15 ,40 ,40 ]

    cola =  [1,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0]
    
   
    ocio =  [0,5 ,45 ,0 ,5 ,20 ,0 ,0 ,0 ,15 ,20 ,20 ,30,0]

    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 


    try:



      for i in range(0, len(numeros1)-2):
        print "i___",i
        print "numeros___",numeros1[i] ,"____", numeros2[i]
        self.ui.tabla_colas_5.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
        self.ui.tabla_colas_5.setItem(i,1, QtGui.QTableWidgetItem(str(llegada[i])))


        self.ui.tabla_colas_5.setItem(i,3, QtGui.QTableWidgetItem(str(horas_inicio[i])))
        self.ui.tabla_colas_5.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))
        self.ui.tabla_colas_5.setItem(i,5, QtGui.QTableWidgetItem(str(servicio[i])))

        self.ui.tabla_colas_5.setItem(i,7, QtGui.QTableWidgetItem(str(ocio[i])))


        hora = datetime.strptime(horainicio, formato)
        self.ui.tabla_colas_5.setItem(i,2, QtGui.QTableWidgetItem(str(hora.strftime(formato))))#se pasa directo el reformato
        

        self.ui.tabla_colas_5.setItem(i,9, QtGui.QTableWidgetItem(str(cola[i])))






        print "llegada___",int(llegada[i])
        tiempoentre=int(llegada[i]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
        valtiempoe=tiempoentre*60 #lo convertimos en minutos
        mastiempoe= hora + timedelta(seconds=int(valtiempoe)) #lo sumamomos
        print "ya sumado",str(mastiempoe.strftime(formato))


        print "llegada-adelanrado___",int(llegada[i])
        if(i!=len(numeros1)-1):
          tiempoentre2=int(llegada[i+1]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
          valtiempoe2=tiempoentre2*60 #lo convertimos en minutos
          mastiempoe2= hora + timedelta(seconds=int(valtiempoe2)) #lo sumamomos
          print str(mastiempoe2.strftime(formato))

          horainicio=str(mastiempoe2.strftime(formato))
          print "nueva hora de INICIO",hora





        gethoratempo=str(self.ui.tabla_colas_5.item(i,3).text())   
        horatempo=datetime.strptime(gethoratempo, formato)


        print "valor toiempo servicio",int(str(self.ui.tabla_colas_5.item(i,5).text()))
        tiemposervicio=int(str(self.ui.tabla_colas_5.item(i,5).text())) #obtenemos el  valor de la tabla (tiemposervicio entre tiemposervicio)
        valtiempos=tiemposervicio*60 #lo convertimos en minutos


        mastiempos= horatempo + timedelta(seconds=int(valtiempos)) #lo sumamomos
        print "ya sumado",str(mastiempos.strftime(formato))

        self.ui.tabla_colas_5.setItem(i,6, QtGui.QTableWidgetItem(str(mastiempos.strftime(formato)))) # se pasa directo ya sumado


      
        ## 
        ## Tiempo de espera del Camion
        ##

        print "hora llegada" ,self.ui.tabla_colas_5.item(i,2).text()
        print "hora servicio" ,self.ui.tabla_colas_5.item(i,3).text()

        horaobtenida=str(self.ui.tabla_colas_5.item(i,2).text())
        horaobtenida2=str(self.ui.tabla_colas_5.item(i,3).text())

        horainicio_llegada =  datetime.strptime(horaobtenida, formato)
        horainicio_servicio = datetime.strptime(horaobtenida2, formato)
        print llegada
        print horainicio_servicio



        tiempo_espera=horainicio_servicio - horainicio_llegada
        print "tiempo de espera" ,tiempo_espera
        self.ui.tabla_colas_5.setItem(i,8, QtGui.QTableWidgetItem(str(tiempo_espera))) # se pasa directo ya sumado


        ##


    except Exception, e:
      print e
     




    print "\n FIN \n"  
 



    trabajado=510 #8:30 to minutos
    valor_normal= Decimal(str(self.ui.line_salario_normal.text())) 
    print valor_normal
    valorxminuto=valor_normal/Decimal(60)
    print valorxminuto

    totalnormal=valorxminuto * Decimal(trabajado)
    print totalnormal
    numeropersonas=5
    total_totalnormal=numeropersonas*totalnormal
    print total_totalnormal
    self.ui.line_normal_10.setText(str(round(total_totalnormal,3)))


    extra=0
    valor_extra= Decimal(str(self.ui.line_salario_extra.text()))
    print valor_extra
    valorxminuto_extra=valor_extra/Decimal(60)
    print valorxminuto_extra

    totalextra=valorxminuto_extra * Decimal(extra)
    print totalextra

    total_totalextra=numeropersonas*totalextra
    print total_totalextra
    self.ui.line_extra_10.setText(str(round(total_totalextra,3)))


    total_salarios=total_totalextra + total_totalnormal
    print total_salarios
    self.ui.line_totals_10.setText(str(round(total_salarios,3)))



    print "OCIO"
    sumatoriaocio=Decimal(35)
    valor_ocio= Decimal(str(self.ui.line_val_camion.text()))
     #obtenemos hora de ocio
    print valor_ocio
    valorxminuto_ocio=valor_ocio/Decimal(60)
    print valorxminuto_ocio
    totalocio=valorxminuto_ocio * Decimal(sumatoriaocio)
    print "total ocio",totalocio
    self.ui.line_camion_10.setText(str(round(totalocio,3)))



    print "Almacem"

    sumatoriaalmacen=Decimal(490)
    valor_almacen= Decimal(str(self.ui.line_val_almacen.text())) 
    print valor_almacen
    valorxminuto=valor_almacen/Decimal(60)
    print valorxminuto

    totalalmacen=valorxminuto * Decimal(sumatoriaalmacen)
    print "total almacen",totalalmacen
    self.ui.line_operacion_10.setText(str(round(totalalmacen,3)))

    

    total_total=total_salarios+ totalocio+ totalalmacen
    print "TOTAL" ,total_total
    self.ui.line_total_10.setText(str(round(total_total,3)))


















  def Generarcolas6p(self):
    self.ui.tabla_colas_6.clearContents();
    no=15

    self.ui.tabla_colas_6.setRowCount(no)

    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 
    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 

    for i in range(0, len(numeros1)-2):
      print "i___",i
      self.ui.tabla_colas_6.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
      self.ui.tabla_colas_6.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))



  def calcularcolas6p(self):
    print "calcular 3p" 

    formato = "%I:%M:%S"

    


    print "Colas"
    #no=int(self.ui.lineval_colas.text())
    no=15
    self.ui.tabla_colas_6.setRowCount(no)

     #li.sort(reverse=True)
    """for i in range(1, no+1):
      rand=str(random.uniform(0,1))
      rand2=str(random.uniform(0,1))
      #self.ui.tabla_unif.setItem(i-1,0, QtGui.QTableWidgetItem(str(i)))
      self.ui.tabla_colas_6.setItem(i-1,0, QtGui.QTableWidgetItem(str(rand)))
      self.ui.tabla_colas_6.setItem(i-1,4, QtGui.QTableWidgetItem(str(rand2)))

    """
    numeros1 =  [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.67940, 0.90872, 0.58997, 0.68691, 0.73488, 0.98564, 0.89745] 

    numeros2 =  [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.97623, 0.87953]
    
    llegada =  [0,40 ,60 ,25 ,35 ,30 ,30 ,30 ,45 ,50 ,40 ,45 ,45 ,60 ,50 ] 

    horas_inicio =  ["11:00:00","11:40:00","12:40:00","1:05:00","1:40:00","2:10:00","2:40:00","3:30:00","3:55:00","4:45:00","5:25:00","6:10:00", "6:55:00", "12:00:00 " ] 

    servicio =  [30,10 ,15 ,25 ,5 ,30 ,15 ,20 ,25 ,15 ,20 ,10 ,5 ,40 ,30 ]

    cola =  [1,0 ,0 ,0 ,0 ,0 ,0,1 ,0 ,0 ,0 ,0 ,0]
    
    ocio =  [0,10 ,50 ,10 ,10 ,25 ,0 ,5 ,5 ,25 ,25 ,25 ,35,0]

   
    horainicio=str(self.ui.line_horainicio.text()) #obtenemos hora de INICIO
    print horainicio 


    try:
      

      for i in range(0, len(numeros1)-1):
        print "i___",i
        print "numeros___",numeros1[i] ,"____", numeros2[i]
        self.ui.tabla_colas_6.setItem(i,0, QtGui.QTableWidgetItem(str(numeros1[i])))
        self.ui.tabla_colas_6.setItem(i,1, QtGui.QTableWidgetItem(str(llegada[i])))


        self.ui.tabla_colas_6.setItem(i,3, QtGui.QTableWidgetItem(str(horas_inicio[i])))
        self.ui.tabla_colas_6.setItem(i,4, QtGui.QTableWidgetItem(str(numeros2[i])))
        self.ui.tabla_colas_6.setItem(i,5, QtGui.QTableWidgetItem(str(servicio[i])))


        self.ui.tabla_colas_6.setItem(i,7, QtGui.QTableWidgetItem(str(ocio[i])))


        hora = datetime.strptime(horainicio, formato)
        self.ui.tabla_colas_6.setItem(i,2, QtGui.QTableWidgetItem(str(hora.strftime(formato))))#se pasa directo el reformato
   

        self.ui.tabla_colas_6.setItem(i,9, QtGui.QTableWidgetItem(str(cola[i])))






        print "llegada___",int(llegada[i])
        tiempoentre=int(llegada[i]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
        valtiempoe=tiempoentre*60 #lo convertimos en minutos
        mastiempoe= hora + timedelta(seconds=int(valtiempoe)) #lo sumamomos
        print "ya sumado",str(mastiempoe.strftime(formato))


        print "llegada-adelanrado___",int(llegada[i])
        if(i!=len(numeros1)-1):
          tiempoentre2=int(llegada[i+1]) #obtenemos el  valor de la tabla (tiempo entre llegadas)
          valtiempoe2=tiempoentre2*60 #lo convertimos en minutos
          mastiempoe2= hora + timedelta(seconds=int(valtiempoe2)) #lo sumamomos
          print str(mastiempoe2.strftime(formato))

          horainicio=str(mastiempoe2.strftime(formato))
          print "nueva hora de INICIO",hora





        gethoratempo=str(self.ui.tabla_colas_6.item(i,3).text())   
        horatempo=datetime.strptime(gethoratempo, formato)


        print "valor toiempo servicio",int(str(self.ui.tabla_colas_6.item(i,5).text()))
        tiemposervicio=int(str(self.ui.tabla_colas_6.item(i,5).text())) #obtenemos el  valor de la tabla (tiemposervicio entre tiemposervicio)
        valtiempos=tiemposervicio*60 #lo convertimos en minutos


        mastiempos= horatempo + timedelta(seconds=int(valtiempos)) #lo sumamomos
        print "ya sumado",str(mastiempos.strftime(formato))

        self.ui.tabla_colas_6.setItem(i,6, QtGui.QTableWidgetItem(str(mastiempos.strftime(formato)))) # se pasa directo ya sumado


      
        ## 
        ## Tiempo de espera del Camion
        ##

        print "hora llegada" ,self.ui.tabla_colas_6.item(i,2).text()
        print "hora servicio" ,self.ui.tabla_colas_6.item(i,3).text()

        horaobtenida=str(self.ui.tabla_colas_6.item(i,2).text())
        horaobtenida2=str(self.ui.tabla_colas_6.item(i,3).text())

        horainicio_llegada =  datetime.strptime(horaobtenida, formato)
        horainicio_servicio = datetime.strptime(horaobtenida2, formato)
        print llegada
        print horainicio_servicio



        tiempo_espera=horainicio_servicio - horainicio_llegada
        print "tiempo de espera" ,tiempo_espera
        self.ui.tabla_colas_6.setItem(i,8, QtGui.QTableWidgetItem(str(tiempo_espera))) # se pasa directo ya sumado


        ##




    except Exception, e:
      print e






    print "\n FIN \n"  
 



    trabajado=510 #8:30 to minutos
    valor_normal= Decimal(str(self.ui.line_salario_normal.text())) 
    print valor_normal
    valorxminuto=valor_normal/Decimal(60)
    print valorxminuto

    totalnormal=valorxminuto * Decimal(trabajado)
    print totalnormal
    numeropersonas=6
    total_totalnormal=numeropersonas*totalnormal
    print total_totalnormal
    self.ui.line_normal_11.setText(str(round(total_totalnormal,3)))


    extra=0
    valor_extra= Decimal(str(self.ui.line_salario_extra.text()))
    print valor_extra
    valorxminuto_extra=valor_extra/Decimal(60)
    print valorxminuto_extra

    totalextra=valorxminuto_extra * Decimal(extra)
    print totalextra

    total_totalextra=numeropersonas*totalextra
    print total_totalextra
    self.ui.line_extra_11.setText(str(round(total_totalextra,3)))


    total_salarios=total_totalextra + total_totalnormal
    print total_salarios
    self.ui.line_totals_11.setText(str(round(total_salarios,3)))



    print "OCIO"
    sumatoriaocio=Decimal(20)
    valor_ocio= Decimal(str(self.ui.line_val_camion.text()))
     #obtenemos hora de ocio
    print valor_ocio
    valorxminuto_ocio=valor_ocio/Decimal(60)
    print valorxminuto_ocio
    totalocio=valorxminuto_ocio * Decimal(sumatoriaocio)
    print "total ocio",totalocio
    self.ui.line_camion_11.setText(str(round(totalocio,3)))



    print "Almacem"

    sumatoriaalmacen=Decimal(480)
    valor_almacen= Decimal(str(self.ui.line_val_almacen.text())) 
    print valor_almacen
    valorxminuto=valor_almacen/Decimal(60)
    print valorxminuto

    totalalmacen=valorxminuto * Decimal(sumatoriaalmacen)
    print "total almacen",totalalmacen
    self.ui.line_operacion_11.setText(str(round(totalalmacen,3)))

    

    total_total=total_salarios+ totalocio+ totalalmacen
    print "TOTAL" ,total_total
    self.ui.line_total_11.setText(str(round(total_total,3)))


    lista=[]


    "3 personas",Decimal(str(self.ui.line_total_3.text()))
    "4 personas",Decimal(str(self.ui.line_total_9.text()))
    "5 personas",Decimal(str(self.ui.line_total_10.text()))
    "6 personas",Decimal(str(self.ui.line_total_11.text()))
   
    tres=Decimal(str(self.ui.line_total_3.text()))
    cuatro=Decimal(str(self.ui.line_total_9.text()))
    cinco=Decimal(str(self.ui.line_total_10.text()))
    seis=Decimal(str(self.ui.line_total_11.text()))




    lista.append(tres)
    lista.append(cuatro)
    lista.append(cinco)
    lista.append(seis)

    lista.sort()
    print "primero" ,lista[0]
    valor=lista[0]

    if(valor==tres):
      self.ui.lbl_resultado.setText("El Equipo Optimo para Trabajar es: 3 Personas")

    elif(valor==cuatro):
      self.ui.lbl_resultado.setText("El Equipo Optimo para Trabajar es: 4 Personas")

    elif(valor==cinco):
      self.ui.lbl_resultado.setText("El Equipo Optimo para Trabajar es: 5 Personas")

    elif(valor==seis):
      self.ui.lbl_resultado.setText("El Equipo Optimo para Trabajar es: 6 Personas")















####### BOTONES ###########



  def mostrar1(self):
    self.ui.UNO.setFocus()


  def mostrar2(self):
    self.ui.DOS.setFocus()


  def mostrar3(self):
    self.ui.TRES.setFocus()


  def mostrar4(self):
    self.ui.CUATRO.setFocus()


  def mostrar5(self):
    self.ui.CINCO.setFocus()


  def mostrar6(self):
    self.ui.SEIS.setFocus()


  def mostrar7(self):
    self.ui.SIETE.setFocus()


  def mostrar8(self):
    self.ui.OCHO.setFocus()


  def mostrar9(self):
    self.ui.NUEVE.setFocus()


  def mostrar10(self):
    self.ui.DIEZ.setFocus()



  def mostrar11(self):
    self.ui.ONCE.setFocus()


  def mostrar12(self):
    self.ui.DOCE.setFocus()


  def mostrarprincipal(self):
    self.ui.PRINCIPAL.setFocus()





  def displayNext(self):
     self.ui.mdiArea.activateNextSubWindow()

  def displayPrevious(self):
      self.ui.mdiArea.activatePreviousSubWindow()

  def closeAll(self):
     self.ui.mdiArea.closeAllSubWindows()

  def cascadeArrange(self):
     self.ui.mdiArea.cascadeSubWindows()

  def tileArrange(self):
     self.ui.mdiArea.tileSubWindows()

  def SubWindowView(self):
     self.ui.mdiArea.setViewMode(0)

  def TabbedView(self):
     self.ui.mdiArea.setViewMode(1)

  def tablaclose(self):
     self.ui.tabla_mix.clear()


if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   tabla  = QtGui.QTableWidget()
   tableItem  = QtGui.QTableWidgetItem()
   myapp = MyForm()
   myapp.show()
   sys.exit(app.exec_())
