# app_logger.py
import logging

_log_format = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"

def get_file_handler(logfilename):
    file_handler = logging.FileHandler(logfilename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler

def get_logger(name,logfilename):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler(logfilename))
    logger.addHandler(get_stream_handler())
    return logger
  