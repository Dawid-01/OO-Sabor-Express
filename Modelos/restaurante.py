from Modelos.avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    #property pode pegar um atributo e modificar como este atributo vai ser lido
    @property 
    def ativo(self):
        return 'Ativado' if self._ativo else 'desativado'


    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota )
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao: #senao tiver nenhuma avalicao retorna 0
            return ' - '
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #utilizando sum, a gente somou especificando que só queremos a nota da avaliação
        quantidade_notas = len(self._avaliacao) # aqui vemos a quantidade de notas que temos
        media = round(soma_das_notas / quantidade_notas,1) # temos a media, e utilizando o round mostramos apenas uma casa decimal
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.tamanho}'
                print(mensagem_bebida)