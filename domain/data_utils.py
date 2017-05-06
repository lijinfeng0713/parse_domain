# 读取文本数据并将其存入一个二维数组中
def read_data(file_path):
    with open(file_path) as file:
        result = []
        for line in file:
            # 处理读入文本结尾的换行符
            line = line.replace('\n', '')
            result.append(line)
    file.close()
    return result


# 写数据，输出处理结果
def write_data(output):
    print(output)
    out_file = open(r"final_output.txt", 'a+', encoding='utf-8')
    try:
        result = ','.join(str(i) for i in output)
        out_file.write(result + '\n')
        out_file.close()
    except:
        out_file.close()

