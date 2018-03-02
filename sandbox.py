import logging
import colorlog

from common.logger import ConsoleLogger, Logger, StdOutLogger, Level


def main():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    )
    log = logging.getLogger('test1')

    formatter = colorlog.ColoredFormatter(
        (
            '%(asctime)s '
            '[%(log_color)s%(levelname)s%(reset)s] '
            '[%(cyan)s%(name)s%(reset)s] '
            '%(message_log_color)s%(message)s'
        ),
        reset=True,
        log_colors={
            'DEBUG': 'bold_cyan',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red,bg_white',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'white',
                'INFO': 'bold_white',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_red',
                'CRITICAL': 'bold_red',
            },
        },
        style='%'
    )

    log2 = logging.getLogger('test2')
    log2.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    log2.addHandler(handler)
    handler.setFormatter(formatter)

    loggers = list()
    loggers.append(ConsoleLogger(log))
    loggers.append(StdOutLogger(Level.INFO))
    loggers.append(ConsoleLogger(log2))
    logger = Logger(loggers)

    logger.debug('Deine Mudda')
    logger.info('DEIN VADDA')


if __name__ == '__main__':
    main()
