### Dev By Adidev
### Youtube_Comment_Scraper  
import requests
import json
import csv


def get_youtube_comments(api_key, video_id, max_comments):
  base_url = "https://www.googleapis.com/youtube/v3/commentThreads"

  params = {
      'part': 'snippet',
      'videoId': video_id,
      'key': api_key,
      'maxResults':
      min(max_comments,
          100)  # Ensure we don't request more than the API allows
  }

  all_comments_data = []

  while len(all_comments_data) < max_comments:
    response = requests.get(base_url, params=params)
    data = response.json()

    for item in data.get('items', []):
      snippet = item.get('snippet', {})
      comment = snippet.get('topLevelComment', {}).get('snippet', {})

      username = comment.get('authorDisplayName')
      comment_text = comment.get('textDisplay')
      timestamp = comment.get('publishedAt')

      all_comments_data.append([username, comment_text, timestamp])

    # Check if there is another page of comments
    if 'nextPageToken' in data:
      params['pageToken'] = data['nextPageToken']
    else:
      break

  return all_comments_data[:
                           max_comments]  # Trim to the desired number of comments


def save_to_csv(data, output_file='youtube_comments.csv'):
  with open(output_file, mode='w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Username', 'Comment', 'Timestamp'])
    csv_writer.writerows(data)


if __name__ == "__main__":
  api_key = ''  # Replace with your YouTube Data API key
  video_id = ''  # Replace with the actual YouTube video ID

  try:
    max_comments = int(
        input("Enter the number of comments you want to download: "))
  except ValueError:
    print("Please enter a valid number.")
    exit()

  comments_data = get_youtube_comments(api_key, video_id, max_comments)

  if comments_data:
    save_to_csv(comments_data)
    print(
        f"Comments successfully fetched and saved to 'youtube_comments.csv'. Total comments: {len(comments_data)}"
    )
  else:
    print("Failed to fetch comments. Please check your API key and video ID.")
