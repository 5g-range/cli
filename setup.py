from setuptools import setup

setup (
	name='cli_5g',
	version='0.01',
	py_modules=['cli_5g'],
	install_requires=['Click',],
	entry_points='''
	[console_scripts]
	cli_5g=cli_5g:cli
	
	'''
	)