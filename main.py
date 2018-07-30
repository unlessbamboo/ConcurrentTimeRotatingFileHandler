# coding:utf8
from __future__ import print_function

import time
import signal
import logging
import random
from datetime import datetime
from multiprocessing import Pool

from config import LOGGING
from concurrent_time_rotating import clogDictConfig


# Initialize
clogDictConfig(LOGGING)
logger_info = logging.getLogger('info')


def write_log(pid, msg, second):
    handle_signal()
    try:
        for i in xrange(20):
            print('-----------------:', i)
            logger_info.info('Time:{}, Pid:{}, Number:{}, Msg:{}'.format(
                str(datetime.now()), pid, i, msg))
            time.sleep(second)
    except KeyboardInterrupt:
        print('Pid:{}, Caught KeyboardInterrupt'.format(pid))


def handle_signal():
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)


def run(msg='This is a test for multiprocessing', minsecond=0.5, maxsecond=1):
    msg = '------------------------------Test--------------------------------'
    pool = Pool()
    for pid in xrange(5):
        sleep_second = random.uniform(minsecond, maxsecond)
        pool.apply_async(write_log, (pid, msg, sleep_second))
    pool.close()
    pool.join()
    print('Sub-process(es) done')


if __name__ == '__main__':
    logger_info.info('----Start Testing ConcurrentTimeRotatingFileHandler----')
    logger_info.info('----Ready Test logger at multiple process----')
    run()
