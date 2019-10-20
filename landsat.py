import landsatxplore.api

# Initialize a new API instance and get an access key
api = landsatxplore.api.API("AanandBajaj", "sonicboost123")

# Request
scenes = api.search(
    dataset='LANDSAT_ETM_C1',
    latitude=19.53,
    longitude=-1.53,
    start_date='1995-01-01',
    end_date='1997-01-01',
    max_cloud_cover=10)

print('{} scenes found.'.format(len(scenes)))

for scene in scenes:
    print(scene['acquisitionDate'])

api.logout()
