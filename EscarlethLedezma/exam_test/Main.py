import logging
from EscarlethLedezma.exam_test.Register import Register


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('Applicatio.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
logger.debug('Create instance')
register=Register()
logger.debug('Registering employee')
register.register_employees()
logger.debug('Print Results')
register.print_table()
