# The404Hacking
# Digital Security ReSearch Group
# Telegram: @The404Hacking
# PubIP Coded By Sir.4m1R
# The404Hacking.BlogSky.Com
# The404Hacking.Team@Gmail.Com

import urllib

print ("-----------------------------------------")
print ("|     PubIP | Get Public IP Address     |")
print ("|             The404Hacking             |")
print ("|    Digital Security ReSearch Group    |")
print ("|       Telegram: @The404Hacking        |")
print ("|            Coder: Sir.4m1R            |")
print ("-----------------------------------------")
print ("")
print ("    Connecting ...")
try:
	data = urllib.urlopen("https://api.ipify.org/")
	ip = data.read()
	print ("    Your Public IP is: "+str(ip))
	print ("")
	print ("To Exit, Press the [Enter] Button")
	raw_input()
except:
	print ("    Check Your Connection !")
	print ("")
	print ("To Exit, Press the [Enter] Button")
	raw_input()
	exit()
