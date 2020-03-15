activate_this = '/var/www/envs/wolf-bs/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/envs/wolf-bs/lib/python3.7/site-packages')
sys.path.insert(0, '/var/www/wolf/')


from wolf.app import app as application
