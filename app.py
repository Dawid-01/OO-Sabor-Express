from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante ('Los pollos hermanos', 'Mexicano')
restaurante_italino = Restaurante ('Italianiii', 'italino')

restaurante_mexicano.receber_avaliacao('Gui', 10)
restaurante_mexicano.receber_avaliacao('Davi', 6)


restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()