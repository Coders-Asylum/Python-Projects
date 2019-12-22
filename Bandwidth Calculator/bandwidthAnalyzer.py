import os
import time

import requests
from flask import Flask
from flask_mail import Mail, Message

import timecalculations

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['Email_user_id'],
    "MAIL_PASSWORD": os.environ['Email_password']
}
app = Flask(__name__)
app.config.update(mail_settings)
mail = Mail(app)
mailRecipientItself = app.config.get("MAIL_USERNAME")


def analyzedownloadspeed():
    url = 'https://raw.githubusercontent.com/Coders-Asylum/Python-Projects/master/resources/5MbFile.txt'
    url2 = 'https://raw.githubusercontent.com/Coders-Asylum/Python-Projects/master/resources/5MbFile.txt'
    record_start_time_no_download = time.time()  # time recorded
    request_url = requests.get(url)
    record_end_time_no_download = time.time()  # time recorded

    # time.sleep(1.0)
    record_down_start_time = time.time()  # time recorded
    request_url = requests.get(url2)
    with open('C:/Users/Adithya B. Shetty/Downloads/demo.txt', 'wb') as downloadedFile:
        downloadedFile.write(request_url.content)

    record_down_end_time = time.time()  # time recorded

    file_information = os.stat('C:/Users/Adithya B. Shetty/Downloads/demo.txt')
    downloaded_file_size = file_information.st_size

    # delete the downloaded file
    os.unlink('C:/Users/Adithya B. Shetty/Downloads/demo.txt')

    return record_start_time_no_download, record_end_time_no_download, record_down_start_time, record_down_end_time, downloaded_file_size


tStartwithoutdownload, tendwithoutdownload, tstartwithdownload, tendwithdownload, filesize = analyzedownloadspeed()


def analyzeuploadspeed():
    with app.app_context():
        # Record time required to send mail without attachments
        record_normal_up_start_time = time.time()  # time recorded
        msg_without_attach = Message(subject="Test pls delete", sender=app.config.get("MAIL_USERNAME"),
                                     recipients=[app.config.get("MAIL_USERNAME")])
        mail.send(msg_without_attach)
        record_normal_up_end_time = time.time()  # time recorded

        # time.sleep(1.0)

        # Record time Required to send mail with attachments
        record_upstart_time = time.time()  # time recorded
        msg_with_attachments = Message(subject="Test File Delete after Use", sender=app.config.get("MAIL_USERNAME"),
                                       recipients=[mailRecipientItself])
        openfile = open("C:/Users/Adithya B. Shetty/Desktop/1MbFile.txt", "r")
        msg_with_attachments.attach(filename="sample", content_type="text/plain", data=openfile.read())
        mail.send(msg_with_attachments)
        record_up_end_time = time.time()  # time recorded

    return record_normal_up_start_time, record_normal_up_end_time, record_upstart_time, record_up_end_time


tStartwithoutupload, tendwithoutupload, tstartwithupload, tendwithupload = analyzeuploadspeed()


def caculatetimefordownloads():
    obj_tstartwod = timecalculations.CalculateTime(tStartwithoutdownload)
    tstartwod = obj_tstartwod.convertEverythingIntoSeconds()
    print(tstartwod)

    obj_tendwod = timecalculations.CalculateTime(tendwithoutdownload)
    tendwod = obj_tendwod.convertEverythingIntoSeconds()
    print(tendwod)

    obj_tstartwd = timecalculations.CalculateTime(tstartwithdownload)
    tstartwd = obj_tstartwd.convertEverythingIntoSeconds()
    print(tstartwd)

    obj_tendwd = timecalculations.CalculateTime(tendwithdownload)
    tendwd = obj_tendwd.convertEverythingIntoSeconds()
    print(tendwd)
    DownloadTime = (tendwd - tstartwd)  # - (tendwod - tstartwod)

    return DownloadTime


def caculatetimeforuploads():
    obj_tstartwou = timecalculations.CalculateTime(tStartwithoutupload)
    tstartwou = obj_tstartwou.convertEverythingIntoSeconds()
    # print(tstartwou)

    obj_tendwou = timecalculations.CalculateTime(tendwithoutupload)
    tendwou = obj_tendwou.convertEverythingIntoSeconds()
    # print(tendwou)

    obj_tstartwu = timecalculations.CalculateTime(tstartwithupload)
    tstartwu = obj_tstartwu.convertEverythingIntoSeconds()
    # print(tstartwu)

    obj_tendwu = timecalculations.CalculateTime(tendwithupload)
    tendwu = obj_tendwu.convertEverythingIntoSeconds()
    # print(tendwu)
    UploadTime = (tendwu - tstartwu) - (tendwou - tstartwou)

    return UploadTime


if __name__ == '__main__':
    print(caculatetimefordownloads())
    print(caculatetimeforuploads())

app.config['DEBUG'] = True
