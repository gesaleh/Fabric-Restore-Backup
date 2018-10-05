# Backup-Restore_fabric

This script will handle

## Backup 
Edit the config json file 
```
{
    "LEDGERS_BACKUP": "./ledger_backup",
```
  the path that will contain the backup peers and orderers
```
    "PEER": {
        "NAME" : [
            "backuprestorefabric_peer0_org1_orange_com_1", "backuprestorefabric_peer1_org1_orange_com_1" 
        ],
        "TOOLS" : [
            "chaincodes", "ledgersData", "peer.pid", "transientStore"
        ],
        "BACKUP": [
            ["backuprestorefabric_peer0_org1_orange_com_1", "peer0_org1"],
            ["backuprestorefabric_peer1_org1_orange_com_1", "peer1_org1"]
        ],
        "RESTORE": [
            ["peer0_org1", "backuprestorefabric_peer0_org1_orange_com_1"],
            ["peer1_org1", "backuprestorefabric_peer1_org1_orange_com_1"]
        ]
    },
```
  Peers configuration 
  - Tools:
    the folder that i backuped from running peer 
  - Names:
    is the container name if you don't know it type `docker ps`
  - Backup:
    array object index:
     - [0] will be container name
     - [1] is the folder name for backup peer in ledger_backup path
  - Restore
    array object index:
     - [0] folder name for backup peer in ledger_backup path
     - [1] container name you want to restore to it
``` 
    "ORDERER": {
        "TOOLS" : [
            "chains", "index"
        ],
        "NAME": "backuprestorefabric_orderer_orange_com_1",
        "BACKUP" : ["backuprestorefabric_orderer_orange_com_1", "orderer"],
        "RESTORE" : ["orderer", "backuprestorefabric_orderer_orange_com_1"]
    }
    
}
```
Orderer Configuration
  - Tools:
    the folder that i backuped from running orderer 
  - Names:
    is the container name if you don't know it type `docker ps`
  - Backup:
    array object index:
     - [0] will be container name
     - [1] is the folder name for backup orderer in ledger_backup path
  - Restore
    array object index:
     - [0] folder name for backup orderer in ledger_backup path
     - [1] container name you want to restore to it
# Run Script 

## Backup
    `python3 backup.py`
    => this will create folder with backuped from ledger

## Restore
    `python3 restore.py`
    => this will restore from backuped folder to container

