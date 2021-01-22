import argparse
import os
from os import path
import csv
from pyisemail import is_email
import pandas as pd


def normalize(row):
    for k in row.keys():
        row[k] = row[k].strip()
    return row

def valid(row, diagnose=False):
    fn = row["First Name"]
    ln = row["Last Name"]
    e = row["Email"].lower()
    if fn == "" or ln == "" or e == "":
        return False
    if not is_email(e):
        if diagnose is True:
            diag = is_email(e, diagnose=True)
            print("bad_email: {}, diagnoses: {}".format(e, diag))
        return False
    return True

parser = argparse.ArgumentParser(description='chimport takes an excel spread sheet, normalizes the data, and uploads it to mail chimp')
parser.add_argument('fileimport')
parser.add_argument('--errors', required=False)
parser.add_argument('--export', required=False)
args = parser.parse_args()

if path.exists(args.fileimport) == False:
    print('Whoopsies! We could not find the file you provided: {}'.format(args.fileimport))
    exit(0)

data = list()

headers = list()

with open(args.fileimport) as csvfile:
    recs = csv.DictReader(csvfile)
    headers = recs.fieldnames
    for rec in recs:
        row = normalize(rec)
        data.append(row)

fields = ["Tax", "First Name", "Last Name", "DOB", "Title", "Company", "Created At", "Address1", "Address2", "City", "State", "ZIP", "Country", "Home", "Work", "Mobile", "Email", "Email2"]

dropfields = list(set(headers) - set(fields))

validdata = [x for x in data if valid(x)]
errordata = [x for x in data if not valid(x)]

vd = pd.DataFrame(validdata)
ed = pd.DataFrame(errordata)

vd = vd.drop(dropfields, axis=1)
ed = ed.drop(dropfields, axis=1)

vdcsv = vd.to_csv(index=False)
edcsv = vd.to_csv(index=False)

print(vdcsv, edcsv)