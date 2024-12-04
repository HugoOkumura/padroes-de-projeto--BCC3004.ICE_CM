class ProxyDesign:
   class Subject:
       def do_action(self):
           pass

   class RealSubject(Subject):
       def do_action(self):
           # Implementa o comportamento
           pass

   class Proxy(Subject):
       def __init__(self):
           self.real_subject = None

       def do_action(self):
           print("Proxy performing additional logic...")
           self.get_real_subject().do_action()

       def get_real_subject(self):
           if self.real_subject is None:
               self.real_subject = self.RealSubject()
           return self.real_subject

def main():
   proxy = ProxyDesign.Proxy()
   proxy.do_action()

if __name__ == "__main__":
   main()