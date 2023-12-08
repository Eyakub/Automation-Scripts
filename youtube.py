from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    """
    NB: Video must not be age restricted, if that so you need to login.
    """
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully: ")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    url = "https://www.youtube.com/watch?v=zT7niRUOs9o&ab_channel=TechWithTim"
    save_path = "/Users/eyakubsorkar/Desktop/Automation-Scripts"

    # video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location")
    else:
        download_video(url, save_dir)
