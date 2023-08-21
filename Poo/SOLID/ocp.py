# OCP
# Clase abierta para extencion, cerrada para modificacion


# Vamos a crear un programa que envie notificaciones a los usuarios.
# Creamos la clase Notificador , lo ideal es que el usuario sea otra clase aparte pero para el ejemplo de ocp va a servir
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        # Al crear este metodo con la siguiente implementacion hacemos que al heredar sea obligatorio agregarlo
        raise NotImplementedError


# Por ejemplo, creamoms una clase que notifique por whatsapp que herede de Notificador
class NotificarPorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Whatsapp a {self.usuario.whatsapp}")


# Usariamos esta parte {self.usuario.whatsapp} si tuvieramos una clase Usuario que contenga todos los datos de contacto del usuario incluido el whatsapp


# Por ejemplo, creamoms una clase que notifique por email que herede de Notificador
class NotificarMail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por eMail a {self.usuario.email}")


# Usariamos esta parte {self.usuario.email} si tuvieramos una clase Usuario que contenga todos los datos de contacto del usuario incluido el email
# Y asi hariamos lo mismo si queremos notificar por otros medios sms, twitter, facebook, etc

# De esta manera estamos expandiendo la clase Notificador sin modificar el codigo padre que es la clase Notificador
# Por lo tanto estamos cumpliendo con el principio OCP porque la clase es expandible facilmente pero no la estamos modificando cuando la expandimos.
