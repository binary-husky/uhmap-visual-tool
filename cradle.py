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
