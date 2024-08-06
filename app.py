from modelos.restaurante import Restaurante

# Criando objetos da Classe Restaurante:
restaurante_01 = Restaurante('Blue Garp', 'Frutos do Mar')
restaurante_02 = Restaurante('Nohar Steak', 'Churrascaria')
restaurante_03 = Restaurante('King Burguer', 'Lanche')

restaurante_02.alternar_estado()
restaurante_03.alternar_estado()

# Definindo arquivo, como principal:
def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()