import paramiko
import glob
import csv
from pymongo import MongoClient

'''
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='',username='',password='')
ftp_client=ssh_client.open_sftp()
ftp_client.get('C:\\Users\\ramarajd\\Documents\\first_data.csv','C:\\Users\\ramarajd\\Documents\\')
ftp_client.close()
'''
path = r'C:\Users\ramarajd\Desktop'
all_files = glob.glob(path + "\*.csv")

for filename in all_files:
    print(filename)
    csvfile = open(filename, 'r')
    reader = csv.DictReader(csvfile)
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.collect_csv_files
    db.segment.drop()
    header = ["Series_reference","Period"]
    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        db.segment.insert_one(row)
