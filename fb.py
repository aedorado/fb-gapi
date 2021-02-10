import facebook
import requests
import time
import csv
import datetime
 
all_vids = []
filename = "videos.csv"
field_names = ["id", "created_time", "permalink_url",
              "length", "title", "description"]
 
 
def write_headers():
   with open(filename, 'w', newline='') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=field_names)
       writer.writeheader()
 
 
def add_videos(videos):
   with open(filename, 'a', newline='') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=field_names)
       for video in videos:
           video['length'] = str(datetime.timedelta(
               seconds=round(video['length'])))
           writer.writerow(video)
           all_vids.append(video)
 
 
def main():
   write_headers()
   graph = facebook.GraphAPI(access_token="t", version="3.1")
   videos = graph.get_object(
       "447059535364591/videos", fields="id,description,title,permalink_url,created_time,length")
   while(True):
       try:
           add_videos(videos['data'])
           print(str(len(all_vids)) + " vidoes collected")
           videos = requests.get(videos['paging']['next']).json()
           time.sleep(0.1)
       except KeyError:
           break
 
 
if __name__ == "__main__":
   main()
 

