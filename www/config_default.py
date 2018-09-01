#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '140.143.250.99',
        'port': 3306,
        'user': 'root',
        'password': 'lxgmysql',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
