from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
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
        avaliacao = Avaliacao(cliente, nota )
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao: #senao tiver nenhuma avalicao retorna 0
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #utilizando sum, a gente somou especificando que só queremos a nota da avaliação
        quantidade_notas = len(self._avaliacao) # aqui vemos a quantidade de notas que temos
        media = round(soma_das_notas / quantidade_notas,1) # temos a media, e utilizando o round mostramos apenas uma casa decimal
        return media
    
