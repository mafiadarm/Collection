# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_02_2018  12:13
   File Name:      /GitHub/progressListen
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging
from time import sleep
from tqdm import tqdm

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


for i in tqdm(range(1000)):
    sleep(0.01)