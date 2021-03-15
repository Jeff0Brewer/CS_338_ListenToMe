#only open system preferences if terminal does NOT have control over computer
import os
import sqlite3
from shortcut_control import curr_system

def commandLineControlMac():
    if curr_system == "Darwin":
        print('Checking to see if preferences are set for terminal access...')
        try:
            connection = sqlite3.connect("/Library/Application Support/com.apple.TCC/TCC.db")
            connection.row_factory = lambda cursor, row: row[0]

            cursor = connection.cursor()

            try: #first try if big sur (with auth_value in query) will work.
                rows = cursor.execute('select client from access where service like "kTCCServiceAccessibility" and auth_value = 2;').fetchall()
                if 'com.apple.Terminal' not in rows:
                    print('Not found')
                    os.system("open 'x-apple.systempreferences:com.apple.preference.security?Privacy'")
                else:
                    print('Found')

            except: #if it errors, assume OS is older. try allowed in query
                rows = cursor.execute('select client from access where service like "kTCCServiceAccessibility" and allowed = 1;').fetchall()
                if 'com.apple.Terminal' not in rows:
                    print('Terminal does not have access. Please change this in settings. Opening settings...')
                    os.system("open 'x-apple.systempreferences:com.apple.preference.security?Privacy'")
                else:
                    print('Found. Terminal has access.')

            print('All set up!')
        except:
            print('Different os system. Cannot check system preferences.')
