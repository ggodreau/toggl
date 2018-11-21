import sys
import requests
import json
import pandas as pd

endpoint = 'https://www.toggl.com/api/v8/time_entries'

def main():
  apikey, start_date, end_date = parse_args(sys.argv)[1:]
  write_file(
    call_api(endpoint, apikey, start_date, end_date)
  )

def call_api(endpoint, apikey, start_date, end_date):
  res = requests.get(
    endpoint,
    auth=(apikey, 'api_token'),
    params={'start_date': start_date, 'end_date': end_date})
  if res.status_code != 200:
    print(f'API Call failed with status code {res.status_code}.\n\
Debug output: \n\n {res.content} \n\nExiting...\n')
    exit(0)
  else:
    return res.json()

def write_file(data):
  if data == None:
    print('No data in file, exiting...')
    exit(0)
  else:
    loc = input('Enter desired file location and name (default ./out.csv): ')
    try:
      if len(loc) == 0:
        loc = './out.csv'
      pd.DataFrame(data).to_csv(loc, index=False)
      print(f'Data successfully written to {loc}. Exiting...')
    except:
      print('What the fuck did you just give me??')
      exit(0)
    exit(0)
    

def parse_args(input):
  if len(input) != 4:
    raise NameError('Number of arguments not correct. \n \
Format: python get_tasks.py <api_key> <start_date> <end_date> \n \
Example: python get_tasks.py 894e66455860a4ea3fde5dd0cf35f566 2018-08-29T15:42:46+02:00 2018-09-24T15:42:46+02:00 \n')
    # exit(0)
  else:
    return (sys.argv)

if __name__ == '__main__':
  main()
