from pyquery import PyQuery as pq


# 解析器：whois查询
# domain: 单个域名
def parse(domain):
    # 根路径
    BASE_URL = 'http://whois.chinaz.com/'

    result = []
    try:
        result.append(domain)
        d = pq(BASE_URL + domain)
        divs = d('.WhLeList-left')
        for div in divs.items():
            if div.text() == '创建时间':
                create_time = div.next('div').text()
                result.append(create_time)
            if div.text() == '过期时间':
                deadline = div.next('div').text()
                result.append(deadline)
        if len(result) == 1:
            result.append('null')
            result.append('null')
    except:
        result.append('exception')
        result.append('exception')

    return result



