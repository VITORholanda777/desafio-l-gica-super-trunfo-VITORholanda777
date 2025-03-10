class Cidade:
    def __init__(self, estado, codigo, nome, populacao, area, pib, pontos_turisticos):
        self.estado = estado
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
        self.area = area
        self.pib = pib
        self.pontos_turisticos = pontos_turisticos
        self.densidade_populacional = self.populacao / self.area if self.area > 0 else 0
        self.pib_per_capita = self.pib / self.populacao if self.populacao > 0 else 0

    def exibir_dados(self):
        print(f"\nCarta: {self.nome} ({self.estado})")
        print(f"Código: {self.codigo}")
        print(f"População: {self.populacao}")
        print(f"Área: {self.area:.2f} km²")
        print(f"PIB: R$ {self.pib:.2f}")
        print(f"Pontos turísticos: {self.pontos_turisticos}")
        print(f"Densidade Populacional: {self.densidade_populacional:.2f} hab/km²")
        print(f"PIB per capita: R$ {self.pib_per_capita:.2f}")


def cadastrar_cidade(dados):
    estado, codigo, nome, populacao, area, pib, pontos_turisticos = dados
    cidade = Cidade(estado, codigo, nome, int(populacao), float(area), float(pib), int(pontos_turisticos))
    print("\nCidade cadastrada com sucesso!")
    cidade.exibir_dados()
    return cidade


def comparar_cartas(cidade1, cidade2, atributo):
    valor1 = getattr(cidade1, atributo)
    valor2 = getattr(cidade2, atributo)

    print(f"\nComparação pelo atributo: {atributo.replace('_', ' ').title()}")
    print(f"{cidade1.nome}: {valor1:.2f}")
    print(f"{cidade2.nome}: {valor2:.2f}")
    
    if atributo == "densidade_populacional":
        vencedor = cidade1 if valor1 < valor2 else cidade2 if valor2 < valor1 else None
    else:
        vencedor = cidade1 if valor1 > valor2 else cidade2 if valor2 > valor1 else None

    if vencedor:
        print(f"\nA cidade vencedora é: {vencedor.nome}!")
    else:
        print("\nEmpate!")


# Fluxo principal

def main():
    print("Bem-vindo ao jogo Super Trunfo de Cidades!")
    print("Usando dados predefinidos para teste...")
    
    dados_cidade1 = ["SP", "001", "São Paulo", "12300000", "1521", "2100000000000", "120"]
    dados_cidade2 = ["RJ", "002", "Rio de Janeiro", "6748000", "1200", "1200000000000", "80"]
    
    cidade1 = cadastrar_cidade(dados_cidade1)
    cidade2 = cadastrar_cidade(dados_cidade2)
    
    atributos = ["populacao", "area", "pib", "densidade_populacional", "pib_per_capita"]
    escolha = 0  # Simula a escolha de um atributo (pode ser ajustado)
    
    comparar_cartas(cidade1, cidade2, atributos[escolha])


if __name__ == "__main__":
    main()
