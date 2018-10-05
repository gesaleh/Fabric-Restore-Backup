import json
import os 
import subprocess
import shutil

backup = "docker cp {}:{} {}/{}"

with open('config.json', 'r') as f:
    config = json.load(f)

ORDERER = config["ORDERER"]
BACKUP_PATH = config["LEDGERS_BACKUP"]

PEER = config["PEER"]

def make_dir(path, rec=True):
    print("Creading folder {} ....".format(path))
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("the {} Exist".format(path))
        if (rec):
            print("removing existing {} ...".format(path))
            shutil.rmtree(path)
            make_dir(path, False)

def shellCommand(command):
    print("run command {}".format(command))
    out = subprocess.Popen(command.split(" "), 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)

    return out.communicate()

def backupOrderer():
    orderBackupPath = "/var/hyperledger/production/orderer/"
    
    ordererName = ORDERER["NAME"]
    orderer_backup = ORDERER["BACKUP"]
    
    print("Backup {} ....".format(ordererName))
    out = shellCommand(backup.format(orderer_backup[0], orderBackupPath, BACKUP_PATH, orderer_backup[1]))
    print("Done {} \n result: {}".format(ordererName, out))

def backupPeers():
    peers = PEER["BACKUP"]
    backupPath = config["LEDGERS_BACKUP"]
    peerBackupPath = "/var/hyperledger/production"

    for peer in peers:
        print("Backup {} ....".format(peer))
        
        out = shellCommand(backup.format(peer[0], peerBackupPath, backupPath, peer[1]))
        print("Done {} \n result: {}".format(peer, out))

make_dir(config["LEDGERS_BACKUP"])
backupOrderer()
backupPeers()