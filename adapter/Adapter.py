# Sistema Antigo
class LeitorTemperaturaLegado:
    def get_temperatura_legado(self):
        return input("Insira a temperatura: ")  # Temperatura em lida como uma string

class SistemaNovo:
    def mostraTemperatura(self, adapter):
        temperatura = adapter.get_temperatura()
        print(f"A temperatura é: {temperatura}°C") 
        ## parte da implementação que utilizaria o dado como um float

# Adapter
class TemperatureAdapter:
    def __init__(self, old_system):
        self.old_system = old_system
    def get_temperatura(self):
        temperatura = self.old_system.get_temperatura_legado()  # sistema antigo le uma string
        return float(temperatura)  # Converte de string para float


old_system = LeitorTemperaturaLegado()

adapter = TemperatureAdapter(old_system)

display = SistemaNovo()
# Adapter para converter para Celsius

# Exibe a temperatura convertida para Celsius

display.mostraTemperatura(adapter)