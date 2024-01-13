from pytube import YouTube

def download_video(url, path):
    try:
        # Create a YouTube object using the provided URL
        yt = YouTube(url)
        
        # Get information about the video
        print(f"Video Title: {yt.title}")
        print(f"Video Duration: {yt.length} seconds")
        
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        
        # Download the video to the specified path
        video_stream.download(output_path=path)
        print("Download completed")
    except Exception as e:
        # Handle exceptions (errors) that might occur during the process
        print("Error:", str(e))

# Example usage
video_link = ""  # Add your YouTube video URL here
save_path = r""  # Add your desired download path here
download_video(video_link, save_path)
