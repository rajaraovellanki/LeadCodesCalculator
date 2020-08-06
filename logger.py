"""This module provides the logger functionality"""
import logging

def get_logger():
    """function providing logger with basic configuration"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - [%(name)s] - [%(levelname)s] - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')
    return logging
