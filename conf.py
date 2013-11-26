# -*- coding: utf-8 -*- 

'''
Created on 2013年10月29日

@author: gjwang
'''

nodeID = 'jx_ja'
interval = 5
mountpoint = '/data'
device = None #device='/dev/sda9'
netcard = 'eth0'
video_server_port='8080'
xmlfile_port= '8088'
psname = 'nginx'
postUrl = 'http://223.82.137.218:8088/lua'
#postUrl='http://61.233.192.135:8089/lua'
wwwroot = '/data/project/xmlfile'
xmlfilename="NodeState.xml"
logfilename = "log/nodestate.log"
weight=1
bandwidth_max=1024*1024*1024/8
conn_max=1000
