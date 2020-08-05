import logging
import constants

#function providing logger with basic configuration


def getLogger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - [%(name)s] - [%(levelname)s] - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    return logging
