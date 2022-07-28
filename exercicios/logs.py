#!/usr/bin/env python3

from decimal import DivisionByZero
from logging import handlers
import os
import logging

# logging é root logger
# Não utiliza f-string com a lib logging pois o fstring possui avaliação imediata

#BOILDERPLATE
# TODO: Usar funcao
 # TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs", log_level)
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, # Tamanho em bytes do arquivo de log
    backupCount=10, # Quantidade de arquivos de backup que queremos manter
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

# Tipos de log
# log.debug("Msg pro dev, QE, sysadmin")

# log.info("Msg geral para usuários")

# log.warning("Aviso que não causa erro")

# log.error("Erro que afeta uma unica execução")

# log.critical("Error geral ex: Banco de dados sumiu")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error(str(e))