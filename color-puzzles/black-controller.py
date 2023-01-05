#!/usr/bin/env python

CONTROLLERS = [
	{
		'type': 'joycon',
		'color': 'orange',
		'side': 'rh',
		'rhbuttons': []
	},
	{
		'type': 'joycon',
		'color': 'purple',
		'side': 'lh',
		'lhbuttons': []
	},
	{
		'type': 'joycon',
		'color': 'gray',
		'side': 'rh',
		'rhbuttons': []
	},
	{
		'type': 'joycon',
		'color': 'red',
		'side': 'lh',
		'lhbuttons': []
	},
	{
		'type': 'joycon',
		'color': 'blue',
		'side': 'rh',
		'rhbuttons': []
	},
	{
		'type': 'pro',
		'color': 'black',
		'rhbuttons': [],
		'lhbuttons': []
	},
	{
		'type': 'pro',
		'color': 'white',
		'rhbuttons': [],
		'lhbuttons': []
	}
]

TARGET_SOLUTION = {
	'X': [True, True, False, False],
	'A': [True, False, True, True],
	'B': [False, False, True, True],
	'Y': [False, True, True, False],
	'U': [False, False, True, False],
	'R': [True, True, True, False],
	'D': [False, False, False, False],
	'L': [True, False, True, False]
}

def main():
	print('hello world')

if __name__ == '__main__':
	main()