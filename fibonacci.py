class Fibonacci:
    def __init__(self) -> None:
        self.sequencia = list()
    
    def __fib(self,value:int)->int:
        if value == 0:
            return 0
        
        elif value == 1 or value == 2:
            return 1
        
        else:
            return self.__fib(value-1) + self.__fib(value-2)
    
    def getSequencia(self,elements)->list:
        for i in range(elements+1):
            self.sequencia.append(self.__fib(i))
        return self.sequencia

class TesteValueFibonacci:
    def __init__(self,valueTotest:int) -> None:
        self.valueTotest = valueTotest
    
    def test(self):
        fib = Fibonacci()
        index = 0
        seq = fib.getSequencia(index)
        while self.valueTotest not in seq:
            if self.valueTotest < seq[-1]:
                return False
            index += 1
            seq = fib.getSequencia(index)
        return True


value = int(input("Digite um número para verificar se ele pertence a sequencia de fibonacci: "))
verifica = TesteValueFibonacci(value).test()
if verifica:
    print("O valor pertence a sequência")
else:    
    print("O valor não pertence a sequência")


