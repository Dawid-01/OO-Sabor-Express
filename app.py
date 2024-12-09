from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante ('Los pollos hermanos', 'Mexicano')
restaurante_italino = Restaurante ('Italianiii', 'italino')

bebida_suco = Bebida('MelanJuyce', 5.00, 'grande')
prato_massa = Prato('Lasanha', 15.00, 'Bolonhesa com mussarela e muito molho')
bebida_suco.aplicar_desconto()
prato_massa.aplicar_desconto()
restaurante_italino.adicionar_no_cardapio(bebida_suco)
restaurante_italino.adicionar_no_cardapio(prato_massa)


restaurante_mexicano.alternar_estado()

def main():
   restaurante_italino.exibir_cardapio

if __name__ == '__main__':
    main()