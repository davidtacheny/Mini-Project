import subprocess
import time
import json
import sys
import re

#I was not able to find a way to use capabilities in Boto so I ran a command
cmd='aws cloudformation create-stack --stack-name cfdtacheny --template-body https://raw.githubusercontent.com/davidtacheny/Mini-Project/master/cf_mini-project.yml --capabilities CAPABILITY_IAM'
cf=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)

# Wait for 120 seconds
print("your cloudformation stack is running waiting 2 min")
time.sleep(120)

json_string = subprocess.check_output("aws cloudformation describe-stacks --stack-name cfdtacheny", shell=True)
urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', json_string)
api = ''.join(urls)
test = subprocess.check_output("curl --request POST '%s'/call" % api, shell=True)
print test
print ("your api url is '%s'/call" % api)
