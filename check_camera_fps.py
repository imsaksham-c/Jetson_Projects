import cv2
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Read video source and print frame size and FPS")
parser.add_argument('--video', type=str, help="Path to the video file or camera index (0 for webcam)", required=True)
args = parser.parse_args()

# Open the video source (file or camera)
video_source = args.video

# If a camera index is passed, convert it to an integer
try:
    video_source = int(video_source)
except ValueError:
    pass

# Capture the video
cap = cv2.VideoCapture(video_source)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Get the frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get the frames per second (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)

# Print the frame size and FPS
print(f"Frame Size: {frame_width}x{frame_height}")
print(f"Frames per Second (FPS): {fps}")

# Release the video capture object
cap.release()
