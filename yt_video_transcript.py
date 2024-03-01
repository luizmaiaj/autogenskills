from youtube_transcript_api import YouTubeTranscriptApi

"""
This Python script uses the YouTubeTranscriptApi to fetch and print the transcript of a YouTube video, given the video's ID.
"""

def get_video_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)
