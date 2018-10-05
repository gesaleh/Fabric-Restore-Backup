import json
import os 
import subprocess
import shutil

with open('config.json', 'r') as f:
    config = json.load(f)

stop_docker = "docker stop {}"
start_docker = "docker start {}"
docker_cp = "docker cp {}/{}/{} {}:{}"

backup_path=config["LEDGERS_BACKUP"]

ORDERER = config["ORDERER"]
PEER = config["PEER"]

def shellCommand(command):
    print("run command {}".format(command))
    out = subprocess.Popen(command.split(" "),
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
           
    return out.communicate()

def restorePeer():
    peers=PEER["RESTORE"]
    tools=PEER["TOOLS"]
    productionPath="/var/hyperledger/production"

    for peer in peers:
        for tool in tools:
            print("Backup {} ....".format(peer))
            out = shellCommand(docker_cp.format(backup_path, peer[0], tool, peer[1], productionPath))
            print("Done {} \n result: {}".format(peer, out))        

def restoreOrderer():
    orderer=ORDERER["NAME"]
    tools=ORDERER["TOOLS"]
    orderer_backup = ORDERER["RESTORE"]
    productionPath="/var/hyperledger/production/orderer/"

    for tool in tools:
        print("Backup {} ....".format(orderer))
        out = shellCommand(docker_cp.format(backup_path, orderer_backup[0], tool, orderer_backup[1], productionPath))
        print("Done {} \n result: {}".format(orderer, out))        


def stopContainer():
    peersAndOrderer = "{} {}".format(ORDERER["NAME"], " ".join(PEER["NAME"]))
    print("Stopping container {} ....".format(peersAndOrderer))
    out = shellCommand(stop_docker.format(peersAndOrderer))
    print("Done {}".format(out))


def startContainer():
    peersAndOrderer = "{} {}".format(ORDERER["NAME"], " ".join(PEER["NAME"]))
    print("Stopping container {} ....".format(peersAndOrderer))
    out = shellCommand(start_docker.format(peersAndOrderer))
    print("Done {}".format(out))

stopContainer()
restorePeer()
restoreOrderer()
startContainer()