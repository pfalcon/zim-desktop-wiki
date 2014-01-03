# -*- coding: utf-8 -*-

# Copyright 2013 Jaap Karssenberg <jaap.karssenberg@gmail.com>


from __future__ import with_statement

import tests

from zim.signals import *


class TestEmitter(tests.TestCase):

	def runTest(self):

		# Test hook
		emitter = Emitter()
		self.assertIsNone(emitter.emit('foo', 'x'))

		emitter.connect('foo', lambda o, a: a * 3)
		emitter.connect('foo', lambda o, a: a * 5)
		self.assertEqual(emitter.emit('foo', 'x'), 'xxx')
			# pick first result


# TODO test Connector, DelayedCallback

class Emitter(SignalEmitter):

	__hooks__ = ('foo')



class TestSignalHandler(tests.TestCase):

	def runTest(self):
		obj = ClassWithHandler()
		self.assertEqual(obj.count, 0)
		self.assertEqual(id(obj.add_one), id(obj.add_one)) # unique instance object

		obj.add_one()
		self.assertEqual(obj.count, 1)

		with obj.add_one.blocked():
			obj.add_one()
			obj.add_one()
			obj.add_one()
		self.assertEqual(obj.count, 1)

		obj.add_one()
		obj.add_one()
		obj.add_one()
		self.assertEqual(obj.count, 4)


class ClassWithHandler(object):

	def __init__(self):
		self.count = 0

	@SignalHandler
	def add_one(self):
		self.count += 1
