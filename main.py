import os.path
import sys
from Utility.Downloader import download_as_file as downloader
import Statistics as stat

if __name__ == "__main__":
    try:
        _, url, file_name = sys.argv
    except:
        try:
            _, url, = sys.argv
            file_name = os.path.basename(url)
            downloader(url, file_name)
        except Exception as e:
            print("Something went wrong.. : ", e)
            sys.exit(1)
    downloader(url, file_name)
    
    stat.create_statistics(file_name)
    