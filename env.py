# -*- encondig: utf-8 -*-
#!/usr/bin/python

URL = "YOUR-FTP-SERVER-ADDRESS" #"ftp.example.com"
PORT = 21 #if you have changed your ftp's port
USER = "YOUR-FPT-USER"  
PASSD = "YOUR-FTP-PASSWORD" 
PATH = "PATH/TO/THE/SERVER" #Where you're going to upload your file ex: /public_ftp/incomming
FILE = "PATH/TO/THE/FILE" #Absolute path to the fileyou want to upload.
LOG = "ftp_client.log" #log file
FILENAME = "YOUR-FILENAME-SERVER" # File's name on the server. ex: upload_file.txt
REMOVE = True #if you want to erase the file in local after FTP Conection
