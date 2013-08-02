# voccs 
### Voice Operated Coding and Control System

> Setup

* make sure you're `cd`'d into the voccs folder

* run `sudo bash /tools/get_dependencies.sh` 

* then run `ln -s /usr/local/bin/voccs voccs.py`

> Basic Usage

* "Shutdown" or "Shutdown Vox"
    - Stop's the speech recognition and shuts down voccs
    - (remember to run `bash kill.sh` after shutting down voccs)

* "Switch [number]"
    - Switches to that terminal window (by number)
  

* "Activate [scope-name]" or "Deactivate [scope-name]" 
    - Enable or disable scope by name. 
    - If a scope is disabled it will not perform any actions.


* "Show-Active" 
    - Displays a list of scopes that are currently active
