#!/usr/bin/env python

"""Tests for Howdoi."""
# https://github.com/gleitz/howdoi/blob/master/test_howdoi.py
import os 
import re 
import time  
import unittest 

from howdoi import howdoi
from pyquery import PyQuery as pq 

class HowdoiTestCase(unittest.TestCase):
    # define a helper function here which other tests can use 
    def call_howdoi(self, query):
        parser = howodi.get_parser()
        args = vars(parser.parse_args(query.split(' ')))
        return howdoi.howdoi(args)
    
    def setUp(self):
        self.queries = ['format date bash',
                        'print stack trace python',
                        'convert mp4 to animated gif',
                        'create tar archive',
                        'cat']
        self.pt_queries = ['abrir arquivo em python',
                           'enviar email em django',
                           'hello world em c']
        self.bad_queries = ['moe',
                            'mel']
    
    def tearDown(self):
        time.sleep(2)
    
    def test_get_link_at_pos(self):
        self.assertEqual(howdoi.get_link_at_pos(['/questions/42/'],1),
    
    