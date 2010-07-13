#!/usr/bin/env python
# encoding: utf-8

""" Tabbed CLI Inteface Application
"""

import io
import sys

from helpers import *
import tabbed.core

from packages import opster


FORMATS = ('json', 'yaml', 'xls', 'csv', 'html')

opts = []

opts.append(('v', 'version', False, 'Report tabbed version'))

for format in FORMATS:
	opts.append(('', format, False, 'Output to %s' % (format.upper())))



@opster.command(options=opts, usage='[FILE] [--FORMAT | FILE]')
def start(in_file=None, out_file=None, **opts):
	"""Covertly convert dataset formats"""
	
	opts = Object(**opts)
	
	if opts.version:
		print('Tabbed, Ver. %s' % tabbed.core.__version__)
		exit(0)
	
	stdin = piped()
	
	if stdin:
		print stdin
	
	elif in_file:
		
		try:
			in_file = io.open(in_file, 'r')
		except Exception, e:
			print(' %s cannot be read.' % in_file)
			exit(65)
		
		file_ext = in_file.name.split('.')[-1]
		
		if file_ext.lower() in FORMATS:
			setattr(opts, file_ext, True)
		else:
			print('Import format not supported.')
			exit(65)
	else:
		print('Please provide input.')
		exit(65)
		

	
	_formats_sum = sum(opts[f] for f in FORMATS)
	
	# Multiple output formats given
	if _formats_sum > 1:
		print('Please specify a single output format.')
		exit(64)
		
	# No output formats given
	elif _formats_sum < 1:
		print('Please specify an output format.')
		exit(64)
	
	
	# fetch options.formats list
	# if sum(()) > 1
	# log only one data format please
	# if sum of formats == 0, specity format
	
	# look for filename
	
	print opts.__dict__
	print in_file
	print out_file