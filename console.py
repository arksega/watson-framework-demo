#!/usr/bin/env python
import os
import sys

import os
import sys

SCRIPT_DIR, SCRIPT_FILE = os.path.split(os.path.abspath(__file__))
os.environ.update({
    'APP_MODULE': 'bazar',
    'APP_DIR': os.path.join(SCRIPT_DIR, 'bazar'),
    'PUBLIC_DIR': os.path.join(SCRIPT_DIR, 'public'),
    'SCRIPT_DIR': SCRIPT_DIR
})
try:
    import watson
except:
    sys.stdout.write('You must have Watson installed, please run `pip install watson-framework`\n')
    sys.exit(1)

from watson.framework import applications
from bazar.config import config

if __name__ == '__main__':
    os.chdir(os.environ['APP_DIR'])
    application = applications.Console(config)
    application()
