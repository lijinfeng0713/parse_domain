from domain.domain import parser
from domain.domain import data_utils as util
from multiprocessing.dummy import Pool as ProcessPool


if __name__ == '__main__':
    print('开始读数据……')
    domains_list = util.read_data("test.txt")
    print('数据读写完毕，开始处理……')
    pool = ProcessPool(20)
    # 解析数据集中前50000个域名
    domains = domains_list[0:50000]
    for domain in domains:
        pool.apply_async(parser.parse, (domain,), callback=util.write_data)
    pool.close()
    pool.join()
    print('数据解析完成')


