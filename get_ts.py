import json
import os
import re
import base64
import argparse
def get_ts_offset(url):
    '''given url, extract the ts offset,
    which is a number(str)
    '''
    try:
        num_str = re.search('index=([0-9]+)', url).group(1)
    except AttributeError as e:
        return -1
    return num_str
    
def write_to_ts_file(content, ts_file_name):
    '''content is base64 encoded
    decode the content to bytes and write it
    to ts_file_name
    '''
    open(ts_file_name, 'wb').write(base64.b64decode(content))
    
def har_processing(file_name_in, file_prefix_out):
    '''given input file_name, which is har archive
    write all the ts files in file_prefix_out + 'number.ts'
    '''
    with open(file_name_in, 'rb') as f:
        str = f.read().decode('utf-8')
        dic = json.loads(str)
        entries = dic['log']['entries']
        for item in entries:
            url = item['request']['url']
            if(url.find('.ts')<0):
                continue
            ts_offset = get_ts_offset(url)
            if(ts_offset == -1):
                continue
            ts_file_name = file_prefix_out + ts_offset + '.ts'
            if(os.path.exists(ts_file_name)):
                continue
            try:
                content = item['response']['content']['text']
            except KeyError as e:
                continue
            write_to_ts_file(content, ts_file_name)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--har', default='v.qq.com.har', help='har file name')
    parser.add_argument('--prefix', default = 'autism_', help='prefix of output ts file name')
    args = parser.parse_args()
    har_processing(args.har, args.prefix)