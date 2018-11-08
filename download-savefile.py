import os
import urllib2

def downloadNewFile(url, filepath):
    try:
        req = urllib2.Request(url)
        req.add_header('softwaretoken', 'gbox_midcontroller')
        content = urllib2.urlopen(req, timeout = 5).read()
        with open(filepath, 'w') as f:
            f.write(content)
        os.system('tar xf /mnt/masstore/midctl.tar -C /gbox_midcontroller/')
        os.system('reboot')
    except Exception:
        print 'error in updating'
