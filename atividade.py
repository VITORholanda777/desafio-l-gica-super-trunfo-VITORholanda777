#include <stdio.h>
#include <string.h>

// Estrutura para representar uma carta de país
typedef struct {
    char nome[50];
    int populacao;
    int area;
    int pib;
    int densidade_demografica;
} Carta;

// Função para exibir os atributos disponíveis
void exibirAtributos() {
    printf("\nEscolha um atributo para comparar:\n");
    printf("1 - Populacao\n");
    printf("2 - Area\n");
    printf("3 - PIB\n");
    printf("4 - Densidade Demografica\n");
}

// Função para obter o valor do atributo selecionado
int obterAtributo(Carta c, int opcao) {
    switch (opcao) {
        case 1: return c.populacao;
        case 2: return c.area;
        case 3: return c.pib;
        case 4: return c.densidade_demografica;
        default: return -1;
    }
}

// Função para exibir o nome do atributo escolhido
const char* nomeAtributo(int opcao) {
    switch (opcao) {
        case 1: return "Populacao";
        case 2: return "Area";
        case 3: return "PIB";
        case 4: return "Densidade Demografica";
        default: return "Desconhecido";
    }
}

int main() {
    // Cartas pré-cadastradas
    Carta carta1 = {"Brasil", 213000000, 8515767, 1440000, 25};
    Carta carta2 = {"Argentina", 45100000, 2780400, 500000, 16};

    int escolha1, escolha2;

    // Escolha do primeiro atributo
    exibirAtributos();
    printf("Escolha o primeiro atributo: ");
    scanf("%d", &escolha1);

    // Escolha do segundo atributo (não pode ser igual ao primeiro)
    do {
        exibirAtributos();
        printf("Escolha o segundo atributo (diferente do primeiro): ");
        scanf("%d", &escolha2);
    } while (escolha2 == escolha1);

    // Obtendo os valores dos atributos escolhidos para cada carta
    int valor1_carta1 = obterAtributo(carta1, escolha1);
    int valor2_carta1 = obterAtributo(carta1, escolha2);
    int valor1_carta2 = obterAtributo(carta2, escolha1);
    int valor2_carta2 = obterAtributo(carta2, escolha2);

    // Comparação individual de atributos
    int pontos_carta1 = (escolha1 == 4 ? (valor1_carta1 < valor1_carta2) : (valor1_carta1 > valor1_carta2)) ? 1 : 0;
    pontos_carta1 += (escolha2 == 4 ? (valor2_carta1 < valor2_carta2) : (valor2_carta1 > valor2_carta2)) ? 1 : 0;
    
    int pontos_carta2 = 2 - pontos_carta1;
    
    // Soma dos valores dos atributos
    int soma_carta1 = valor1_carta1 + valor2_carta1;
    int soma_carta2 = valor1_carta2 + valor2_carta2;

    // Exibindo os resultados
    printf("\nComparacao entre %s e %s:\n", carta1.nome, carta2.nome);
    printf("%s: %d vs %d\n", nomeAtributo(escolha1), valor1_carta1, valor1_carta2);
    printf("%s: %d vs %d\n", nomeAtributo(escolha2), valor2_carta1, valor2_carta2);
    printf("Soma total: %d vs %d\n", soma_carta1, soma_carta2);

    // Determinar o vencedor
    if (soma_carta1 > soma_carta2) {
        printf("Vencedor: %s!\n", carta1.nome);
    } else if (soma_carta2 > soma_carta1) {
        printf("Vencedor: %s!\n", carta2.nome);
    } else {
        printf("Empate!\n");
    }

    return 0;
}


