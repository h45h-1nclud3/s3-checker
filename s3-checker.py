import requests
import sys




if len(sys.argv) >= 2:


    s3_regions = ['s3-website.us-east-2.amazonaws.com', 's3-website.us-east-1.amazonaws.com', 's3-website.us-west-1.amazonaws.com', 's3-website.us-west-2.amazonaws.com', 's3-website.ap-east-1.amazonaws.com', 's3-website.ap-south-1.amazonaws.com', 's3-website.ap-northeast-3.amazonaws.com', 's3-website.ap-northeast-2.amazonaws.com', 's3-website.ap-southeast-1.amazonaws.com', 's3-website.ap-southeast-2.amazonaws.com', 's3-website.ap-northeast-1.amazonaws.com', 's3-website.ca-central-1.amazonaws.com', 's3-website.cn-north-1.amazonaws.com.cn', 's3-website.cn-northwest-1.amazonaws.com.cn', 's3-website.eu-central-1.amazonaws.com', 's3-website.eu-west-1.amazonaws.com', 's3-website.eu-west-2.amazonaws.com', 's3-website.eu-west-3.amazonaws.com', 's3-website.eu-north-1.amazonaws.com', 's3-website.me-south-1.amazonaws.com', 's3-website.sa-east-1.amazonaws.com', 's3-website.us-gov-east-1.amazonaws.com', 's3-website.us-gov-west-1.amazonaws.com']



    for region in s3_regions:
        res = requests.get("http://" + sys.argv[1] + "." + region)
        if res.status_code == 200:
            print("Domain Found in " + region + " !")
            print("=====> URL : " + "http://" + sys.argv[1] + "." + region)
            
else:
    print("Usage : python3 s3-checker.py <Domain>")
