import logging

import fire

from bhds.cli import Bhds

logging.basicConfig(format='%(asctime)s (%(levelname)s) - %(message)s', level=logging.INFO, datefmt='%Y%m%d %H:%M:%S')


class Task:

    def __init__(self):
        self.bhds = Bhds()


if __name__ == '__main__':
    fire.Fire(Task)
