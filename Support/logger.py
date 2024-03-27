import logging
from logging import Logger
from logging import FileHandler
from logging import Formatter

logger: Logger = logging.getLogger(__name__)
handler: FileHandler = logging.FileHandler('./support/test_automation.log')
formatter: Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
