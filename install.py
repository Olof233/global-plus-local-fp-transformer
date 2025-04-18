# 打开txt文件并读取每一行
with open(r'MSU-LatentAFIS\latentafis.yml', 'r') as file:
    lines = file.readlines()

# 处理每一行
with open(r'MSU-LatentAFIS\latentafis2.yml', 'w') as file:
    for line in lines[7:157]:
        # 如果行以'pypi_0'结尾，则注释这一行
        newline1 = line.split('=')[0]
        newline2 = newline1.split('-', 1)[1]
        newline3 = newline2.strip(' ') + ' '
        file.write(newline3)
