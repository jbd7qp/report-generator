import logging
from typing import Any

def setup_logger(level: str = "INFO", logfile: str = "/app/logs/report.log"):
    numeric = getattr(logging, level.upper(), logging.INFO)
    logger = logging.getLogger("reportgen")
    logger.setLevel(numeric)
    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        logger.addHandler(sh)
        try:
            fh = logging.FileHandler(logfile)
            fh.setFormatter(fmt)
            logger.addHandler(fh)
        except Exception:
            logger.warning("Could not create file handler at %s", logfile)
    return logger
