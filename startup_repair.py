import os
import sys
from os import listdir

from os.path import isfile, join
mypath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aiml/pandora')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

## @Once stratup is written thi s method is invoked
## @to find brain cache and finally delete it
def searchBrainFile(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return os.path.join(root, name)

# Model training on Demand && Deleted brain cache
"""sample path => os.path.dirname(__file__)/AIML/standard:*"""
# loads all AIML xml files from directory(/AIML/standard)\
command = input("Retrain AIML model now ?")
if(command == "yes"):
	print(searchBrainFile("bot_brain.brn", "D:\AI"))
	print("\r\n")
	print(os.path.dirname(os.path.abspath(__file__)))
	sys.exit();
else:
	print("Using existing brain file..")
	sys.exit();

# filtering ML files now
print("\r\n === writing files ===\r\n ")
print("Command : (load all model)")
"""
    @ Script to dynamically add train model(AIML) to the memory
    @ Run on demand with command - train model
    @ Training type : Recursively throughout the AIML directory
"""
bsx = '<aiml version="1.0"> \r\n ';
bsx += '<category>\r\n '
bsx += '   <pattern>LOAD AIML B</pattern> \r\n '
bsx += '   <template> \r\n '
xmls = ""
try:
    startupconfig = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aiml/std-startup.xml'), 'w',encoding = 'utf-8')
    startupconfig.write(bsx)
    index = 0
    dls = ""
    for fl in onlyfiles:  
        dls += '<learn>aiml/standard/'+fl+'</learn> \r\n '
        pass
    startupconfig.write(dls)
    xmls += '</template> \r\n'
    xmls += '</category> \r\n '
    xmls += '</aiml>'
    startupconfig.write(dls)
    startupconfig.write(xmls)
except:
    print("Error writing file....")
finally:
    startupconfig.close
    print("# File writing successful \r\n # All new and existing models are formated \r\n # and added to bot_brain.brn file as well'")