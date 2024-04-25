import math


def calculate_avg_err(fn):
    with open(fn, "r") as file:
        lines = file.readlines()
        err = 0
        for line in lines:
            predict, actual = line.split()
            err += abs(int(predict) - int(actual))
        return float(err) / len(lines)


# print(calculate_avg_err("gpt3.5-fine-tuning-result-american.txt"))
# print(calculate_avg_err("gpt3.5-fine-tuning-result-asian.txt"))
# print(calculate_avg_err("gpt3.5-fine-tuning-result-europe.txt"))
# print(calculate_avg_err("gpt3.5-fine-tuning-result-latin.txt"))
err_list = [calculate_avg_err("gpt3.5-fine-tuning-result-american.txt"),
            calculate_avg_err("gpt3.5-fine-tuning-result-asian.txt"),
            calculate_avg_err("gpt3.5-fine-tuning-result-europe.txt"),
            calculate_avg_err("gpt3.5-fine-tuning-result-latin.txt")
            ]
import matplotlib.pyplot as plt

# 假设有一个数据列表
data = err_list
labels = ['American', 'Asian', 'Europe', 'Latin']

# 创建条形图
plt.bar(labels, data, color='blue')  # 使用蓝色条形
# 创建条形图

# 添加标题和标签
plt.title('Bar Chart of Error and Region')
plt.xlabel('Region')
plt.ylabel('Average Error')

# 显示图表
# plt.show()
plt.savefig('error and region')