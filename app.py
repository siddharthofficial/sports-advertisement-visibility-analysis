import streamlit as st
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import yt_dlp

st.title("🏏 Paytm Logo Visibility Analytics")

st.write("Upload a match video URL to analyze advertisement exposure")

video_url = st.text_input("Enter Video URL")

@st.cache_resource
def load_model():
    return YOLO("best.pt")
model=load_model()


def download_video(url):

    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': 'video.mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "video.mp4"


if st.button("Run Analysis"):

    video_path = download_video(video_url)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fully_visible_frames = 0
    partially_visible_frames = 0
    no_logo_frames = 0
    total_frames = 0
    fully_visible_occurrences = 0
    partially_visible_occurrences = 0
    progress_bar=st.progress(0)
    timeline = []

    data = []
    frame_index=0
    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        frame_index += 1
        total_frames += 1
        progress_bar.progress(frame_index/frame_count)

        if frame_index % 10 != 0:
         continue

        results = model.predict(frame, conf=0.35, verbose=False)

        detected_class = "none"

        for r in results:
            for box in r.boxes:

                class_id = int(box.cls)

                if class_id == 0:
                    detected_class = "fully"

                elif class_id == 1:
                    detected_class = "partial"

        timestamp = frame_index / fps

        if detected_class == "fully":

            fully_visible_frames += 1
            timeline.append(2)

        elif detected_class == "partial":

            partially_visible_frames += 1
            timeline.append(1)

        else:

            no_logo_frames += 1
            timeline.append(0)

        data.append({
            "frame": total_frames,
            "timestamp": timestamp,
            "visibility": detected_class
        })

    cap.release()
    
    # --- Count logo appearances ---
    previous_state = 0

    for state in timeline:

     if state == 2 and previous_state != 2:
        fully_visible_occurrences += 1

     if state == 1 and previous_state != 1:
        partially_visible_occurrences += 1

     previous_state = state

    fully_time = fully_visible_frames / fps
    partial_time = partially_visible_frames / fps
    total_exposure = fully_time + partial_time

    visibility_rate = total_exposure / (total_frames / fps) * 100


    st.subheader(" Exposure Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Fully Visible Time", f"{fully_time:.2f}s")
    col2.metric("Partial Visible Time", f"{partial_time:.2f}s")
    col3.metric("Visibility Rate", f"{visibility_rate:.2f}%")
    
    st.subheader("Logo Appearances")

    col4, col5 = st.columns(2)

    col4.metric("Fully Visible Appearances", fully_visible_occurrences)
    col5.metric("Partial Appearances", partially_visible_occurrences)

    fig, ax = plt.subplots()

    labels = ["Fully Visible", "Partially Visible"]
    values = [fully_time, partial_time]

    ax.bar(labels, values)

    ax.set_title("Logo Exposure Time")
    ax.set_ylabel("Seconds")

    st.pyplot(fig)


    fig2, ax2 = plt.subplots()

    labels = ["Fully", "Partial", "No Logo"]
    values = [fully_visible_frames, partially_visible_frames, no_logo_frames]

    ax2.bar(labels, values)

    ax2.set_title("Frame-wise Logo Detection")
    ax2.set_ylabel("Frames")

    st.pyplot(fig2)


    fig3, ax3 = plt.subplots()

    sizes = [
        fully_visible_frames,
        partially_visible_frames,
        no_logo_frames
    ]

    labels = [
        "Fully Visible",
        "Partially Visible",
        "No Logo"
    ]

    ax3.pie(sizes, labels=labels, autopct="%1.1f%%")

    ax3.set_title("Logo Visibility Distribution")

    st.pyplot(fig3)


    segments = []

    current_state = timeline[0]
    start = 0

    for i in range(1, len(timeline)):

        if timeline[i] != current_state:

            segments.append((start, i, current_state))
            start = i
            current_state = timeline[i]

    segments.append((start, len(timeline), current_state))


    fig4, ax4 = plt.subplots(figsize=(10,2))

    colors = {0:"black",1:"orange",2:"blue"}

    for s,e,state in segments:

        ax4.barh(0,e-s,left=s,color=colors[state])

    ax4.set_title("Broadcast Exposure Timeline")
    ax4.set_yticks([])

    st.pyplot(fig4)


    df = pd.DataFrame(data)

    st.subheader("📄 Frame Timeline Data")

    st.dataframe(df.head())

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "logo_visibility_report.csv",
        "text/csv"
    )