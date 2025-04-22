from abc import ABC, abstractmethod

class UserRegister(ABC):

    @abstractmethod
    def registrar(self, first_name:str, last_name:str , age:int)->dict:   pass
