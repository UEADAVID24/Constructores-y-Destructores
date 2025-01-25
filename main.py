class FileManager:
    """
    Clase para gestionar archivos con uso de constructores (__init__) y destructores (__del__).
    """

    def __init__(self, file_name, mode):
        """
        Constructor que inicializa los atributos del objeto y abre un archivo en el modo especificado.
        :param file_name: Nombre del archivo.
        :param mode: Modo de apertura del archivo ('r', 'w', 'a', etc.).
        """
        self.file_name = file_name
        self.mode = mode
        try:
            self.file = open(self.file_name, self.mode)
            print(f"Archivo '{self.file_name}' abierto correctamente en modo '{self.mode}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.file = None

    def write_to_file(self, content):
        """
        Método para escribir contenido en el archivo.
        :param content: Texto a escribir en el archivo.
        """
        if self.file and not self.file.closed and 'w' in self.mode or 'a' in self.mode:
            self.file.write(content)
            print(f"Contenido escrito en '{self.file_name}'.")
        else:
            print(f"No se pudo escribir en el archivo '{self.file_name}'. Verifica el modo de apertura.")

    def __del__(self):
        """
        Destructor que se activa al eliminar el objeto. Cierra el archivo si está abierto.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado correctamente.")
        else:
            print(f"El archivo '{self.file_name}' ya estaba cerrado o no fue abierto correctamente.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto FileManager para escribir en un archivo
    manager = FileManager("example.txt", "w")
    manager.write_to_file("Este es un ejemplo de uso de constructores y destructores en Python.\n")

    # El destructor se activará automáticamente al finalizar el programa o al eliminar el objeto
    del manager  # Destructor llamado explícitamente (opcional)

