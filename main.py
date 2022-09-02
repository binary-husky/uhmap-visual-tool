import os, commentjson, shutil
from onedrivedownloader import download
from UTIL.exp_helper import get_ssh_sftp


VERSION = 'uhmap-v1'


# remove folders | 删除临时文件夹
try:
    os.makedirs('./Temp')
except:
    shutil.rmtree('./Temp')
    os.makedirs('./Temp')

print('>> download uhmap file manifest')
manifest_url = "https://ageasga-my.sharepoint.com/:u:/g/personal/fuqingxu_yiteam_tech/EVmCQMSUWV5MgREWaxiz_GoBalBRV3DWBU3ToSJ5OTQaLQ?e=I8yjl9"
download(manifest_url, filename="./Temp/manifest.jsonc")
with open("./Temp/manifest.jsonc", "r") as f:
    manifest = commentjson.load(f)



try:
    os.makedirs('./UnrealEngine')
except:
    pass

uhmap_url = manifest[VERSION]
download(uhmap_url, filename="./UnrealEngine/%s.zip"%VERSION, unzip=True, unzip_path='./UnrealEngine')




# remove folders | 删除临时文件夹
try:
    os.makedirs('./RemoteCode')
except:
    shutil.rmtree('./RemoteCode')
    os.makedirs('./RemoteCode')
    
# Address, usr, pwd of remote linux server for ssh connection | 远程linux服务器的地址、用户名、密码
addr = "172.18.116.149:2266"
usr  = "hmp"
pwd  = "hmp"
remote_folder = '/home/hmp/MultiServerMission/try-start-pr-db/src/'
remote_config = '/home/hmp/MultiServerMission/try-start-pr-db/src/ZHECKPOINT/RVE-drone2-ppoma-run2/experimentT.jsonc'








# Fetch code, trained model from linux server | 从远程服务器拿代码和模型
ssh, sftp = get_ssh_sftp(addr, usr, pwd)
print('downloading from remote server, this is going to take some time | 下载代码中, 请等待')
sftp.get_dir(source=remote_folder, target='./RemoteCode', ignore_list=['.git', 'PROFILE', 'TEMP'], win_compat=True)
_, local_config = remote_config.split('/ZHECKPOINT') 
local_config = './RemoteCode/' + local_config









