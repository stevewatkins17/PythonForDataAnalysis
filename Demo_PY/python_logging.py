import pytz
import datetime
import logging
import logging.handlers

log_file = 'IpythonNotebooks/Data/app.log'
logger = logging.getLogger(log_file)
logger.setLevel(logging.INFO)

log_format_file = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
handler_file = logging.handlers.RotatingFileHandler(log_file, maxBytes=1073741824, backupCount=1)
handler_file.setFormatter(log_format_file)
logger.addHandler(handler_file)

log_format_console = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler_console = logging.StreamHandler()
handler_console.setLevel(logging.INFO)
handler_console.setFormatter(log_format_console)
logger.addHandler(handler_console)

log = logging.getLogger('IpythonNotebooks/Data/app.log')

def main():
    timestamp_b = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))
    log.info(f"'begin session':'{str(timestamp_b)}'")

    timestamp_e = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))
    log.info(f"'end session':'{str(timestamp_e)}'")

if __name__ == "__main__":
    main()
