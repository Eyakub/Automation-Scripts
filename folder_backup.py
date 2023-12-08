import os
import shutil
import datetime
import schedule
import time


SOURCE_DIR = "/Users/eyakubsorkar/Personal/backup_source"
DESTINATION_DIR = "/Users/eyakubsorkar/Personal/destination_source"


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    destination_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("02:10").do(lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR))

while True:
    schedule.run_pending()
    time.sleep(60)
# copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR)