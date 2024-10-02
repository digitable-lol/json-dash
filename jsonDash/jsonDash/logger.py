import logging
import os


format = "%(asctime)s %(levelname)s: %(message)s"


def setupLoggerConfig(fileName):
    logging.basicConfig(
        level=logging.INFO,
        format=format,
        handlers=[
            logging.FileHandler(os.getenv("LOG_FILE_PATH") + fileName),
            logging.StreamHandler(),
        ],
    )


def setupLogger():
    setupLoggerConfig("info.log")