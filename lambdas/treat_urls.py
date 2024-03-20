from functions import *

def init(event, context):
    if 'Records' in event:
        if 'messageAttributes' in event['Records'][0]:
            Url         = event['Records'][0]['messageAttributes']['Url']['stringValue']
            UrlId       = event['Records'][0]['messageAttributes']['UrlId']['stringValue']
            DateTreat   = event['Records'][0]['messageAttributes']['DateTreat']['stringValue']
    else:
        Url         = event['Url']
        UrlId       = event['UrlId']
        DateTreat   = event['DateTreat']

    item = parse_url(Url)
    itemPath = item.path
    if item.path == '' or item.path == '/':
        itemPath = '/index.html'
    else:
        if not item.path.endswith('.html'):
            itemPath = item.path + '/index.html'
    
    start = time.time()
    response = request_urlopen(Url)
    print('urlopen response: '+Url+' / '+str(response))
    end = time.time()
    print(type(response))
    if type(response) is str:
        print('GET CODE DIFF 200 !!!')
        cloudwatch_put_log_events(os.environ['cw_log_group_err_urls'], str(time.strftime('%Y-%m-%d')), Url+' ('+str(response)+')')
        cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'treat_urls_not_200', 'Count', 1)
        # PUT IN SQS QUEUE URL TO RE TREATED
    else:
        if response.getcode() == 200:
            s3_response = s3_put_object(os.environ['bucket_website_pages'], make_bucket_key(itemPath), response.read(), 'public-read', 'text/html')
            cloudwatch_put_log_events(os.environ['cw_log_group_put_urls'], str(time.strftime('%Y-%m-%d')), Url+' ('+str(response.getcode())+') ('+str(round(end - start, 3))+') -> in S3')
            cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'treat_urls_200', 'Count', 1)
            if 'Records' in event:
                if 'ReceiptHandle' in event['Records'][0]:
                    sqs_delete_message(os.environ['sqs_website_pages'], event['Records'][0]['ReceiptHandle'])
        else:
            print('GET CODE DIFF 200 !!!')
            cloudwatch_put_log_events(os.environ['cw_log_group_err_urls'], str(time.strftime('%Y-%m-%d')), Url+' ('+str(response)+') -> error')
            cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'treat_urls_error', 'Count', 1)
            # PUT IN SQS QUEUE URL TO RE TREATED

    
    return {
        'statusCode': 200,
        'body': 'Done...'
    }