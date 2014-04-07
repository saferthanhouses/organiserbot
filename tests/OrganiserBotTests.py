import unittest
from OrganiserBot import organiser_bot
import os
import sys

class DirPathTest(unittest.TestCase):

	def test(self):
		dir_path=organiser_bot.dir_path()
		self.assertEqual(dir_path==os.path.realpath(organiser_bot.__file__))


# Check that check_setup does create files
# doesn't create files
# Edge Cases?

class ExtractFTypeTest(unittest.TestCase):

	def test_goodinput(self):
		res = OrganiserBot.extract_ftype('lions.jpg')
		self.assertEqual(res, '.jpg')

	def test_dblftype(self):
		res = OrganiserBot.extract_ftype('lions.tar.gz')
		self.assertEqual(res, '.tar.gz')

	def test_randm(self):
		for n in ['!^$&£(*&$txt']

	def test_noftype(self):
		pass

	def test_hiddenf(self):
		pass

class FindDestTest(unittest.TestCase):

	instr == {'Pictures': ['.jpg','.gif'], 'Documents': ['.pdf', '.txt']}

	def test_goodin(self):
		pass

	def test_unkninp(self):
		'''test well-formed input not in instructions'''
		pass




if __name__=='__main__':
	unittest.main()