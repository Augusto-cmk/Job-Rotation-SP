class String_inv:
    def __init__(self,string:str) -> None:
        self.string = string
    
    def __str__(self) -> str:
        return self.__inverse()

    def __inverse(self)->str:
        newStr = ""
        i = len(self.string) - 1
        while i >= 0:
            newStr += self.string[i]
            i -= 1
        return newStr


entrada = input("Entre com a string que deseja inverter: ")
print(f"String invertida: {String_inv(entrada)}")
