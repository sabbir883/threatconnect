# -*- coding: utf-8 -*-

""" standard """
import json
import ConfigParser
import sys
from datetime import datetime

""" custom """

from threatconnect import *
from threatconnect.RequestObject import RequestObject


# define global variables 

# Add owners . See examples below 
owners = ['Example Community']
# Here are some of the examples 
# owners = ['Acme Corp']
# owners = ['EmergingThreats IP Rep', 'Blocklist.de Source', 'ZeuS Tracker Source', 'MalwareDomainList Source']

# bulk Json report will stored ins this direcoty. Customer may change it here. 
directoryPath = "c:\Report_Threat_Connect\Bulk_report_"




# main function 

def main():

    # configuration file . Needs to be on same folder as this .py file. Or path needs to be defined. 
    config_file = "tc.conf"

    # retrieve configuration file
    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    try:
        api_access_id = config.get('threatconnect', 'api_access_id')
        api_secret_key = config.get('threatconnect', 'api_secret_key')
        api_default_org = config.get('threatconnect', 'api_default_org')
        api_base_url = config.get('threatconnect', 'api_base_url')
        api_result_limit = int(config.get('threatconnect', 'api_result_limit'))
    except ConfigParser.NoOptionError:
        print('Could not retrieve configuration file.')
        sys.exit(1)

    # create an instance of threatconnect object and pass required paramerters to the constructor function. 
    
    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # Set max api result limit
    tc.set_api_result_limit(api_result_limit)

    # set threat connect log (tcl) level
    tc.set_tcl_file('log/tc.log', 'debug')
    tc.set_tcl_console_level('critical')

    # build bulk INDICATORS request object
     
    ro = RequestObject()
    ro.set_http_method('GET')
    ro.set_owner(owners)
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(True)
    ro.set_request_uri('/v2/indicators/bulk')

    #
    # store api response to results variable 
    #
    try:
        results = tc.api_request(ro)
        
    except RuntimeError as e:
            print(e)
            sys.exit(1)

    if results.headers['content-type'] == 'application/json':
        data = results.json()
        time=datetime.now()
        jsonFile = open(directory_path+time.year+time.month+time.day+time.hour+time.minute, "w+" )
        jsonFile.write(data)

    # This is for debug purposes 
    #print(json.dumps(data, indent=4))    


if __name__ == "__main__":
    main()

