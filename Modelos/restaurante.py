class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    
    def listar_restaurantes():
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    #property pode pegar um atributo e modificar como este atributo vai ser lido
    @property 
    def ativo(self):
        return 'Ativado' if self._ativo else 'desativado'


    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza XJSON', 'Pizza')

Restaurante.listar_restaurantes()

