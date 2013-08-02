#!/usr/bin/env python
# Copyright (c) 2013, Scott Cagno
# All rights reserved.
# BSD LICENSED (can be found in LICENSE file)

scope = {
	
	'name'				:	'editor',
	'id'				: 	1,
	'type'				: 	'base',
	'active'			:	False,
	'actions'			:	{

		# MODES
		"ESCAPE"			:	[ ('key', "Escape") ],
		"INSERT"			:	[ ('key', "i") ],
		"SELECT"			:	[ ('key', "Escape"), ('key', "v") ],
		
		# COMMAND MODE -- NAVIGATION
		"LEFT"				:	[ ('type', "h") ],
		"DOWN"				:	[ ('type', "j") ],
		"UP"				:	[ ('type', "k") ],
		"RIGHT"				:	[ ('type', "l") ],
		"LINE"				:	[ ('type', ":") ],
		
		# COMMAND MODE -- DOCUMENT
		"EXECUTE"			:	[ ('type', ":! ") ],
		"SAVE"				:	[ ('type', ":w!"), ('key', "Return") ],
		"CLOSE"				:	[ ('type', ":bw!"), ('key', "Return") ],
		"EDIT"				:	[ ('type', ":e ") ],
		"UNDO"				:	[ ('type', "u") ],
		"REDO"				:	[ ('type', ":redo"), ('key', "Return") ],
		"UNDO-LINE"			: 	[ ('type', "U") ],
		"CUT"				:	[ ('type', "d") ],
		"COPY"				:	[ ('type', "y") ],
		"PASTE"				:	[ ('type', "p") ],
		"DELETE"			:	[ ('type', "d") ],
		"DELETE-LINE"		:	[ ('type', "dd") ],
		"WORD"				:	[ ('type', "w") ],
		"TOP"				:	[ ('type', "H") ],	
		"BOTTOM"			:	[ ('type', "L") ],
		"BEGINNING"			:	[ ('type', "b") ],
		"END"				:	[ ('type', "e") ],
		"BEGINNING-OF-LINE"	:	[ ('type', "^") ],
		"END-OF-LINE"		:	[ ('type', "$") ],
		"AGAIN"				:	[ ('type', ".") ],
		"FIND"				:	[ ('type', "?") ],
		"NEXT"				:	[ ('type', "n") ],
		"PREVIOUS"			:	[ ('key', "shift+n") ],
		"REPLACE"			:	[ ('type', ":s//"), ('key', "Left") ],
		"REPLACE-ALL"		:	[ ('type', ":%s//"), ('key', "Left") ],
		"BACKSPACE"			:	[ ('key', 'Delete') ],

		# COMMAND MODE -- MACROS
		"START-MACRO"		:	[ ('type', "qq") ],
		"STOP-MACRO"		:	[ ('type', "q") ],
		"RUN-MACRO"			:	[ ('type', "@q") ],

		# COMMAND MODE -- PLUGINS
		"BUNDLE-INSTALL"	:	[ ('type', ":BundleInstall"), ('key', "Return") ],
		"SEARCH"			:	[ ('type', "s") ],
		"INSTALL"			:	[ ('type', "i") ],
		"CLEAN"				:	[ ('type', "cY") ],

		# SELECT MODE -- SELECTIONS
		"INNER"				:	[ ('type', "i") ],
		"A"					:	[ ('type', "a") ],
		"CHANGE"			:	[ ('type', "c") ],	
		"TAG"				:	[ ('type', "t") ],
		"DE-SELECT"			:	[ ('key', "Escape") ],
		"TOGGLE-CASE"		:	[ ('type', "~") ]
	}

}