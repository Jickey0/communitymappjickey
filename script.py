import boto3

# Create a Location Service client
location_client = boto3.client('location')

# Specify the map name and map resource name
map_name = 'MyMap1'
map_resource_name = 'YourMapResourceName'

# Specify marker details
marker_coordinates = [-75.480858, 40.632950]  # Example coordinates (longitude, latitude)
marker_label = 'MarkerLabel'

# Add a marker to the map
location_client.batch_update_device_position(
    TrackerName=map_name,
    Updates=[
        {
            'DeviceId': 'UniqueDeviceID',
            'Position': marker_coordinates,
            'SampleTime': '2023-01-01T00:00:00Z',
            'CustomPosition': {
                'Latitude': marker_coordinates[1],
                'Longitude': marker_coordinates[0],
            },
            'DeviceMetadata': {
                'DeviceState': 'ACTIVE',
            },
        },
    ],
)