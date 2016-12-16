#!/usr/bin/python
# -*- encondig: utf-8 -*-

from ftplib import FTP
from datetime import datetime
import env, os, logging


now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
logging.basicConfig(filename=env.LOG, filemode='a', level=logging.DEBUG)

try:
    print 'Starting FTP Connection'

    ftp = FTP()
    ftp.connect(env.URL, env.PORT)
    ftp.login(env.USER, env.PASSD)
    f = open(env.FILE, 'rb') 
    ftp.cwd(env.PATH)

    try:
        print "Uploading file from %s to %s:%s" % (env.FILE, env.URL, env.PATH)

        ftp.storlines('STOR ' + env.FILENAME, f)        
        
        if env.REMOVE:
            os.remove(env.FILE)
            print "Erasing %s..." % env.FILE
            
        print """
    	        Transference Successfull
                Process Completed
            """

        msj = 'Uploaded file Successful at %s in %s' % (now, env.PATH)
        logging.info(msj)


    except Exception, e:
        print str(e)
        logging.warning('ERROR: %s %s' % (str(e), now))
   
    

except Exception, e:
    logging.warning(str(e))
    msj = 'FTP transferetion failed. File %s was not upload at %s' % (env.FILE, now)
    logging.warning(msj)
   
    print """
	Opps something is wrong:
	%s. Check the %s
    """ % (str(e), env.LOG)

finally:
    ftp.quit()
    ftp.close()
