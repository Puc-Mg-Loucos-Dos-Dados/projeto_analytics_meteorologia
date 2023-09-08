class T_PrevisaoHora:
    def __init__(self, hora: int,
                 umidade_prevista: float,
                 umidade_medida: float,
                 temperatura_prevista: float = None,
                 temperatura_medida: float = None,
                 sensacao_termica: float = None,
                 ponto_orvalho: float = None,
                 pressao_prevista: float = None,
                 pressao_medida: float = None,
                 vento_velocidade_prevista: float = None,
                 vento_velocidade_medida: float = None,
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
        self.umidade_prevista = umidade_prevista
        self.umidade_medida = umidade_medida
        self.temperatura_prevista = temperatura_prevista
        self.temperatura_medida = temperatura_medida
        self.sensacao_termica = sensacao_termica
        self.ponto_orvalho = ponto_orvalho
        self.pressao_prevista = pressao_prevista
        self.pressao_medida = pressao_medida
        self.vento_velocidade_prevista = vento_velocidade_prevista
        self.vento_velocidade_medida = vento_velocidade_medida
        self.vento_velocidade_maxima_prevista = vento_velocidade_maxima_prevista
        self.vento_direcao = vento_direcao
        self.chuva = chuva
        self.chuva_probabilidade = chuva_probabilidade
        self.nevoeiro = nevoeiro
        self.cota_neve = cota_neve
        self.nuvens = nuvens
        self.uv_coberto = uv_coberto
        self.uv_despejado = uv_despejado
