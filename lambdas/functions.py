import os
import boto3
import time

def sqs_send_message(queue_url, m_delay, m_body, m_attr):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl = queue_url,
        DelaySeconds = m_delay,
        MessageBody = m_body,
        MessageAttributes = m_attr
    )
    return response

def sqs_delete_message(queue_url, receipt_handle):
    sqs = boto3.client('sqs')
    response = sqs.delete_message(
        QueueUrl = queue_url,
        ReceiptHandle = receipt_handle
    )
    return response

def s3_put_object(bucket, key, body, acl, type):
    #print(body)
    s3 = boto3.client('s3')
    response = s3.put_object(
        Bucket = bucket,
        Key = key,
        Body = body,
        ACL = acl,
        ServerSideEncryption='AES256',
        ContentType = type
    )
    return response

def make_bucket_key(itemPath):
    if itemPath.startswith("/"):
        itemPath = itemPath[1:]
    return itemPath

# Example : cloudwatch_put_metric_data('Crawl...', 'get_sitemap', 'count', 1)
def cloudwatch_put_metric_data(Namespace, MetricName, Unit, Value):
    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.put_metric_data(
        MetricData = [{
                'Timestamp': date_timestamp(),
                'MetricName': MetricName,
                'Unit': Unit,
                'Value': Value
            }],
        Namespace = Namespace
    )
    return response

def cloudwatch_put_log_events(LOG_GROUP, LOG_STREAM, message):
    logs = boto3.client('logs')
    try:
        logs.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass
    timestamp = int(round(time.time() * 1000))
    response = logs.put_log_events(
        logGroupName=LOG_GROUP,
        logStreamName=LOG_STREAM,
        logEvents=[{'timestamp': timestamp, 'message': str(message)}]
    )
    return response

def parse_url(url):
    from urllib.parse import urlparse
    return urlparse(url)

def request_urlopen(url):
    import urllib.request
    try:
        content = urllib.request.urlopen(url)
        return content
    except urllib.error.HTTPError as e:
        return 'error: '+str(e.code)

def read_site_map(host, sitemap):
    import http.client
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/"+str(sitemap), headers={"Host": host})
    response = conn.getresponse()
    xml_content = response.read().decode('utf-8')
    return xml_content

def parse_xml(xml_content):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_content)
    return root

def get_urls(content, type):
    urls = []
    for url in content.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}'+type):
        urls.append(url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text)
    return urls

def md5_string(loc):
    import hashlib
    hash_md5 = hashlib.md5()
    hash_md5.update(loc.encode('utf-8'))
    md5_result = hash_md5.hexdigest()
    return md5_result

def date_now():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("Europe/Paris"))
    date_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return date_now

def date_timestamp():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    now = datetime.now()
    return now