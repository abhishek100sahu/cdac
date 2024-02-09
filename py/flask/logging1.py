import logging
import os
from datetime import datetime as dt
log_folder = './logs'

os.makedirs(log_folder, exist_ok=True)

logfilename = os.path.join(log_folder, dt.now().strftime('%Y-%m-%d_%H_%M_%S)'+ str("_HES.log")))

logging.basicConfig(
    level=logging.INFO,
    filename=logfilename,
    format="%(asctime)s %(funcName)s %(levelname)-s %(message)s %(filename)s",
    filemode="w",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("debug logging")
logging.info("info logging")
logging.warning("warnings logging")
logging.error("error logging")
logging.critical("critical")

