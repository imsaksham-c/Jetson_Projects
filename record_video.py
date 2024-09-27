import cv2
import argparse
import time

def record_rtsp_video(rtsp_link, output_file="./output.mp4", record_duration=30):
    # Open the video stream
    cap = cv2.VideoCapture(rtsp_link)

    if not cap.isOpened():
        print(f"Error: Unable to open the video stream: {rtsp_link}")
        return

    # Get the frame width, height, and frames per second (fps)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    print(f"Recording video for {record_duration} seconds...")

    # Calculate when to stop recording
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Write the frame to the output file
        out.write(frame)

        # Check if the recording duration has been reached
        if time.time() - start_time >= record_duration:
            break

    # Release resources
    cap.release()
    out.release()
    print(f"Video saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Record 30 seconds of video from a stream.")
    parser.add_argument("--video", required=True, help="Video stream link (RTSP or file).")
    parser.add_argument("--output_file", default="./output.mp4", help="Output video file name (default: ./output.mp4).")
    args = parser.parse_args()

    # Record the video from the stream
    record_rtsp_video(args.video, args.output_file)
