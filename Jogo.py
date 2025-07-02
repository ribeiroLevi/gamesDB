class Jogo(object):

 ##buscar como fazer o relacionamento com outros classes/foreing keys

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):   
        self._id = id
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricao(self):
        return self._descricao
    @nome.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def idioma(self):
        return self._idioma
    @nome.setter
    def idioma(self, idioma):
        self._idioma = idioma

    @property
    def duracao(self):
        return self._duracao
    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def min_jogadores(self):
        return self._min_jogadores 
    @min_jogadores.setter
    def min_jogadores(self, min_jogadores):
        self._min_jogadores = min_jogadores

    @property
    def max_jogadores(self):  
        return self._max_jogadores
    @max_jogadores.setter
    def max_jogadores(self, max_jogadores):
        self._max_jogadores = max_jogadores

    
    

    