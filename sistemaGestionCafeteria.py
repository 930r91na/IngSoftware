
class Bebida:
    def __init__(self, nombre, tamaños):
        self.nombre = nombre
        self.tamaños = tamaños
    
    def __str__(self):
        return f"{self.nombre} ({', '.join(map(str, self.tamaños))})"
    
    def inputStr(string):
        # This function will receive a string in the format "nombre, tamaño1, tamaño2, tamaño3, tamaño4"
        parts = string.split(",")
        
        # Ignore the spaces
        nombre = parts[0].strip()

        if nombre == None or nombre == "":
            raise ValueError("There is no name in the drink")
    
        # Check that parts can be converted to integers
        for i in parts[1:]:
            try:
                int(i)
            except:
                raise ValueError("Sizes are not integers")
            
        # Ignore the spaces and convert the sizes to integers
        tamaños = [int(tamaño.strip()) for tamaño in parts[1:]]

        # Check that tamaño is not null 
        if tamaños == None:
            raise ValueError("There are no sizes in the drink")
        
        # Check that nombre is between 2-15 characters
        if len(nombre) < 2 or len(nombre) > 15:
            raise ValueError("Name is not between 2-15 characters")
        
        # Check that nombre has only letters
        if nombre.isalpha() == False:
            raise ValueError("Name has non-letter characters") 

        # Check that there is no more than 5 sizes
        if len(tamaños) > 5:
            raise ValueError("There cannot be more than 5 sizes")

        # Check that tamaños is in ascending order, positive, not null and between 1-48
        for i in range(len(tamaños) -1):
            if tamaños[i] >= tamaños[i + 1]:
                raise ValueError("Sizes are not in ascending order")
            if tamaños[i] <= 0:
                raise ValueError("Sizes are not positive")
            if tamaños[i] > 48:
                raise ValueError("Sizes cannot be greater than 48")
            if tamaños[i] == None:
                raise ValueError("Sizes are null")

        
        return Bebida(nombre, tamaños)

# Main 
# Print the drink name and sizes
# print(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44")) 


# entry = input("Enter the drink name and sizes separated by commas: ")
# print(Bebida.inputStr(entry))