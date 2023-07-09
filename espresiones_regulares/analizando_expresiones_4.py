#       VALIDANDO UN MAIL CON EXPRESIONES REGULARES

import re

email = "mariano.3gs@gmail.com"


# analizamos por partes la expresion regular 
# el guion medio sirve para hacer separaciones desde-hasta

#       PRIMER CONJUNTO DEL PATRON [a-zA-Z0-9._%+-]

# formato que tiene que tener el patron para ser True o valido
# puede contener valores de la a a la z minus [a-z
# puede contener valores de la A a la Z mayus [a-zA-Z
# puede contener numeros del 0 al 9 [a-zA-Z0-9
# con el . sin la barra le indicamos que puede contener todo lo que no sea un espacio en linea
# todo lo que no sea un espacio en linea y los guiones bajos estan permitidos tambien [a-zA-Z0-9._
# el porcentaje es como un comodin, va a validar todo lo que encuentre antes y despues de [a-zA-Z0-9._%
# el + busca una o mas coincidencias, si encuetra 0 no lo valida y cerramos el conjunto [a-zA-Z0-9._%+-]
# el menos no lo menciona en el video que esta haciendo

#       SEGUNDO y TERCER CONJUNTO DEL PATRON +@[a-ZA-Z10-9.-]

# el + nos indica que antes de la @ tiene que haber por lo menos 1 caracter que cumpla con las condiciones antes buscadas [a-zA-Z0-9._%+-]+@
# al estar el + adelante modifica lo que esta atras y como lo que esta atraas esta encerrado en corchetes lo modifica todo junto [a-zA-Z0-9._%+-]+@
# el conjunto siguiente valida lo mismo que el primero [a-zA-Z0-9._%+-]+@[a-ZA-Z10-9.-]+
# validar que halla un . , con la barra invertida le decimos que si o si tiene que haber un punto [a-zA-Z0-9._%+-]+@[a-ZA-Z10-9.-]+\. 
# luego del punto validar que por lo menos tiene que haber 2 caracteres de la de la a-z minus o A-Z mayus

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z10-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

print(result)

# este if valida que la cadena de caracteres

if result:
    print("El email es valido")
else:
    print("El email es invalido")


