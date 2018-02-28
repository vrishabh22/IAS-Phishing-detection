#!/usr/bin/env python

import csv
#from sklearn.model_selection import train_test_split
import Feature_extraction as urlfeature

def resultwriter(feature,output_dest):
    flag=True
    with open(output_dest,'wb') as f:
        for item in feature:
            w = csv.DictWriter(f, item[1].keys())
            if flag:
                w.writeheader()
                flag=False
            w.writerow(item[1])



def process_URL_list(file_dest,output_dest):
    feature=[]
    with open(file_dest) as file:
        for line in file:
            url=line.split(',')[0].strip()
            malicious_bool=line.split(',')[1].strip()
            
            if url!='':
                print 'working on: '+url
                ret_dict=urlfeature.feature_extract(url)
                ret_dict['malicious']=malicious_bool
                feature.append([url,ret_dict]);
    resultwriter(feature,output_dest)


"""
hey!
"""

def main():
        process_URL_list('testurls.txt','op1.csv')
        
	"""
        with open('url_features.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        """
main()
