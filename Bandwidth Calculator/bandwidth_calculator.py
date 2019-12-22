import bandwidthAnalyzer
import pingAnalyzer

# Get all the Values
getServerStatus = pingAnalyzer.pingingfunction()
getDownloadTime = bandwidthAnalyzer.caculatetimefordownloads()
getDownloadFileSize = bandwidthAnalyzer.filesize
getUploadTime = bandwidthAnalyzer.caculatetimeforuploads()


# Calculate the Download Speed in Kb/s
def DownloadSpeed():
    DownloadedFileSize = getDownloadFileSize / 1000
    download_speed = DownloadedFileSize / getDownloadTime
    return download_speed


# Calculate the Upload Speed in Kb/s
def UploadSpeed():
    UploadedFileSize = 1048575 / 1000
    upload_speed = UploadedFileSize / getUploadTime
    return upload_speed


if __name__ == '__main__':
    print(
        "________________________________________________________________________________________________________________")
    if getServerStatus:
        print(" The Server is up and running")
    else:
        print("The server is down")

    print(
        "________________________________________________________________________________________________________________")
    print(f"Download Speed ={DownloadSpeed()} Kb/s")
    print(f"Upload Speed={UploadSpeed()} Kb/s")
