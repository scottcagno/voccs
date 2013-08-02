#!/usr/bin/env python
# Copyright (c) 2013, Scott Cagno
# All rights reserved.
# BSD LICENSED (can be found in LICENSE file)

# imports
import uuid, time, datetime

scope = {
	
	'name'					:	'base',
	'id'					:	None,
	'type'					:	'default',
	'active'				:	True,
	'actions'				:	{

		# SWITCHING
		"SWITCH"			:	[ ('key', 'ctrl+a') ],

		# ALPHA
		"ALPHA" 			:	[ ('type', "a") ],
		"BRAVO" 			:	[ ('type', "b") ],
		"CHARLIE" 			:	[ ('type', "c") ],
		"DELTA" 			:	[ ('type', "d") ],
		"ECHO" 				:	[ ('type', "e") ],
		"FOXTROT" 			:	[ ('type', "f") ],
		"GOLF" 				:	[ ('type', "g") ],
		"HOTEL" 			:	[ ('type', "h") ],
		"INDIA" 			:	[ ('type', "i") ],
		"JULIE" 			:	[ ('type', "j") ],
		"KILO" 				:	[ ('type', "k") ],
		"LIMA" 				:	[ ('type', "l") ],
		"MIKE" 				:	[ ('type', "m") ],
		"NOVEMBER" 			:	[ ('type', "n") ],
		"OSCAR" 			:	[ ('type', "o") ],
		"PAPA" 				:	[ ('type', "p") ],
		"QUEBEC" 			:	[ ('type', "q") ],
		"ROMEO" 			:	[ ('type', "r") ],
		"SEE-ARRA" 			:	[ ('type', "s") ],
		"TANGO" 			:	[ ('type', "t") ],
		"UNIFORM" 			:	[ ('type', "u") ],
		"VICTOR" 			:	[ ('type', "v") ],
		"WHISKEY" 			:	[ ('type', "w") ],
		"X-ER" 				:	[ ('type', "x") ],
		"YANKEE" 			:	[ ('type', "y") ],
		"ZEN" 				:	[ ('type', "z") ],
		
		# DIGIT
		"ZERO" 				:	[ ('type', "0") ],
		"ONE" 				:	[ ('type', "1") ],
		"TWO" 				:	[ ('type', "2") ],
		"THREE" 			:	[ ('type', "3") ],
		"FOUR" 				:	[ ('type', "4") ],
		"FIVE" 				:	[ ('type', "5") ],
		"SIX" 				:	[ ('type', "6") ],
		"SEVEN" 			:	[ ('type', "7") ],
		"EIGHT" 			:	[ ('type', "8") ],
		"NINE" 				:	[ ('type', "9") ],
		
		# MATH(S)
		"PLUS"				:	[ ('type', "+") ],
		"MINUS"				:	[ ('type', "-") ],
		"DIVIDE"			:	[ ('type', "/") ],
		"MULTIPLY"			:	[ ('type', "*") ],
		"REMAINDER"			:	[ ('type', "%") ],
		"MOD-U-LUS"			:	[ ('type', "%") ],
		"MO-NAD"			:	[ ('type', "?") ],
		"EXPONENT"			:	[ ('type', "**") ],
		"PIE" 				:	[ ('type', "3.14") ],
		"FIB-A-NOCH-EE" 	:	[ ('type', "0, 1, 1, 2, 3, 5, 8, 13, 21") ],

		# SYMBOL
		"TIL-DA"			:	[ ('type', "~") ],
		"BANG" 				:	[ ('type', "!") ],
		"ET" 				:	[ ('type', "@") ],
		"HASH" 				:	[ ('type', "#") ],
		"CASH" 				:	[ ('type', "$") ],
		"PERCENT" 			:	[ ('type', "%") ],
		"CARET" 			:	[ ('type', "^") ],
		"AND-PER-SAND" 		:	[ ('type', "&") ],
		"STAR" 				:	[ ('type', "*") ],
		"DOT" 				:	[ ('type', ".") ],
		"COMMA" 			:	[ ('type', ",") ],
		"COLON" 			:	[ ('type', ":") ],
		"SEMI-COLON" 		:	[ ('type', ";") ],
		"SPACE" 			:	[ ('type', " ") ],
		"SLASH"				:	[ ('type', "/") ],
		"BACK-SLASH"		:	[ ('type', "\\") ],	

		# EXTENDED SYMBOLS
		"PA-RENS" 			:	[ ('type', "()"), ('key', "Left") ],
		"LEFT-PA-REN" 		:	[ ('type', "(") ],
		"RIGHT-PA-REN" 		:	[ ('type', ")") ],
		"BRACKETS" 			:	[ ('type', "[]"), ('key', "Left") ],
		"LEFT-BRACKET" 		:	[ ('type', "[") ],
		"RIGHT-BRACKET" 	:	[ ('type', "]") ],
		"BRACES" 			:	[ ('type', "{}"), ('key', "Left") ],
		"LEFT-BRACE" 		:	[ ('type', "{") ],
		"RIGHT-BRACE" 		:	[ ('type', "}") ],
		"SINGLE-QUOTE" 		:	[ ('type', "'") ],
		"SINGLE-QUOTES" 	:	[ ('type', "''"), ('key', "Left") ],
		"DOUBLE-QUOTE" 		:	[ ('type', '"') ],
		"DOUBLE-QUOTES" 	:	[ ('type', "''"), ('key', "Left") ],
		"BACKTICK" 			:	[ ('type', "`") ],
		"BACKTICKS" 		:	[ ('type', "``"), ('key', "Left") ],

		# META
		"OKAY" 				:	[ ('key', "Return") ],
		"CAPS-LOCK" 		:	[ ('key', "Caps_Lock") ],
		"TAB"				:	[ ('key', "Tab") ],
		"PAGE-UP"			:	[ ('key', "Page_Up") ],
		"PAGE-DOWN"			:	[ ('key', "Page_Down") ],

		# TIMESTAMPS
		"TIME-STAMP"		:	[ ('type', datetime.datetime.now().time().strftime("%I:%M:%S %p")) ],
		"DATE-STAMP"		:	[ ('type', datetime.datetime.now().date().strftime("%m/%d/%y")) ],
		"UNIX-STAMP"		:	[ ('type', str(time.time())) ],
		"NICE-STAMP"		:	[ ('type', datetime.datetime.now().ctime()) ],
		"MINUTE" 			: 	[ ('type', str(datetime.datetime.now().minute)) ],
		"HOUR" 				: 	[ ('type', str(datetime.datetime.now().hour)) ],
		"DAY" 				: 	[ ('type', str(datetime.datetime.now().day)) ],
		"MONTH" 			: 	[ ('type', str(datetime.datetime.now().month)) ],
		"YEAR" 				: 	[ ('type', str(datetime.datetime.now().year)) ],
		
		# PK's and ID's
		"UNIQUE-ID"			:	[ ('type', str(uuid.uuid1())) ],

		# WEB
		"COM"				:	[ ('type', "com") 	],
		"ORG"				:	[ ('type', "org") 	],
		"NET"				:	[ ('type', "net") 	],
		"W-W-W"				:	[ ('type', "www") 	],
		"H-T-T-P"			:	[ ('type', "http") 	],
		"H-T-T-P-S"			:	[ ('type', "https") ],
		"GOOGLE"			:	[ ('type', "google") ],
		"G-MAIL"			:	[ ('type', "gmail") ],

		}
}
