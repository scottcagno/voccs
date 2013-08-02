#!/usr/bin/env python
# Copyright (c) 2013, Scott Cagno
# All rights reserved.
# BSD LICENSED (can be found in LICENSE file)

scope = {
	
	'name'				:	'shell',
	'id'				: 	2,
	'type'				: 	'base',
	'active'			:	False,
	'actions'			:	{

		# UNIQUE
		"PASSWORD"			:	[ ('type', "envnei9049") ],
		"ROOT-PASSWORD"		:	[ ('type', "d10No335") ],

		# COMMON COMMANDS
		"L-S"				:	[ ('type', "ls ") ],
		"CLEAR"				:	[ ('type', "clear"), ('key', "Return") ],
		"UNDO"				:	[ ('key', "shift+alt+b"), ('key', "ctrl+k") ],
		"DELETE"			:	[ ('key', "Delete") ],
		"C-D"				:	[ ('type', "cd ") ],
		"D-F"				:	[ ('type', "df -h ") ],
		"M-K-DIR"			:	[ ('type', "mkdir ") ],
		"TOUCH"				:	[ ('type', "touch ") ],
		"M-V"				:	[ ('type', "mv ") ],
		"DATE"				:	[ ('type', "date ") ],
		"TREE"				:	[ ('type', "tree ") ],
		"FIND"				:	[ ('type', "find . ") ],
		"MAN"				:	[ ('type', "man ") ],
		"R-M"				:	[ ('type', "rm -rf ") ],
		"CAT"				:	[ ('type', "cat ") ],
		"VIM"				:	[ ('type', "vim ") ],
		"EXIT"				:	[ ('type', "exit"), ('key', "Return") ],
		"SUDO"				:	[ ('type', "sudo ") ],
		"C-H-MOD"			:	[ ('type', "chmod ") ],
		"C-H-OWN"			:	[ ('type', "chown ") ],
		"P-W-D"				:	[ ('type', "pwd ") ],
		"H-TOP"				:	[ ('type', "htop ") ],
		"TOP"				:	[ ('type', "top ") ],
		"TAIL"				:	[ ('type', "tail ") ],
		"GREP"				:	[ ('type', "grep ") ],
		"LESS"				:	[ ('type', "less ") ],
		"KILL"				:	[ ('type', "kill ") ],
		"P-S"				:	[ ('type', "ps ") ],
		"P-I-D-OF"			:	[ ('type', "pidof ") ],
		"WHO"				:	[ ('type', "w ") ],
		"APT-GET"			:	[ ('type', "apt-get ") ],
		"S-S-H"				:	[ ('type', "ssh ") ],
		"AWK"				:	[ ('type', "awk ") ],
		"SED"				:	[ ('type', "sed ") ],
		"PING"				:	[ ('type', "ping ") ],
		"HOST"				:	[ ('type', "host ") ],
		"TAR"				:	[ ('type', "tar ") ],
		"CURL"				:	[ ('type', "curl ") ],
		"QUIT"				:	[ ('type', "q") ],
		"EXPORT"			:	[ ('type', "export ") ],
		"ALIAS"				:	[ ('type', "alias ") ],
		"BASH-R-C"			:	[ ('type', ".bashrc") ],
		"VIM-R-C"			:	[ ('type', ".vimrc") ],
		"HOME"				:	[ ('type', "~/") ],
		"U-NAME"			:	[ ('type', "uname ") ],
		"WHO-AM-I"			:	[ ('type', "whoami ") ],
		"USER"				:	[ ('type', "$USER") ],
		"ROOT"				:	[ ('type', "root") ],

		# SYMBOLS
		"TACK"				:	[ ('type', "-") ],
		"BACKGROUND"		:	[ ('type', "&") ],

		# SHORTCUTS
		"AUTO"				:	[ ('key', "Tab") ],					
		"REVERSE-SEARCH"	:	[ ('key', "ctrl+r") ],					

		# MOVEMENT							
		"START-OF-LINE"		:	[ ('key', "ctrl+a") ],				
		"END-OF-LINE"		:	[ ('key', "ctrl+e") ],							
		"UP"				:	[ ('key', "Up") ],
		"DOWN"				:	[ ('key', "Down") ],
		"LEFT"				:	[ ('key', "Left") ],
		"RIGHT"				:	[ ('key', "Right") ],

		# PROCESS CONTROL
		"NO-HUP"			:	[ ('type', "nohup  2>&1 &"), ('key', "ctrl+a"), ('key', "shift+alt+f"), ('key', "Right") ],
		"SUSPEND"			:	[ ('key', "ctrl+z") ],
		"FORE-GROUND"		:	[ ('type', "fg"), ('key', "Return") ],	
		"STOP"				:	[ ('key', "ctrl+c") ],

		# MODIFIERS/FLOW REDIRECTION
		"PIPE"				:	[ ('type', " | ") ],		
		"RE-DIRECT"			:	[ ('type', " > ") ],		
		"APPEND"			: 	[ ('type', " >> ") ],		
		"RE-DIRECT-OUTPUT"	: 	[ ('type', " 2>&1 ") ],

		# GIT 
		"GIT-CONFIG"		:	[ ('type', "git config -global user.name 'scottcagno'; git config -global user.email 'scottiecagno@gmail.com'") ],
		"GIT-IN-IT"			:	[ ('type', "git init; touch README.md") ],			
		"GIT-ADD"			:	[ ('type', "git add ") ],
		"GIT-REMOVE"		:	[ ('type', "git rm ") ],								
		"GIT-ADD-ORGIN"		:	[ ('type', "git remote add origin https://github.com/scottcagno/.git"), ('key', "Left"), ('key', "Left"), ('key', "Left"), ('key', "Left") ],
		"GIT-PUSH"			:	[ ('type', "git push origin master") ],
		"GIT-CLONE"			:	[ ('type', "git clone https://github.com/scottcagno/.git"), ('key', "Left"), ('key', "Left"), ('key', "Left") ],

		# SCREEN MULTIPLEXING
		"T-MUX"				:	[ ('type', "tmux"), ('key', "Return") ],	
		"SPLIT"				:	[ ('key', "ctrl+b"), ('type', "%") ],	
		"CYCLE"				:	[ ('key', "ctrl+b"), ('type', "o") ],	
		"NEW-WINDOW"		:	[ ('key', "ctrl+b"), ('type', "c") ],	
		"CYCLE-WINDOW"		:	[ ('key', "ctrl+b"), ('type', "n") ]		
	}

}