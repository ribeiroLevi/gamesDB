class JogoUsuario(object):
    @property
    def local(self):
        return self._local
    @local.setter
    def local(self, local):
        self._local = local

    @property
    def dataAquisicao(self):
        return self._dataAquisicao
    @dataAquisicao.setter
    def dataAquisicao(self, dataAquisicao):
        self._dataAquisicao = dataAquisicao
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status