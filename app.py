from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante ('Los pollos hermanos', 'Mexicano')
restaurante_italino = Restaurante ('Italianiii', 'italino')

bebida_suco = Bebida('MelanJuyce' 5.00, 'grande')
prato_massa = ('Lasanha', 15.00, 'Bolonhesa com mussarela e muito molho')



restaurante_mexicano.alternar_estado()

def main():
   pass

if __name__ == '__main__':
    main()