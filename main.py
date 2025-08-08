import cv2
import os

# Path to the folder containing the videos
video_folder = r"C:\Users\Administrator\Desktop\videos"

# Number of videos you have (adjust if needed)
num_videos = 18  # or any number you want to process

for i in range(1, num_videos + 1):
    video_path = os.path.join(video_folder, f"video{i}.mp4")  # assuming .mp4 extension
    thumb_path = os.path.join(video_folder, f"thumb{i}.jpg")

    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Cannot open video {video_path}")
        continue

    # Read the first frame
    ret, frame = cap.read()
    if ret:
        # Save the frame as an image
        cv2.imwrite(thumb_path, frame)
        print(f"Saved thumbnail for video{i} as {thumb_path}")
    else:
        print(f"Failed to read frame from {video_path}")

    cap.release()
