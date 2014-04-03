try:
	from setuptools import setup
except:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author' 	 : 'Joe Oliver',
	'url' 		 : 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'joey_oliver@hotmail.com',
	'version'	 : '0.1',
	'install_requires': ['nose'],
	'packages'	: ['NAME'],
	'scripts'	: [],
	'name 		: projectname;'
}

setup(**config)