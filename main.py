import random
import time

intentos=0
suerte= 0
iniciar_trivia=True


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
RESET = '\033[39m'
#  bienvenida de trivia
time.sleep(1.7)
print ("\n !!! Alto mortal ¡¡¡ Soy el Gran ZODD y tendrás que responder una serie de \n preguntas si es que quieres vivir. Estoy al tanto del conocimiento \n de tu mundo, así que no seré tan cruel, el tema será sobre Marvel's \n Comics, soy consciente que es algo muy popular en tu mundo,sino fuiste muy \n seguidor de estos")
time.sleep(2.5)
print("\n...\n \n !!!Pues mala suerte¡¡¡ MUAJAJAJAJAJ\n")
time.sleep(2)
print ("\n Discúlpame mortal, me deje llevar jeje \n ahora dime tu nombre y de que lugar provienes\n para hacerlo oficial de una vez\n")
nombre = input("Ingresa tu nombre: ")
lugar= input("Ingresa el lugar de donde eres: ")
time.sleep(1.2)
print(RED+"\n\n*Recuerda:Necesitas de 4 o 5 puntos para pasar la prueba  no más, no menos "+RESET)
time.sleep(1.2)
print("\n \n", nombre,"de",lugar, "responde las siguientes preguntas escribiendo \n la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
time.sleep(1.2)
print("\n Se me olvidaba, dime el nombre a quien se le entregarán tus restos en caso \n de tu muy probable fracaso.\n")
nombre2= input("Ingresa el nombre: ")
time.sleep(1.2)
print(YELLOW+"\n PERFECTO. En Total seran unas 5 preguntas que sellaran tu destino.\n Buena Suerte\n"+RESET)


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos +=1
  puntaje = 0
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  # Pregunta 1
  time.sleep(2)
  print("Ahi va la primera")
  time.sleep(1)
  print (RED+"1) ¿Quién es el dios más antiguo en Marvle's Comics?"+RESET)
  print ("a) Thor Odinson")
  print ("b) Odin Borson")
  print ("c) Zeus Panhellenios")
  print ("d) Hercules Panhellenios")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d","z"):
    respuesta_1 = input(MAGENTA+"\nDebes responder a, b, c o d. Tienes suerte que el Gran ZODD es bondadoso y solo tomaré como a, b, c o d como respuesta alguna.\n\n Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_1 == "z":
    puntaje += 10
    print("Hummmm... vamos con la siguiente pregunta\n")
  elif  respuesta_1 == "a":
    print("\nTu",nombre,"de",lugar,",Thor,actual principe de Asgard, es imposible que sea el más antiguo")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_1 == "b":
    print("\nTu",nombre,"de",lugar,"El gran Odin Padre de todo, buen razonamiento, pero lamentablemente te equivocas")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_1 == "d":
    print("\nTu",nombre,"de",lugar,"Heracles es un semidios, es mitad mortal, ni siquiera debiste considerar esa opción, Estas a unn paso más a tu fin")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  else :
    puntaje += 1
    print ("Tu respuesta es correcta ",nombre,"de",lugar, "me impresionas ")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  
  # Pregunta 2
  time.sleep(2)
  print("Segunda pregunta")
  time.sleep(1)
  print (RED+"\n2) ¿A cuál de estos heroes lo llaman 'El gigante verde'?"+RESET)
  print ("a) El increible Hulk")
  print ("b) Wolverine")
  print ("c) Daredevil")
  print ("d) Spiderman")
  
  respuesta_2 = input("\nTu respuesta: ")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  
  while respuesta_2 not in ("a", "b", "c", "d","z"):
    respuesta_2 = input(MAGENTA+"\nDebes responder a, b, c o d. ; Mi bondad tiene límites, aún asi solo tomaré como a, b, c o d como respuesta alguna.\n\n Ingresa nuevamente tu respuesta: "+RESET)
  if  respuesta_2 == "b":
    print("\nTu",nombre,"de",lugar,",A wolverine se le conoce como el Arma X, respuesta incorrecta")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_2 == "z":
    puntaje+=10
    print("Curioso... vamos con la siguiente pregunta\n")
  elif respuesta_2 == "c":
    print("\nTu",nombre,"de",lugar,"A daredevil se le conoce como el diablillo de HellsKitchen, muy mal")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_2 == "d":
    print("\nTu",nombre,"de",lugar,"A Spiderman se le conoce como el trepa muros, donde vives bajo una piedra?")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  else :
    puntaje += 1
    print ("Tu respuesta es correcta ",nombre,"de",lugar, "me impresionas ")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  
  # Pregunta 3
  time.sleep(2)
  print("Tercera pregunta")
  time.sleep(1)
  print (RED+"\n3) ¿Cuál de estos heroes tiene un esqueleto de 'Adamantio'?"+RESET)
  print ("a) The Punisher")
  print ("b) Wolverine")
  print ("c) Black Widow")
  print ("d) Nick Fury")
  
  respuesta_3 = input("\nTu respuesta: ")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  
  while respuesta_3 not in ("a", "b", "c", "d","z"):
    respuesta_3 = input(MAGENTA+"\nDebes responder a, b, c o d. ; Mi bondad tiene límites, aún asi solo tomaré como a, b, c o d como respuesta alguna.\n\n Ingresa nuevamente tu respuesta: "+RESET)
  if  respuesta_3 == "a":
    print("\nTu",nombre,"de",lugar,",Frank Castle es un simple militar sin poderes, sólo habilidad, respuesta incorrecta")
    print("Tu puntajes es de:",puntaje,"puntos.")
  elif respuesta_3 == "z":
    puntaje += 10
    print("Curioso... vamos con la siguiente pregunta\n")
  elif respuesta_3 == "c":
    print("\nTu",nombre,"de",lugar,"BlackWidow es una espía soviética, muy mal")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_3 == "d":
    print("\nTu",nombre,"de",lugar,"Nick fury es solo un hombre sin un ojo, no podría soportar el adamantio en su cuerpo")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  else :
    puntaje += 1
    print ("Tu respuesta es correcta ",nombre,"de",lugar, "me impresionas ")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  
  # Pregunta 4
  time.sleep(2)
  print("Cuarta pregunta")
  time.sleep(1)
  print (RED+"\n4) ¿A que grupo de heroes pertenece 'Ironman'?"+RESET)
  print ("a) X-men")
  print ("b) Avengers")
  print ("c) Alpha Flight")
  print ("d) Damage Control")
  
  respuesta_4 = input("\nTu respuesta: ")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  
  while respuesta_4 not in ("a", "b", "c", "d","z"):
    respuesta_4 = input(MAGENTA+"\nDebes responder a, b, c o d. ; Mi bondad tiene límites, aún asi solo tomaré como a, b, c o d como respuesta alguna.\n\n Ingresa nuevamente tu respuesta: "+MAGENTA)
  if  respuesta_4 == "a":
    print("\nTu",nombre,"de",lugar,",Los X-men son un grupo de los llamados mutantes y Ironman es un humano con un traje tecnológico")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_4 == "z":
    puntaje += 10
    print("Curioso... vamos con la siguiente pregunta\n")
  elif respuesta_4 == "c":
    print("\nTu",nombre,"de",lugar,"Es un grupo canadiense con poderes, porfavor pudiste hacerlo mejor")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_4 == "d":
    print("\nTu",nombre,"de",lugar,"Uno de los mejores heroes del planeta se preocuparia solo de la destrucción que generan las batallas de otros heroes?")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  else :
    puntaje += 1
    print ("Tu respuesta es correcta ",nombre,"de",lugar, "me impresionas ")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  # Pregunta 5
  time.sleep(2)
  print("Quinta y última pregunta")
  time.sleep(1)
  print (RED+"\n5) ¿De qué reino es pertenece el rey Blackagar Boltagon'Black Bolt' ?"+RESET)
  print ("a) Lemuria")
  print ("b) Wakanda")
  print ("c) Asgard")
  print ("d) Attilan")
  
  respuesta_5 = input("\nTu respuesta: ")
  while respuesta_5 not in ("a", "b", "c", "d","z"):
    respuesta_5 = input(MAGENTA+"\nDebes responder a, b, c o d. ; Mi bondad tiene límites, aún asi solo tomaré como a, b, c o d como respuesta alguna.\n\n Ingresa nuevamente tu respuesta: "+RESET)
  if  respuesta_5 == "a":
    print("\nTu",nombre,"de",lugar,",Ese es el reino de los despreciables desviantes")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_5 == "z":
    puntaje += 10
    print("Curioso... vamos con la siguiente pregunta\n")
  elif respuesta_5 == "b":
    print("\nTu",nombre,"de",lugar,"Ese es el reino de del Prncipe T´Chala")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  elif respuesta_5 == "c":
    print("\nTu",nombre,"de",lugar,"La tenías fácil, Thor es principe y Odin es su rey")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")
  else :
    puntaje += 1
    print ("Tu respuesta es correcta ",nombre,"de",lugar, "me impresionas ")
    print("\nTu puntajes es de:",puntaje,"puntos.\n")





  
  time.sleep(3)
  if puntaje <=14 and puntaje>= 4:
    print(YELLOW+"\nTu",nombre,"de",lugar,",supongo que te subestime, puedes conservar tu vida"+RESET)
  
  elif puntaje >= 20 and puntaje <=40 :
    print("\n Pensé que me liberarias, pero NO, no fuiste tan listo.Ahora me cobraré tu vida")
    print(GREEN+"Estas muerto.Obtuviste",puntaje,"puntos. Al parecer",nombre2,"se llevará una desagradable sopresa."+RESET)
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  elif puntaje==50:
   suerte = random.randint(1,10)
   print(MAGENTA+"\n ME HAS LIBERADO, ESTARÉ ETERNAMENTE AGRADECIDO, TE DARÉ UN REGALO ADEMÁS DE CONSERVAR TU VIDA...",suerte,"Serán los años de vida adicionalesque te daré.Creeme sabrás el momento exacto cuando se te dará este regalo"+RESET)
  else:
    print(GREEN+"Estas muerto.Obtuviste",puntaje,"puntos. Al parecer",nombre2,"se llevará una desagradable sopresa."+RESET)
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
 
      
if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False
