# -*- coding: utf-8 -*-

'''
Created on 2013年10月29日

@author: gjwang
'''
#region's name for short for nodeID
nodeID = 'jx_ja'
#post interval
interval = 10
#mountpoint for main disk
mountpoint = '/data'
device = None #device='/dev/sda9'
netcard = 'eth0'
#port for video stream
video_server_port='8080'
#port for getting xml file from nginx 
xmlfile_port = '80'
#nginx 的对于获取nginx连接数的配置路径
nginx_status = '/nginx_status'
#获取nginx配置路径的端口
nginx_status_port='8089'
#the host's url for posting xml string
postUrl = 'http://xxx:port/lua'
#local xml file's path
wwwroot = '/data/ysten'
#xml file for posting
xmlfilename="NodeState.xml"
#program's log
logfilename = "log/nodestate.log"
#所有主机整体配置的综合系数
weight=1
#网卡最大带宽
bandwidth_max=1024*1024*1024/8
#主机最多可以承载多少用户数
conn_max=1000
