#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python_web
    @Date: 8/30/2018 11:56 PM
    @Author: xuegangliu
    @Description: config_default
"""

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}