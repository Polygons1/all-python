import os
import time

print('currently logind on as ' + os.getlogin() + '\ncurrent time:', str(time.localtime()[3]) + ':' + str(time.localtime()[4]))