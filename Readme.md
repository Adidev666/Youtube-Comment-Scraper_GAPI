### YouTube Comment Scraper
### Dev By Adidev666(ADITYA DAS)
### Follow and Support me on Github 
 
**Description:**
This Python script allows you to scrape comments from a YouTube video and save them to a CSV file. It utilizes the YouTube Data API v3 for efficient retrieval of comments, usernames, and timestamps. The script handles paginated requests, ensuring all comments are captured based on user preference.

**Prerequisites:**
1. **YouTube Data API Key:**
   - Obtain an API key from the [Google Cloud Console](https://console.developers.google.com/).
   - Enable the YouTube Data API v3 for your project.
   - Create an API key to authenticate your requests.

2. **Python Libraries:**
   - Install required Python libraries using the following command:
     ```bash
     pip install requests beautifulsoup4
     ```

**Usage:**
1. Replace `'YOUR_API_KEY_HERE'` with your obtained YouTube Data API key.
2. Replace `'YOUR_VIDEO_ID_HERE'` with the actual YouTube video ID you want to scrape comments from.
3. Run the script and enter the desired number of comments when prompted.

**Output:**
The script will fetch comments based on your input and save them to a CSV file named 'youtube_comments.csv'. The CSV file includes columns for usernames, comments, and timestamps.

---

