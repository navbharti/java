'''
Created on Nov 9, 2014

@author: rajni
'''
import soundcloud

# create client object with app and user credentials
client = soundcloud.Client(client_id='b0d5791113277104bcdcd445b15df6c5',
                           client_secret='43849b5d768bc76154cf5e23ab1c1ae9',
                           username='navbharti',
                           password='soundcloud123#')

resolve = client.get('/resolve')
print resolve