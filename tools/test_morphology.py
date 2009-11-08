#!/usr/bin/python3.0
"""
A very slow script that tests the morphology that deals selbri for zirsam.
If it properly parses a selbri, it should output selbri(WORD).
It caches the last error so that you don't have to run through everything again to check it again.

Instead of running this script (which is very slow), you can do:
	cat data/lujvo data/fuhivla | ./morphology.py | grep CMAVO 
If it prints anything, than there was a problem. This catches obvious errors, and is many orders of magnitude faster. But this one is nicer if you're making changes.
"""

print("This program tests lujvo individually, which takes a while. You can run, instead:")
print("cat data/lujvo data/fuhivla | ./morphology.py | grep CMAVO")
print("That command only takes a few seconds on my computer, while this takes several minutes")

import os
import sys

err = os.path.expanduser('~/.zirsam_selbri_test_error')

def test(line, form='SELBRI'):
	line = line.strip()
	assert ' ' not in line
	assert '(' not in line
	assert '#' not in line
	assert '[' not in line
	t = "%s(%s)" % (form, line)
	cmd = "echo %r | ./morphology.py" % line.strip()
	output = os.popen(cmd).read().strip()
	if output != t:
		print("!!!Error with", line.strip(), ':')
		os.system("echo %r | jbofihe -x" % line)
		print("Got", output, "expected", t, ".")
		os.system(cmd + ' --token-error')
		open(err, 'w').write(line.strip())
		return False
	return True
		

def test_all(filename):
	for line in open(filename):
		line = line.strip()
		print("\r", line, end=' '*40, sep='')
		if line[0] == '#':
			print(" (ignored) ", end='')
		elif not test(line):
			return False
	return True
	

def test_old():
	try:
		first = open(err).read().strip()
	except:
		print("Nothing cached.")
		return True

	if first:
		if test(first):
			open(err, 'w').close()
		else:
			return False
	return True
	

def run_test():
	if test_old():
		if test_all('data/lujvo') and test_all('data/fuhivla'):
			print("\nHooray! :D")
			os.system("beep")
			raise SystemExit
	else:
		return False

if __name__ == '__main__':
	if 'old' in sys.argv:
		test_old()
	elif 'loop' in sys.argv:
		while 1:
			run_test()
			i = True
			while i:
				i = input().strip()
				if i:
					if test(i):
						print("Passed.")
			print("=====================================")
	else:
		run_test()
