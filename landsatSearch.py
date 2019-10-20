import landsatxplore.api
from landsatxplore.earthexplorer import EarthExplorer


# enter user information
username = "" 
password = "" 
dataset = 'LANDSAT_ETM_C1'
outputFolder = './data'


# enter location information
latitude = 0
longitutde = 0
start_date = 'yyyy-mm-dd'
end_date = 'yyyy-mm-dd'
max_cloud_cover = 0


api = landsatxplore.api.API(username, password)

#Scene Requests
scenes = api.search(data,
                    latitude,
                    longitude,
                    start_date,
                    end_date,
                    max_cloud_cover)

for scene in scenes:
    ee.download(scene['entityID'], output_dir = outputFolder)

ee.logout()
api.logout() 
