from functions import *

def init(event, context):
    if 'Records' in event:
        if 'messageAttributes' in event['Records'][0]:
            Url         = event['Records'][0]['messageAttributes']['Url']['stringValue']
            SitemapId  = event['Records'][0]['messageAttributes']['SitemapId']['stringValue']
            DateTreat     = event['Records'][0]['messageAttributes']['DateTreat']['stringValue']
    else:
        Url         = event['Url']
        SitemapId   = event['SitemapId']
        DateTreat   = event['DateTreat']
    
    item = parse_url(Url)
    xml_content = read_site_map(item.netloc, item.path)
    content = parse_xml(xml_content)

    urls = get_urls(content, 'url')
    i = 0
    for url in urls:
        i += 1
        print(url)
        m_attr = {}
        m_attr['UrlId'] = {'DataType': 'String', 'StringValue': md5_string(url)}
        m_attr['Url'] = {'DataType': 'String', 'StringValue': url}
        m_attr['DateTreat'] = {'DataType': 'String', 'StringValue': date_now()}
        sqs_send_message(os.environ['sqs_website_pages'], int(10 + round(i / 10, 0)), url, m_attr)
        cloudwatch_put_log_events(os.environ['cw_log_group_get_urls'], str(time.strftime('%Y-%m-%d')), url+' -> in SQS')
        cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'get_urls', 'Count', 1)
    cloudwatch_put_log_events(os.environ['cw_log_group_domain'], 'history', 'get_urls: '+str(i))

    if 'Records' in event:
        if 'ReceiptHandle' in event['Records'][0]:
            sqs_delete_message(os.environ['sqs_website_sitemaps'], event['Records'][0]['ReceiptHandle'])

    return {
        'statusCode': 200,
        'body': 'count urls: '+str(i)
    }