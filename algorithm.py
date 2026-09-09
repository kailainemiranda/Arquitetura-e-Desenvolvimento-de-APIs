import math
from datetime import datetime

def calculate_retention(last_studied_at: datetime, stability_factor: float = 7.0) -> float:
    """
    Calcula a retenção de memória com base na Curva de Ebbinghaus:
    R = exp(-t / S)
    onde 't' é o tempo decorrido em dias e 'S' é o fator de estabilidade.
    """
    now = datetime.utcnow()
    elapsed_days = (now - last_studied_at).total_seconds() / 86400.0
    if elapsed_days < 0:
        elapsed_days = 0
        
    retention = math.exp(-elapsed_days / max(stability_factor, 1.0))
    return round(retention * 100, 2)
