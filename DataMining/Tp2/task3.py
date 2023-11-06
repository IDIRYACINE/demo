# import the necessary libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json

def search_video(video_id):
    api_key = "ApiKEy"
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        video_response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        video_title = video_response['items'][0]['snippet']['title']
        video_description = video_response['items'][0]['snippet']['description']

        comments_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText'
        ).execute()

        comments = []
        for item in comments_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments.append({'author': author, 'comment': comment})

        with open ("./{}.json".format(video_id), 'w') as outfile:
            json.dump({'title': video_title, 'description': video_description, 'comments': comments}, outfile, indent=4)

    except HttpError as e:
        print('An error occurred: %s' % e)
        return None

search_video('rczDieh3_ng')