class T_PrevisaoHora:
    def __init__(self, hora: int,
                 umidade_relativa: float,
                 temperatura: float = None,
                 sensacao_termica: float = None,
                 ponto_orvalho: float = None,
                 pressao: float = None,
                 vento_velocidade: float = None,
                 vento_velocidade_maxima_prevista: float = None,
                 vento_direcao: str = None,
                 chuva: float = None,
                 chuva_probabilidade: float = None,
                 nevoeiro: bool = False,
                 cota_neve: int = None,
                 nuvens: float = None,
                 uv_coberto: float = None,
                 uv_despejado: float = None):
        self.hora = hora
        self.umidade_relativa = umidade_relativa
        self.temperatura = temperatura
        self.sensacao_termica = sensacao_termica
        self.ponto_orvalho = ponto_orvalho
        self.pressao = pressao
        self.vento_velocidade = vento_velocidade
        self.vento_velocidade_maxima_prevista = vento_velocidade_maxima_prevista
        self.vento_direcao = vento_direcao
        self.chuva = chuva
        self.chuva_probabilidade = chuva_probabilidade
        self.nevoeiro = nevoeiro
        self.cota_neve = cota_neve
        self.nuvens = nuvens
        self.uv_coberto = uv_coberto
        self.uv_despejado = uv_despejado
