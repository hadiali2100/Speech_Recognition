import requests
n = input("n: ")

if n == '0':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=HIGH&deviceName=BOLT1119308')
elif n == '1':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=HIGH&deviceName=BOLT1119308')
elif n == '2':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=HIGH&deviceName=BOLT1119308')
elif n == '3':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=HIGH&deviceName=BOLT1119308')
elif n == '4':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=HIGH&deviceName=BOLT1119308')
elif n == '10':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=LOW&deviceName=BOLT1119308')
elif n == '-1':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=LOW&deviceName=BOLT1119308')
elif n == '-2':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=LOW&deviceName=BOLT1119308')
elif n == '-3':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=LOW&deviceName=BOLT1119308')
elif n == '-4':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=LOW&deviceName=BOLT1119308')
elif n == 'ALL':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=HIGH&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=HIGH&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=HIGH&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=HIGH&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=HIGH&deviceName=BOLT1119308')
elif n == 'N':
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=0&state=LOW&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=1&state=LOW&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=2&state=LOW&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=3&state=LOW&deviceName=BOLT1119308')
    res = requests.get('https://cloud.boltiot.com/remote/d9cc968c-6a7f-4ad0-ae30-abc625086a34/digitalWrite?pin=4&state=LOW&deviceName=BOLT1119308')




print(res)