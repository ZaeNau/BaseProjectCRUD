import logging

# Konfigurasi logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log_activity(action, details):
        log_message = f"{action}: {details}"
        logging.info(log_message)
