bhlog
=====

Adds a call hierarchy information up to the point where the the logger is called to display the log message.

Install and use
---------------

1. python bhlog/setup.py sdist
2. <virtualenv_location>/bin/pip install bhlog.zip 
3. add 

```
import bhlog.log_ch
import bhlog.current_call_stack

# ..... code ....
log_ch.debug("you message {0}".format(bhglog.current_call_stack()))
