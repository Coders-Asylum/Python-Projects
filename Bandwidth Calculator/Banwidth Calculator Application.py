import bandwidth_calculator
import pingAnalyzer

if __name__ == '__main__':
    try:
        CheckConnection = pingAnalyzer.pingingfunction()
    except Exception:
        CheckConnection = False

    if CheckConnection == True:  # the statement is equal to 'pingAnalyzer.pingingfunction()== True
        DownloadSpeed = bandwidth_calculator.DownloadSpeed()
        UploadSpeed = bandwidth_calculator.UploadSpeed()

        print("connected")
        if DownloadSpeed >= 3600:
            print("Connection is too slow")
        else:
            print(f"The Download Speed= {DownloadSpeed / 125} Mbps")
            print(f"The Upload Speed={UploadSpeed / 125} Mbps")
    else:
        print("not connected")
