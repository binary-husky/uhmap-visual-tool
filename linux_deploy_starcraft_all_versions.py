import os, commentjson, shutil, subprocess
from onedrivedownloader import download
from UTIL.exp_helper import get_ssh_sftp


VERSION = 'starcraft-all-versions'

# download uhmap file manifest | 下载manifest目录文件
try:
    os.makedirs('./Temp')
except:
    shutil.rmtree('./Temp')
    os.makedirs('./Temp')

print('download uhmap file manifest | 下载manifest目录文件')
manifest_url = "https://ageasga-my.sharepoint.com/:u:/g/personal/fuqingxu_yiteam_tech/EVmCQMSUWV5MgREWaxiz_GoBalBRV3DWBU3ToSJ5OTQaLQ?e=I8yjl9"
try:
    file = download(manifest_url, filename="./Temp/")
except:
    print('failed to connect to onedrive | 连接onedrive失败, 您可能需要翻墙才能下载资源')

with open("./Temp/uhmap_manifest.jsonc", "r") as f:
    manifest = commentjson.load(f)

# download unreal engine visual file | 下载虚幻引擎文件
try:
    os.makedirs('./UnrealEngine')
except:
    pass

if not os.path.exists("./UnrealEngine/%s.zip"%VERSION):
    uhmap_url = manifest[VERSION]
    print('download main files | 下载预定文件')
    file = download(uhmap_url, filename="./UnrealEngine/", unzip=True, unzip_path='./UnrealEngine')
else:
    print('Unreal engine binary exists, skip download.. | 虚幻引擎文件已存在, 跳过下载, 若重试请删除UnrealEngine文件夹')
