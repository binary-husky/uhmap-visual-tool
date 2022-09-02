import os, commentjson, shutil, subprocess
from onedrivedownloader import download
from UTIL.exp_helper import get_ssh_sftp


VERSION = 'uhmap-v1'
addr = "172.18.116.149:2266"
usr  = "hmp"
pwd  = "hmp"
remote_config = '/home/hmp/MultiServerMission/try-start-pr-db/src/ZHECKPOINT/RVE-drone2-ppoma-run2/experimentT.jsonc'
remote_folder, _ = remote_config.split('/ZHECKPOINT') 


# download uhmap file manifest | 下载manifest目录文件
# download uhmap file manifest | 下载manifest目录文件
try:
    os.makedirs('./Temp')
except:
    shutil.rmtree('./Temp')
    os.makedirs('./Temp')

print('download uhmap file manifest | 下载manifest目录文件')
manifest_url = "https://ageasga-my.sharepoint.com/:u:/g/personal/fuqingxu_yiteam_tech/EVmCQMSUWV5MgREWaxiz_GoBalBRV3DWBU3ToSJ5OTQaLQ?e=I8yjl9"
download(manifest_url, filename="./Temp/manifest.jsonc")
with open("./Temp/manifest.jsonc", "r") as f:
    manifest = commentjson.load(f)

# download unreal engine visual file | 下载虚幻引擎文件
# download unreal engine visual file | 下载虚幻引擎文件
try:
    os.makedirs('./UnrealEngine')
except:
    pass

if not os.path.exists("./UnrealEngine/%s.zip"%VERSION):
    uhmap_url = manifest[VERSION]
    download(uhmap_url, filename="./UnrealEngine/%s.zip"%VERSION, unzip=True, unzip_path='./UnrealEngine')
else:
    print('Unreal engine binary exists, skip download.. | 虚幻引擎文件已存在, 跳过下载, 若重试请删除UnrealEngine文件夹')

# Fetch code, trained model from linux server | 从远程服务器拿代码和模型
# Fetch code, trained model from linux server | 从远程服务器拿代码和模型
try:
    os.makedirs('./RemoteCode')
except:
    shutil.rmtree('./RemoteCode')
    os.makedirs('./RemoteCode')
ssh, sftp = get_ssh_sftp(addr, usr, pwd)
print('downloading from remote server, this is going to take some time | 从linux服务器下载代码和模型中, 请等待')
sftp.get_dir(source=remote_folder, target='./RemoteCode', ignore_list=['.git', 'PROFILE', 'TEMP'], win_compat=True)
_, local_config = remote_config.split('/ZHECKPOINT') 
local_config = './RemoteCode/' + local_config




import os, shutil, subprocess
import commentjson as json
os.chdir('RemoteCode')

local_conf = "C:/Users/fuqingxu/Desktop/uhmap-visual-tool/RemoteCode/ZHECKPOINT/RVE-drone2-ppoma-run2/experimentT.jsonc"


with open(local_conf, encoding='utf8') as f:
    json_data = json.load(f)
json_data["config.py->GlobalConfig"]["num_threads"] = 1
json_data["config.py->GlobalConfig"]["fold"] = 1
json_data["config.py->GlobalConfig"]["test_only"] = True

json_data["MISSION.uhmap.uhmap_env_wrapper.py->ScenarioConfig"]["render"] = True
json_data["MISSION.uhmap.uhmap_env_wrapper.py->ScenarioConfig"]["UhmapRenderExe"] = './../UnrealEngine/WindowsNoEditor/UHMP.exe'
json_data["MISSION.uhmap.uhmap_env_wrapper.py->ScenarioConfig"]["TimeDilation"] = 2
for i in json_data.keys():
    for j in json_data[i].keys():
        if j=='load_specific_checkpoint':
            json_data[i][j] = json_data[i][j].replace(':','_')

with open(local_conf, 'w') as f:
    json.dump(json_data, f, indent=4)

    
subprocess.run('python main.py -c %s'%local_conf)


