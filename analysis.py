import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('your_data.csv')

# 将日期列解析为日期时间格式
data['date'] = pd.to_datetime(data['date'])

# 提取月日信息
data['date'] = data['date'].dt.strftime('%m-%d')

# 按日期升序排序
data.sort_values(by='date', inplace=True)

# 计算累计值列
data['cum_climbingTime'] = data['climbingTime(min)'].cumsum()
data['cum_calories'] = data['calories(kcal)'].cumsum()
data['cum_floors'] = data['floors'].cumsum()

# 绘图
plt.figure(figsize=(10, 6))

# 绘制累计值列的曲线
plt.plot(data['date'], data['cum_climbingTime'], label='Climbing Time', marker='o')
plt.plot(data['date'], data['cum_calories'], label='Calories', marker='o')
plt.plot(data['date'], data['cum_floors'], label='Floors', marker='o')

# 绘制实际值列的曲线
plt.plot(data['date'], data['heart_rate'], c='red', label='Heart Rate', marker='o')

# 设置标题、坐标轴标签和图例
plt.title('Fitness Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# 显示数据值
for i in range(len(data)):
    plt.text(data['date'][i], data['cum_climbingTime'][i], str(data['cum_climbingTime'][i]), ha='center', va='bottom')
    plt.text(data['date'][i], data['cum_calories'][i], str(data['cum_calories'][i]), ha='center', va='bottom')
    plt.text(data['date'][i], data['cum_floors'][i], str(data['cum_floors'][i]), ha='center', va='bottom')
    plt.text(data['date'][i], data['heart_rate'][i], str(data['heart_rate'][i]), ha='center', va='bottom')

# 显示图形
plt.show()
