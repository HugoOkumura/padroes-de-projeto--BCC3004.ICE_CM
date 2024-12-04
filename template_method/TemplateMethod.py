from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        '''
        O template_method define o esqueleto do algoritmo
        '''
        self.base_operation1()
        self.required_operation1()

        self.base_operation2()
        self.required_operation2()

    # Operações que já possui implementação
    def base_operation1(self):
        print("Operação base 1")
    
    def base_operation2(self):
        print("Operação base 2")

    # Operações específicas para cada subclasse
    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass


class ConcreteClass1(AbstractClass):

    #implementação específica da classe concreta 1
    def required_operation1(self): 
        print("ConcreteClass1: operação especifica 1")

    def required_operation2(self): 
        print("ConcreteClass1: operação especifica 1")

class ConcreteClass2(AbstractClass):

    #implementação específica da classe concreta 1
    def required_operation1(self):
        print("ConcreteClass2: operação especifica 1")

    def required_operation2(self):
        print("ConcreteClass2: operação especifica 2")
