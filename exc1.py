import requests
import csv
from bs4 import BeautifulSoup

# 发送HTTP请求获取链接页面内容
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, "html.parser")

# 查找表格
table = soup.find("div")
if table is None:
    print("无法找到表格")
else:
    # 提取表格行
    table_rows = table.find_all("tr")

    # 创建数据列表
    data = []

    # 遍历表格行
    for row in table_rows:
        # 提取表格单元格
        cells = row.find_all("td")

        # 确保表格行有足够的单元格
        if len(cells) >= 6:
            # 获取单元格数据
            isin = cells[0].text.strip()
            bond_code = cells[1].text.strip()
            issuer = cells[2].text.strip()
            bond_type = cells[3].text.strip()
            issue_date = cells[4].text.strip()
            latest_rating = cells[5].text.strip()

            # 检查条件是否满足
            if bond_type == "Treasury Bond" and "2023" in issue_date:
                # 将数据添加到列表
                data.append([isin, bond_code, issuer, bond_type, issue_date, latest_rating])

    # 保存为CSV文件
    filename = "treasury_bonds_2023.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # 写入列名
        writer.writerow(["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"])

        # 写入数据
        writer.writerows(data)

    print("数据已保存为", filename)