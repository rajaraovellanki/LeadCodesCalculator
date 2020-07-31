import logging

#function providing logger with basic configuration
def getLogger():
    logging.basicConfig(level=logging.DEBUG, filename='.//logs//app.log', filemode='w', format='%(asctime)s - [%(name)s] - [%(levelname)s] - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    return logging