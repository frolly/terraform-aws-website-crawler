from functions import *

def init(event, context):
   xml_content = read_site_map(os.environ['website_domain_name'], os.environ['website_sitemap_index'])
   print(str(xml_content))
   
   content = parse_xml(xml_content)
   print(str(content))

   if 'urlset' not in str(content):
      urls = get_urls(content, 'sitemap')
      print('not in urlset: '+str(urls))
      i = 0
      for url in urls:
         i += 1
         print(url)
         m_attr = {}
         m_attr['SitemapId'] = {'DataType': 'String', 'StringValue': md5_string(url)}
         m_attr['Url'] = {'DataType': 'String', 'StringValue': url}
         m_attr['DateTreat'] = {'DataType': 'String', 'StringValue': date_now()}
         sqs_send_message(os.environ['sqs_website_sitemaps'], int(10 + i), url, m_attr)
         cloudwatch_put_log_events(os.environ['cw_log_group_sitemaps'], str(time.strftime('%Y-%m-%d')), url+' -> in SQS')
         cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'get_sitemap_index', 'Count', 1)
      cloudwatch_put_log_events(os.environ['cw_log_group_domain'], 'history', 'get_sitemaps: '+str(i))
   else:
      urls = get_urls(content, 'url')
      print('in urlset: '+str(urls))
      i = 0
      for url in urls:
         i += 1
         print(url)
         m_attr = {}
         m_attr['UrlId'] = {'DataType': 'String', 'StringValue': md5_string(url)}
         m_attr['Url'] = {'DataType': 'String', 'StringValue': url}
         m_attr['DateTreat'] = {'DataType': 'String', 'StringValue': date_now()}
         sqs_send_message(os.environ['sqs_website_pages'], int(10 + i), url, m_attr)
         cloudwatch_put_log_events(os.environ['cw_log_group_get_urls'], str(time.strftime('%Y-%m-%d')), url+' -> in SQS')
         cloudwatch_put_metric_data('Crawl_'+os.environ['cw_log_group_domain'], 'get_sitemap_urls', 'Count', 1)
      cloudwatch_put_log_events(os.environ['cw_log_group_domain'], 'history', 'get_sitemaps: '+str(i))
   return {
      'statusCode': 200,
      'body': 'count sitemaps: '+str(i)
   }
