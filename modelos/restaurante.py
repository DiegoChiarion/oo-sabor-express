# Criação da classe Restaurante
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print()
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(20)} | {r.categoria.ljust(20)} | {r.ativo}')

    @property
    def ativo(self):
        return '☑ Ativo' if self._ativo else '☐ Inativo'
    

    def alternar_estado(self):
        self._ativo = not self._ativo


'''# Criação dos objetos pertencentes a essa clase:
restaurante_praca = Restaurante('praça', 'Lanches')
restaurante_garp = Restaurante('blue Garp', 'Frutos do Mar')
restaurante_garp.alternar_estado()
restaurante_praca.alternar_estado()

Restaurante.listar_restaurantes()

# Acessando objeto
restaurante_garp.nome = 'Blue Garp'
restaurante_garp.categoria = 'Frutos do Mar'''