#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-09-25 21:11:15
@LastEditTime: 2019-12-31 15:51:08
'''

import socket
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor
from libs.brute import BruteBaseClass

class MongoDBBruteForce(BruteBaseClass):
    """MongoDBBruteForce"""

    def check_unauth(self,host,port):
        try:
            mongo = MongoClient(host=host,port=port,serverSelectionTimeoutMS=self.timeout)
            dblist = mongo.list_database_names()
        except Exception as e:
            hook_msg((False,host,port,"Anonymous",""))
            # print(str(e))
        else:
            hook_msg((True,host,port,"Anonymous",""))
            self.unauth_result.append(host)
        finally:
            mongo.close()

    def worker(self,hpup):
        host,port,user,pwd = hpup
        try:
            mongo = MongoClient(host=host,port=port,username=user,password=pwd,
                                authSource='admin',serverSelectionTimeoutMS=self.timeout)
            dblist = mongo.list_database_names()
        except Exception as e:
            hook_msg((False,host,port,user,pwd))
        else:
            hook_msg((True,host,port,user,pwd))
        finally:
            mongo.close()


bruter = MongoDBBruteForce

