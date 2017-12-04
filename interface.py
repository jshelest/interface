#! /usr/bin/python

#import python modules
import os
import ssl
import requests
import csv
import re
from time import gmtime, strftime
 
#Force SSL to TLS
ssl.PROTOCOL_SSLv23=ssl.PROTOCOL_TLSv1

#Pull QoS from PA API, stores XML output into variable
#- Modify as Needed - Replace PA1_FIREWALL, Replace interface ethernet with yours, Replace key=XXXXXXX,
r_stats_PA1 = requests.get('https://192.168.55.11/api/?&type=op&cmd=%3Cshow%3E%3Cqos%3E%3Cinterface%3Eethernet1%2F1%3C%2Finterface%3E%3Cthroughput%3E0%3C%2Fthroughput%3E%3C%2Fqos%3E%3C%2Fshow%3E&key=LUFRPT14MW5xOEo1R09KVlBZNnpnemh0VHRBOWl6TGM9bXcwM3JHUGVhRlNiY0dCR0srNERUQT09&user=admin&password=admin', verify=False)
 
#saves API output to variable as string
r_string_PA1 = r_stats_PA1.text
 
#Modify as needed
#save_directory = './panstats/'
 
#parses out the XML from the output
r_string_PA1 = re.sub('<[^>]*>', '', r_string_PA1)

#records the time the data was pulled
response_time = strftime("%Y-%m-%d %H:%M:%S")

#stats = re.search(r'(?:class 4:.*)', response_stats_PA1)
stats = r_string_PA1.split(":")
for item in stats:
    item = item.encode('ascii')
print item

#adds the time to the QoS output
response_stats_PA1 = response_time + ',' + item + '\n'

#creates a csv file in your save directory
if response_stats_PA1:
	#qos_stats_file = save_directory + 'qos_stats_PA1.csv'
	qos_stats_file = 'qos_stats_PA1.csv'
with open(qos_stats_file, 'a') as myFile:
	myFile.write(response_stats_PA1)
#myFile.flush()
#os.fsync(myFile.fileno())
myFile.close()

