#!/usr/bin/env python
# Copyright (c) 2013, Scott Cagno
# All rights reserved.
# BSD LICENSED (can be found in LICENSE file)

# imports
import subprocess, pynotify, gst, gobject, sys, signal, datetime, inspect
# local imports
import config

# update corpus
def update_corpus(scopes, extras):
	with open('vocab.corpus', 'w') as fd:
		for phrase in extras: 
			fd.write(phrase + '\n')
		for scope in scopes:
			fd.write(scope['name'].upper() + '\n')
			for phrase in scope['actions']:
				fd.write(phrase + '\n')
	subprocess.check_call('bash tools/corpus_updater.sh', shell=True)

# load scopes
def load_scopes():
	for module in config.__all__:
		__import__('config.' + module)
		scopes = []
		for name, scope in config.__dict__.items():
			if inspect.ismodule(scope) and name in config.__all__:
				scopes.append(scope.scope)
	return scopes

# notification engine class
class Notify(object):

	# constructor
	def __init__(self):
		pynotify.init('notify')
		self.notify = pynotify.Notification('','')

	# display or update notification
	def show(self, title, body):
		self.notify.update(str(title), str(body))
		self.notify.show()

# speech engine
class Speech(gobject.GObject):
	
	# setup
	__gsignals__ = {
		'finished' : (
			gobject.SIGNAL_RUN_LAST, 
			gobject.TYPE_NONE, 
			(gobject.TYPE_STRING,)
		)
	}
	
	# constructor
	def __init__(self, models):
		gobject.GObject.__init__(self)
		pipe = [
			'autoaudiosrc',
			'audioconvert',
			'audioresample',
			'vader name=vad',
			'pocketsphinx name=asr',
			'appsink sync=false'
		]
		
		# assemble audio pipeline
		self.pipeline = gst.parse_launch(' ! '.join(pipe))
		
		# audio speech recognition, aka pocketsphinx libs
		asr = self.pipeline.get_by_name('asr')
		asr.connect('result', self.result)
		asr.set_property('lm', models + '/lm')
		asr.set_property('dict', models + '/dic')
		asr.set_property('configured', True)
		
		# voice activity dector
		self.vad = self.pipeline.get_by_name('vad')
		self.vad.set_property('auto-threshold', True)
	
	# set state to listen
	def listen(self):
		self.pipeline.set_state(gst.STATE_PLAYING)
	
	# set state to pause
	def pause(self):
		self.vad.set_property('silent', True)
		self.pipeline.set_state(gst.STATE_PAUSED)
	
	# emit result
	def result(self, asr, hyp, uttid):
		self.emit('finished', hyp)

# parsing engine
class Parser(object):
	
	# constructor
	def __init__(self, notify, scopes, update):
		self.notify = notify
		self.scopes = scopes
		if update: 
			update_corpus(self.scopes, ['ACTIVATE', 'DE-ACTIVATE', 'SHOW-ACTIVE', 'SHUTDOWN-VOX'])
		self.speech = Speech('models')
		self.speech.connect('finished', self.parse)

	# parse hypothesis and execute actions(s)
	def parse(self, stt, hyp):
		hyp = hyp.split(' ')
		if hyp[0] == 'SHUTDOWN-VOX':
			sys.exit()
		self.notify.show('Hypothesis', hyp)
		if len(hyp) >= 2 and hyp[0] in ['ACTIVATE', 'DE-ACTIVATE']:
			self.toggle(hyp)
		elif hyp[0] == 'SHOW-ACTIVE':
			self.active()
		else:
			for cmd in hyp:
				for scope in self.scopes:
					if cmd in scope['actions'] and scope['active']:
						self.execute(scope['actions'][cmd])

	# toggle scopes on or off
	def toggle(self, hyp):
			for scope in self.scopes:
				sn = scope['name'].upper()
				if hyp[1] == sn:
					if hyp[0] == 'ACTIVATE':
						scope['active'] = True
						self.notify.show('%s Activated' % (sn), 'Active = True')
					elif hyp[0] == 'DE-ACTIVATE':
						scope['active'] = False
						self.notify.show('%s De-Activated' % (sn), 'Active = False')

	# show active
	def active(self):
		active = []
		for scope in self.scopes:
			if scope['active']:
				active.append(scope['name'].upper())
		self.notify.show('Currently Active', active)

	# execute method
	def execute(self, actions):
		for k, v in actions:
			subprocess.call("xdotool %s --delay 3 '%s'" % (k, v), shell=True) 

# voccs class
class Voccs(object):
	
	# constructor
	def __init__(self, update=True):
		gobject.threads_init()
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.notify = Notify()
		self.parser = Parser(self.notify, load_scopes(), update)
		self.parser.speech.listen()
		self.notify.show('Voice v1.0a', 'Copyright 2013, Scott Cagno')
		loop = gobject.MainLoop()
		try:
			loop.run()
		except:
			loop.quit()
			sys.exit()

if __name__ == '__main__':
	Voccs()