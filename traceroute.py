import os, sys
import numpy as np

while True:
	s = input().split()[1]
	command = "ping -c 1 " + s
	ex = os.popen(command)
	dest = ex.read().split('\n')[0].split()[2][1:-2]
	print ("traceroute to " + s + " (" + dest + ")" + ", 30 hops maximum:")
	ttl = 1
	com = "ping -c 1 -m "
	flag = 0
	while True:
		mss = []
		ip_addr = []
		cmd = com + str(ttl) + " -t 2 " + s
		# print (cmd)								#debug
		ex1 = os.popen(cmd, 'r')
		ping_res1 = ex1.read().split('\n')
		ex1.close()
		# print (ping_res1[1])					#debug
		if ping_res1[1] == '':
			mss.append('*')
			# print (mss[0])						#debug
			ip_addr.append('_')
		elif ping_res1[1].split()[-1] == 'exceeded':
			ip = ping_res1[1].split()[3][0:-1]
			ip_addr.append(ip)
			# print (ip_addr[0])					#debug
			# print ((com[0:10] + '-t 5 ' + ip_addr[0]))		#debug
			dummy1 = os.popen((com[0:10] + '-t 2 ' + ip_addr[0]), 'r')
			dum1 = dummy1.read().split('\n')[1]
			# print (dum1)#debug
			if dum1 == '':
				mss.append('*')
			elif dum1.split()[-1] != "ms":
				mss.append('*')
			else:
				mss.append(dum1.split('=')[-1])
			# print (mss[0])						#debug
			dummy1.close()
		else:
			ip_addr.append(ping_res1[1].split()[3][:-1])
			mss.append(ping_res1[5].split()[3].split('/')[0] + " ms")
			flag = 1
			# print (ip_addr[0])
			# print (mss[0])
		ex2 = os.popen(cmd, 'r')
		ping_res2 = ex2.read().split('\n')
		ex2.close()
		# print (ping_res2[1])					#debug
		if ping_res2[1] == '':
			mss.append('*')
			# print (mss[1])						#debug
			ip_addr.append('_')
		elif ping_res2[1].split()[-1] == 'exceeded':
			ip = ping_res2[1].split()[3][0:-1]
			ip_addr.append(ip)
			# print (ip_addr[1])					#debug
			# print ((com[0:10] + '-t 5 ' + ip_addr[1]))		#debug
			dummy2 = os.popen((com[0:10] + '-t 2 ' + ip_addr[1]), 'r')
			dum2 = dummy2.read().split('\n')[1]
			# print (dum2)#debug
			if dum2 == '':
				mss.append('*')
			elif dum2.split()[-1] != "ms":
				mss.append('*')
			else:
				mss.append(dum2.split('=')[-1])
			# print (mss[1])						#debug
			dummy2.close()
		else:
			ip_addr.append(ping_res2[1].split()[3][:-1])
			mss.append(ping_res2[5].split()[3].split('/')[0] + " ms")
			flag = 1
			# print (ip_addr[1])
			# print (mss[1])
		ex3 = os.popen(cmd, 'r')
		ping_res3 = ex3.read().split('\n')
		ex3.close()
		# print (ping_res3[1])					#debug
		if ping_res3[1] == '':
			mss.append('*')
			# print (mss[2])						#debug
			ip_addr.append('_')
		elif ping_res3[1].split()[-1] == 'exceeded':
			ip = ping_res3[1].split()[3][0:-1]
			ip_addr.append(ip)
			# print (ip_addr[2])					#debug
			# print ((com[0:10] + '-t 5 ' + ip_addr[2]))		#debug
			dummy3 = os.popen((com[0:10] + '-t 2 ' + ip_addr[2]), 'r')
			dum3 = dummy3.read().split('\n')[1]
			# print (dum3)#debug
			if dum3 == '':
				mss.append('*')
			elif dum3.split()[-1] != "ms":
				mss.append('*')
			else:
				mss.append(dum3.split('=')[-1])
			# print (mss[2])						#debug
			dummy3.close()
		else:
			ip_addr.append(ping_res3[1].split()[3][:-1])
			mss.append(ping_res3[5].split()[3].split('/')[0] + " ms")
			flag = 1
			# print (ip_addr[2])
			# print (mss[2])
		trace_out = str(ttl) + '  '
		if ip_addr[0] != '_':
			trace_out = trace_out + ip_addr[0] + " " + mss[0]
		else:
			trace_out += mss[0]
		if ip_addr[1] == ip_addr[0]:
			trace_out = trace_out + " " + mss[1]
		else:
			if ip_addr[1] == '_':
				trace_out = trace_out + " " + mss[1]
			else:
				trace_out = trace_out + " " + ip_addr[1] + " " + mss[1]
		if ip_addr[2] == ip_addr[1]:
			trace_out = trace_out + " " + mss[2]
		else:
			if ip_addr[2] == '_':
				trace_out = trace_out + " " + mss[2]
			else:
				trace_out = trace_out + " " + ip_addr[2] + " " + mss[2]
		print (trace_out)
		if flag == 1 :
			break
		if ttl == 30:
			break
		ttl += 1