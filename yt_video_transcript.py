from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'pmvciDB0Bmg'
transcript = YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)
