import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'admin', wait=True)

conn.subscribe(destination='/queue/Test_Queues', id=1, ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/queue/Test_Queues')

time.sleep(2)
conn.disconnect()
