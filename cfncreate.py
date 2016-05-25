import os
import sys
import getopt
import commands
import time
import boto
import boto.ec2
import boto.cloudformation

cfconn = boto.ec2.connect_to_region("us-west-2", aws_access_key_id='aws_access_key_id',aws_secret_access_key='aws_secret_access_key')
s3template = "https://"
cfoutput = cfnconn.create_stack(stackname,template_url=s3template)
print "stack created completed \n"
