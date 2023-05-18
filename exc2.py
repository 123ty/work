import csv

# 读取CSV文件
with open('C:/Users/Administrator/Desktop/fyx_chinamoney.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行
    code_list = [int(row[0]) for row in reader]  # 获取第一列数据

# 每80个元素为一批次，拆分成多个数组
batch_size = 80
batch_list = [code_list[i:i+batch_size] for i in range(0, len(code_list), batch_size)]

# 打印输出每个批次的数组
for i, batch in enumerate(batch_list):
    print(f"Batch {i+1}: {batch}")