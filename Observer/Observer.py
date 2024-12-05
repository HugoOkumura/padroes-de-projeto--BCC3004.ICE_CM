from abc import ABC, abstractmethod

# Subject (Sujeito)
class Subject:
    def __init__(self):
        self._observers = []  # Lista de observadores
    
    def attach(self, observer):
        """Adiciona um observador"""
        self._observers.append(observer)
    
    def detach(self, observer):
        """Remove um observador"""
        self._observers.remove(observer)
    
    def notify(self):
        """Notifica todos os observadores"""
        for observer in self._observers:
            observer.update(self)

# Observer (Observador)
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        """Atualiza o estado do observador"""
        pass

# Um Subject específico
class Blog(Subject):
    def __init__(self):
        super().__init__()
        self._latest_post = None  # Última postagem do blog

    @property
    def latest_post(self):
        return self._latest_post
    
    @latest_post.setter
    def latest_post(self, post):
        self._latest_post = post
        self.notify()  # Notifica os observadores sobre a mudança
