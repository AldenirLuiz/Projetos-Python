
snake_names = {
    "cascavel": "\n Cascavél (Crotalus durissus) é uma cobra venenosa da família Viperidae, subfamília Crotalinae, e sua distribuição geográfica está restrita a América do Sul, da Colômbia até a Argentina de forma descontínua. Estas serpentes possuem um veneno neurotóxico, que atua no sistema nervoso e faz com que a vítima tenha dificuldades de locomoção e respiração. É uma serpente com hábitos predominantemente noturnos, é terrestre e pouco ágil. No Brasil, cinco subespécies de cascavéis podem ser encontradas em áreas do Cerrado, nas regiões áridas e semi-áridas do Nordeste e em áreas abertas do Sul, Sudeste e Nordeste.\n",
    "jararaca": "\n Bothrops jararaca > é uma serpente de até 1,6 m, encontrada no Brasil (da Bahia ao Rio Grande do Sul) e em regiões adjacentes no Paraguai e Argentina.",
    "coral": "\n Micrurus corallinus > Cobra-coral é uma denominação comum a várias serpentes da família Elapidae, da tribo Calliophini, que podem ser subdivididas em dois grupos: corais do Velho Mundo e corais do Novo Mundo. Existem 16 espécies de corais do Velho Mundo, pertencentes aos gêneros Calliophis, Hemibungarus e Sinomicrurus, e mais de 65 espécies de corais do Novo Mundo, incluídas nos gêneros Leptomicrurus, Micruroides, e Micrurus. Estudos genéticos indicam que as linhagens mais basais de corais se encontram na Ásia, indicando que elas se originaram no Velho Mundo. No Brasil, podem ser conhecidas pelos nomes cobra-coral-venenosa, coral-venenosa, coral-verdadeira,ibiboboca,ibiboca e ibioca.\n ",
    "mussurana": "\n Clelia Clelia > Seus hábitos foram descobertos pelo médico e cientista brasileiro Vital Brasil (1865-1950). Pesquisador do ofidismo,[5] Vital Brazil apresentou, em uma conferência em 1915, um filme, de 1911, mostrando a luta de uma muçurana contra uma jararaca, Pertence a família Dipsadidae. Seu porte vai de pequeno a médio,podendo chegar a medir 2,40 metros de comprimento quando alcançar a vida adulta. A sua coloração varia de acordo com a idade, possuindo uma coloração rosada com cabeça escura, quando jovem, e quando adultos são preto azuladas com uma faixa branca na parte ventral, Apresenta veneno na sua peçonha mas não apresenta risco ao ser humano.\n ",
    "naja": "\n Naja é um gênero de cobras-capelo, serpentes peçonhentas da família Elapidae (cobras). Seu habitat estende-se a toda a África, Sudoeste da Ásia, Sul da Ásia e Sudeste Asiático. Apesar de vários outros gêneros de cobras-capelo poderem ser designados, na língua corrente, por naja, as najas propriamente ditas são as cobras-capelo do gênero Naja, o grupo mais reconhecido e mais difundido de cobras-capelo. O gênero Naja consiste de 20 a 22 espécies, mas sofreu várias revisões taxonômicas nos últimos anos, portanto, as fontes variam muito. São animais peçonhentos, agressivos e bastante perigosos",    
    "cobra rei": "\n A cobra-real (Ophiophagus hannah) é uma espécie de serpente peçonhenta da família dos Elapídeos, autóctone da Ásia meridional e do sudeste asiático, que habita as planícies e florestas tropicais da Índia e da China, bem entre outras nações do sudeste asiático, Está ameaçada pela destruição do seu habitat e encontra-se listada como vulnerável na Lista Vermelha da IUCN desde 2010. É a maior cobra peçonhenta conhecida. Cobras-reais adultas normalmente vão de 3 a 4 metros de comprimento, sendo que a maior já registrada chegou a medir 5,85 m. \nApesar de contar com o substantivo cobra no nome, esta espécie não pertence ao gênero Naja, mas é o único membro do gênero Ophiophagus.É carnívora e a sua dieta consiste basicamente em outros ofídios, venenosos ou não, mas não despreza lagartos, ovos e pequenos mamíferos.O nome científico Ophiophagus significa literalmente, a comedora de serpentes.\n ",  
    "python": "\n Python é um gênero de répteis da família Pythonidae. Pode ser encontrado na Ásia e África. Popularmente são denominadas de pitão ou píton. Nenhuma das serpentes desta família possui dentes inoculadores de veneno, porém possuem presas afiadas curvadas pra dentro para agarrar sua presa.\n",
}

class AskMeSnake:
    def __init__(self) -> None:
        self.ask = self.ask_me()
        self.answer = snake_names.get(self.ask)

    @staticmethod
    def ask_me() -> str:
        return input("Digite o nome da serpente para consultar: ").lower()
    
    def show_answer(self):
        if self.answer:
            print(self.answer)
        else:
            print(f"Nenhuma serpente com este nome foi encontrada na base de dados.")

if __name__ == "__main__":
    snake = AskMeSnake().show_answer()