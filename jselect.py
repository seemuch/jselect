#!/usr/bin/env python
import sys
import json

result = []

def handle_dict_json(json_obj, element_list):
	global result
	if element_list[0] not in json_obj:
		return

	if len(element_list) == 1:
		result.append(json_obj[element_list[0]])

	else:
		handle_json(json_obj[element_list[0]], element_list[1:])


def handle_list_json(json_obj, element_list):
	global result
	for one_obj in json_obj:
		handle_json(one_obj, element_list)


def handle_json(json_obj, element_list):
	global result
	if type(json_obj) is dict:
		handle_dict_json(json_obj, element_list)
	elif type(json_obj) is list:
		handle_list_json(json_obj, element_list)
	else:
		print 'Unhandled type'
		return

	return

def usage():
	print '''
	Two usages:
	1. jselect file_name wanted_elements
		e.g. jselect student.json department.major
	2. some_input | jselect wanted_elements
		e.g. cat student.json | jselect department.major
	'''

if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.exit(0)

	elif len(sys.argv) == 2:
		element_list = sys.argv[1].split('.')
		input_str = sys.stdin.read()

	elif len(sys.argv) == 3:
		try:
			file_obj = open(sys.argv[1])
		except IOError as e:
			print 'Failed to open the file "' + sys.argv[1] + '"'
			sys.exit(2)
		element_list = sys.argv[2].split('.')
		input_str = file_obj.read()

	else:
		usage()
		sys.exit(1)

	json_obj = json.loads(input_str)
	handle_json(json_obj, element_list)

	for one_result in result:
		print one_result
