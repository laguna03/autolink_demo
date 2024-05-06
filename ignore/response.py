#!/usr/bin/env python3
from client_operations import read_client_endpoint
import sys
sys.path.append('/Users/manuel/Desktop/autolink_demo/api/app')


client_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d478'
response = read_client_endpoint(client_id)
print(response)

