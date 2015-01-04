#coding=utf8
import socket
import random
import os

network = 'irc.oulu.fi'
port = 6667
channels = ["#kooderit"]

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK zazenbot\r\n' )
irc.send ( 'USER zazenbot zazenbot skizzobot :Zazenbot!\r\n' )
for channel in channels:
	irc.send ( 'JOIN '+channel+'\r\n' )

while True:
	data = irc.recv ( 4096 )
	if (data != ""):
		print data
	if data.find ( 'PING' ) != -1:
		irc.send ( 'PONG' + data.split() [ 1 ] + '\r\n' )
	if data.find ( 'KICK' ) != -1:
		for channel in channels:
			irc.send ( 'JOIN '+channel+'\r\n' )

