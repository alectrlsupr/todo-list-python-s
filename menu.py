from todolist import TodoList
import sys

class Menu:
    # TODO: And option for help 

    def __init__(self):
      self.todolist = TodoList()
      self.options = {
        "1": self.create_todo,
        "2": self.show_todo,
        "3": self.complete_todo,
        "4": self.update_todo,
        "5": self.delete_todo, 
        "6": self.quit, 

       }  

    def display_menu(self):
      print("""
    
    Bienvenido al sistema de gestión de tareas pendientes.
    Selecciona una alternativa:

    1. Crear un pendiente
    2. Revisar un pendiente
    3. Marcar como completado un pendiente
    4. Modificar un pendiente
    5. Eliminar un pendiente 
    6. Salir de la aplicación

    """)

    def run(self):
      while True:
        self.display_menu()
        option = input("Selecciona una alternativa ")
        action = self.options.get(option) 
        if action: 
             action()
        else:
            print("la opción seleccionado no es válida")

    def create_todo(self):
        name = input("Ingresar nombre de la tarea")
        description = input("Ingresa la descripción de la tarea")
        self.todolist.add_todo(name, description) 
        pass 

    def show_todo(self):
      pass 

    def complete_todo(self):
      pass

    def update_todo(self):
      pass 

    def delete_todo(self):
      pass 

    def quit(self):
      print("Gracias por usar el sistema de pendientes, hasta luego")
      sys.exit()

    