# Sistema Antigo
class LeitorTemperaturaLegado:
    def get_temperatura_legado(self):
        return input("Insira a temperatura: ")  # Temperatura em lida como uma string

class SistemaNovo: # Sistema que espera um float
    def mostraTemperatura(self, adapter):
        temperatura = adapter.get_temperatura()
        print(f"A temperatura é: {temperatura}°C") 
        ## parte da implementação que utilizaria o dado como um float

class TemperatureAdapter: # Adapter que tranforma a string do leitor legado em um float para o sistema novo
    def __init__(self, sistemaLegado):
        self.sistemaLegado = sistemaLegado
    def get_temperatura(self):
        temperatura = self.sistemaLegado.get_temperatura_legado()  # sistema antigo le uma string
        return float(temperatura)  # Converte de string para float


old_system = LeitorTemperaturaLegado()

adapter = TemperatureAdapter(old_system)

display = SistemaNovo()


display.mostraTemperatura(adapter)