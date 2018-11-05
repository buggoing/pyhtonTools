import uuid

def getTimestampFromUuidString(uuidString):
    return uuid.UUID(uuidString).time

def getTimestampFromFilename(filename):
    uuidString = filename.split('_')[1]
    timestamp = getTimestampFromUuidString(uuidString)
    return timestamp

filename = 'gbox_2c40bc87-dc2a-11e8-a7c0-16d4bbc07901_3_3.jpg'
print getTimestampFromFilename(filename)
