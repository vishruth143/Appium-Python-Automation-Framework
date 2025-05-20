# pylint: disable=[line-too-long, missing-module-docstring, useless-object-inheritance, too-many-instance-attributes]
# pylint: disable=[too-many-arguments, self-assigning-variable, too-few-public-methods, import-error]
# pylint: disable=[too-many-positional-arguments]


import datetime
import logging
import logging.handlers
import os
import sys
from datetime import timezone
import colorlog

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(ROOT_PATH, "logs")

sys.path.append(LOG_PATH)


class Logger(object):
    """
    Logger class for logging events from each action
    """

    def __init__(self, logger=None, date_tag=None,
                 filehandler=None, consolehandler=None,
                 file_id=None, formatter=None):
        """
        constructor for all the default params for the logger
        :param logger: logger object
        :param date_tag: date time stamp
        :param filehandler: To write to a file
        :param consolehandler: To display logs in console
        :param file_id: file name prefix
        :param formatter: format of logs
        """

        if date_tag is None:
            date_tag = datetime.datetime.now(tz=timezone.utc).strftime("%Y-%m-%d-%H-%M")

        if file_id is None:
            file_id = file_id

        if logger is None:
            logger = logging.getLogger(file_id)

        if formatter is None:
            formatter = logging.Formatter(fmt='%(asctime)-1s\
            %(levelname)-1s %(name)s:%(funcName)s:%(lineno)-1s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Create a rotating log file handler that will rotate the log file when it reaches 10MB in size, and will keep
        # up to 5 backup log files
        if filehandler is None:
            if not os.path.exists(LOG_PATH):
                os.makedirs(LOG_PATH)
            filehandler = logging.handlers.RotatingFileHandler(os.path.join(LOG_PATH, 'test_execution.log'),
                                                               maxBytes=10*1024*1024, backupCount=5,
                                                               delay=False, encoding=None, errors=None)
            filehandler.setFormatter(formatter)

        if consolehandler is None:
            consolehandler = colorlog.StreamHandler(sys.stdout)
            consolehandler.setFormatter(colorlog.ColoredFormatter(
                fmt='%(log_color)s%(asctime)-s\
                %(levelname)-s %(name)s:%(funcName)s:%(lineno)-s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        logger.setLevel(logging.DEBUG)

        self.logger = logger
        self.date_tag = date_tag
        self.filehandler = filehandler
        self.consolehandler = consolehandler
        self.file_id = file_id
        self.info = logger.info
        self.error = logger.error
        self.debug = logger.debug
        self.exception = logger.exception
