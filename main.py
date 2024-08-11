# 普通交互式折线图：
import csv
import matplotlib.pyplot as plt
import mplcursors
import math

# Example unordered data pairs
times = ['0', '1.015', '1.999', '2.993', '4', '5.02', '6.001', '7.006', '7.997', '9.002', '10.025', '11.015', '12.01',
         '13.013', '14.008', '15.011', '16.017', '17.008', '18.014', '20.016', '21.039', '22.997']
times = [float(x) for x in times]
data_values = ['36.0', '22.0', '34.0', '36.0', '27.0', '36.0', '84.0', '88.0', '76.0', '84.0', '88.0', '78.0', '87.0',
               '81.0', '82.0', '87.0', '110.0', '108.0', '105.0', '116.0', '117.0', '26.0']
data_values = [float(x) for x in data_values]

plt.plot(times, data_values, marker='o', linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Manual Scaling')
plt.legend('Line Plot label')

plt.grid(True)
plt.tight_layout()
cursor = mplcursors.cursor(hover=True)


@cursor.connect("add")
def on_hover(sel):
    index = sel.target.index
    x = times[index]
    y = data_values[index]
    sel.annotation.set_text(f'Time: {x}, Value: {y}')


plt.show()

# 输入模拟数据
# 一共最多学习10次，最多生成10组数据：
# 第一组模拟数据(假设采集到的是31个点（每组数据可能稍有增加可能减少，模拟现实情况），按照1秒1个记录，最后一个时间值进1取整）：

# 第二组模拟数据：
times1 = []
data_values1 = []
# 第二组模拟数据：
times2 = []
data_values2 = []
# 第三组模拟数据：
times3 = []
data_values3 = []
# 第四组模拟数据：
times4 = []
data_values4 = []
# 第五组模拟数据：
times5 = []
data_values5 = []
# 第六组模拟数据：
times6 = []
data_values6 = []
# 第七组模拟数据：
times7 = []
data_values7 = []
# 第八组模拟数据：
times8 = []
data_values8 = []
# 第九组模拟数据：
times9 = []
data_values9 = []
# 第十组模拟数据：
times10 = []
data_values10 = []
# 第十一组模拟数据：
times11 = []
data_values11 = []
# Open the CSV file
with open('/Users/xieqingyu/Desktop/清洗过的数据.csv', mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[4] == "1":
            times1.append(row[1])
            data_values1.append(row[2])

        if row[4] == "2":
            times2.append(row[1])
            data_values2.append(row[2])

        if row[4] == "3":
            times3.append(row[1])
            data_values3.append(row[2])

        if row[4] == "4":
            times4.append(row[1])
            data_values4.append(row[2])

        if row[4] == "5":
            times5.append(row[1])
            data_values5.append(row[2])

        if row[4] == "6":
            times6.append(row[1])
            data_values6.append(row[2])

        if row[4] == "7":
            times7.append(row[1])
            data_values7.append(row[2])

        if row[4] == "8":
            times8.append(row[1])
            data_values8.append(row[2])

        if row[4] == "9":
            times9.append(row[1])
            data_values9.append(row[2])

        if row[4] == "10":
            times10.append(row[1])
            data_values10.append(row[2])

        if row[4] == "11":
            times11.append(row[1])
            data_values11.append(row[2])


# 求任意两个整数左开右开间的所有整数：
def integers_in_range_open(start, end):
    return [i for i in range(start + 1, end)]


# 求任意两个整数左闭右闭间的所有整数：
def integers_in_range_close(start, end):
    return [i for i in range(start, end + 1)]


# 求任意两个整数左开右闭间的所有整数：
def integers_in_range(start, end):
    return [i for i in range(start + 1, end + 1)]


# 求任意两个整数左闭右开间的所有整数：
def integers_in_range_inverse(start, end):
    return [i for i in range(start, end)]


# 对齐点斜式方法：
def slope_intercept(x_new, x1, y1, x2, y2):
    return round(y1 + (x_new - x1) * ((y2 - y1) / (x2 - x1)), 3)


# 第一组模拟数据string转numbers：
times1 = [float(x) for x in times1]
data_values1 = [float(y) for y in data_values1]
for i in range(0, len(times1)):
    if times1[i] - math.floor(times1[i]) == 0:
        times1[i] = int(times1[i])

for i in range(0, len(data_values1)):
    if data_values1[i] - math.floor(data_values1[i]) == 0:
        data_values1[i] = int(data_values1[i])
# 第一组模拟数据对齐：
times1_final = []
data_values1_final = []
for i in range(0, len(times1) - 1):
    if isinstance(times1[i], int) and isinstance(times1[i + 1], int):
        times1_final.append(times1[i])
        data_values1_final.append(data_values1[i])
        for j in integers_in_range_open(times1[i], times1[i + 1]):
            times1_final.append(j)
            data_values1_final.append(
                slope_intercept(j, times1[i], data_values1[i], times1[i + 1], data_values1[i + 1]))
    elif isinstance(times1[i], float) and isinstance(times1[i + 1], float):
        for k in integers_in_range_close(math.ceil(times1[i]), math.floor(times1[i + 1])):
            if math.ceil(times1[i]) <= math.floor(times1[i + 1]):
                times1_final.append(k)
                data_values1_final.append(
                    slope_intercept(k, times1[i], data_values1[i], times1[i + 1], data_values1[i + 1]))
    elif isinstance(times1[i], float) and isinstance(times1[i + 1], int):
        if times1[i + 1] - times1[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times1[i]), times1[i + 1]):
                times1_final.append(p)
                data_values1_final.append(
                    slope_intercept(p, times1[i], data_values1[i], times1[i + 1], data_values1[i + 1]))
    elif isinstance(times1[i], int) and isinstance(times1[i + 1], float):
        times1_final.append(times1[i])
        data_values1_final.append(data_values1[i])
        if times1[i + 1] - times1[i] > 1:
            for o in integers_in_range(times1[i], math.floor(times1[i + 1])):
                times1_final.append(o)
                data_values1_final.append(
                    slope_intercept(o, times1[i], data_values1[i], times1[i + 1], data_values1[i + 1]))
times1_final.append(times1[-1])
data_values1_final.append(data_values1[-1])

print(times1_final)
print(data_values1_final)

# 第二组模拟数据string转numbers：
times2 = [float(x) for x in times2]
data_values2 = [float(y) for y in data_values2]
for i in range(0, len(times2)):
    if times2[i] - math.floor(times2[i]) == 0:
        times2[i] = int(times2[i])

for i in range(0, len(data_values2)):
    if data_values2[i] - math.floor(data_values2[i]) == 0:
        data_values2[i] = int(data_values2[i])
# 第二组模拟数据对齐：
times2_final = []
data_values2_final = []
for i in range(0, len(times2) - 1):
    if isinstance(times2[i], int) and isinstance(times2[i + 1], int):
        times2_final.append(times2[i])
        data_values2_final.append(data_values2[i])
        for j in integers_in_range_open(times2[i], times2[i + 1]):
            times2_final.append(j)
            data_values2_final.append(
                slope_intercept(j, times2[i], data_values2[i], times2[i + 1], data_values2[i + 1]))
    elif isinstance(times2[i], float) and isinstance(times2[i + 1], float):
        for k in integers_in_range_close(math.ceil(times2[i]), math.floor(times2[i + 1])):
            if math.ceil(times2[i]) <= math.floor(times2[i + 1]):
                times2_final.append(k)
                data_values2_final.append(
                    slope_intercept(k, times2[i], data_values2[i], times2[i + 1], data_values2[i + 1]))
    elif isinstance(times2[i], float) and isinstance(times2[i + 1], int):
        if times2[i + 1] - times2[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times2[i]), times2[i + 1]):
                times2_final.append(p)
                data_values2_final.append(
                    slope_intercept(p, times2[i], data_values2[i], times2[i + 1], data_values2[i + 1]))
    elif isinstance(times2[i], int) and isinstance(times2[i + 1], float):
        times2_final.append(times2[i])
        data_values2_final.append(data_values2[i])
        if times2[i + 1] - times2[i] > 1:
            for o in integers_in_range(times2[i], math.floor(times2[i + 1])):
                times2_final.append(o)
                data_values2_final.append(
                    slope_intercept(o, times2[i], data_values2[i], times2[i + 1], data_values2[i + 1]))
times2_final.append(times2[-1])
data_values2_final.append(data_values2[-1])

print(times2_final)
print(data_values2_final)

# 第三组模拟数据string转numbers：
times3 = [float(x) for x in times3]
data_values3 = [float(y) for y in data_values3]
for i in range(0, len(times3)):
    if times3[i] - math.floor(times3[i]) == 0:
        times3[i] = int(times3[i])

for i in range(0, len(data_values3)):
    if data_values3[i] - math.floor(data_values3[i]) == 0:
        data_values3[i] = int(data_values3[i])
# 第三组模拟数据对齐：
times3_final = []
data_values3_final = []
for i in range(0, len(times3) - 1):
    if isinstance(times3[i], int) and isinstance(times3[i + 1], int):
        times3_final.append(times3[i])
        data_values3_final.append(data_values3[i])
        for j in integers_in_range_open(times3[i], times3[i + 1]):
            times3_final.append(j)
            data_values3_final.append(
                slope_intercept(j, times3[i], data_values3[i], times3[i + 1], data_values3[i + 1]))
    elif isinstance(times3[i], float) and isinstance(times3[i + 1], float):
        for k in integers_in_range_close(math.ceil(times3[i]), math.floor(times3[i + 1])):
            if math.ceil(times3[i]) <= math.floor(times3[i + 1]):
                times3_final.append(k)
                data_values3_final.append(
                    slope_intercept(k, times3[i], data_values3[i], times3[i + 1], data_values3[i + 1]))
    elif isinstance(times3[i], float) and isinstance(times3[i + 1], int):
        if times3[i + 1] - times3[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times3[i]), times3[i + 1]):
                times3_final.append(p)
                data_values3_final.append(
                    slope_intercept(p, times3[i], data_values3[i], times3[i + 1], data_values3[i + 1]))
    elif isinstance(times3[i], int) and isinstance(times3[i + 1], float):
        times3_final.append(times3[i])
        data_values3_final.append(data_values3[i])
        if times3[i + 1] - times3[i] > 1:
            for o in integers_in_range(times3[i], math.floor(times3[i + 1])):
                times3_final.append(o)
                data_values3_final.append(
                    slope_intercept(o, times3[i], data_values3[i], times3[i + 1], data_values3[i + 1]))
times3_final.append(times3[-1])
data_values3_final.append(data_values3[-1])

print(times3_final)
print(data_values3_final)

# 第四组模拟数据string转numbers：
times4 = [float(x) for x in times4]
data_values4 = [float(y) for y in data_values4]
for i in range(0, len(times4)):
    if times4[i] - math.floor(times4[i]) == 0:
        times4[i] = int(times4[i])

for i in range(0, len(data_values4)):
    if data_values4[i] - math.floor(data_values4[i]) == 0:
        data_values4[i] = int(data_values4[i])
# 第四组模拟数据对齐：
times4_final = []
data_values4_final = []
for i in range(0, len(times4) - 1):
    if isinstance(times4[i], int) and isinstance(times4[i + 1], int):
        times1_final.append(times4[i])
        data_values1_final.append(data_values4[i])
        for j in integers_in_range_open(times4[i], times4[i + 1]):
            times4_final.append(j)
            data_values4_final.append(
                slope_intercept(j, times4[i], data_values4[i], times4[i + 1], data_values4[i + 1]))
    elif isinstance(times4[i], float) and isinstance(times4[i + 1], float):
        for k in integers_in_range_close(math.ceil(times4[i]), math.floor(times4[i + 1])):
            if math.ceil(times4[i]) <= math.floor(times4[i + 1]):
                times4_final.append(k)
                data_values4_final.append(
                    slope_intercept(k, times4[i], data_values4[i], times4[i + 1], data_values4[i + 1]))
    elif isinstance(times4[i], float) and isinstance(times4[i + 1], int):
        if times4[i + 1] - times4[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times4[i]), times4[i + 1]):
                times4_final.append(p)
                data_values4_final.append(
                    slope_intercept(p, times4[i], data_values4[i], times4[i + 1], data_values4[i + 1]))
    elif isinstance(times4[i], int) and isinstance(times4[i + 1], float):
        times4_final.append(times4[i])
        data_values4_final.append(data_values4[i])
        if times4[i + 1] - times4[i] > 1:
            for o in integers_in_range(times4[i], math.floor(times4[i + 1])):
                times4_final.append(o)
                data_values4_final.append(
                    slope_intercept(o, times4[i], data_values4[i], times4[i + 1], data_values4[i + 1]))
times4_final.append(times4[-1])
data_values4_final.append(data_values4[-1])

print(times4_final)
print(data_values4_final)

# 第五组模拟数据string转numbers：
times5 = [float(x) for x in times5]
data_values5 = [float(y) for y in data_values5]
for i in range(0, len(times5)):
    if times5[i] - math.floor(times5[i]) == 0:
        times5[i] = int(times5[i])

for i in range(0, len(data_values5)):
    if data_values5[i] - math.floor(data_values5[i]) == 0:
        data_values5[i] = int(data_values5[i])
# 第五组模拟数据对齐：
times5_final = []
data_values5_final = []
for i in range(0, len(times5) - 1):
    if isinstance(times5[i], int) and isinstance(times5[i + 1], int):
        times5_final.append(times5[i])
        data_values5_final.append(data_values5[i])
        for j in integers_in_range_open(times5[i], times5[i + 1]):
            times5_final.append(j)
            data_values5_final.append(
                slope_intercept(j, times5[i], data_values5[i], times5[i + 1], data_values5[i + 1]))
    elif isinstance(times5[i], float) and isinstance(times5[i + 1], float):
        for k in integers_in_range_close(math.ceil(times5[i]), math.floor(times5[i + 1])):
            if math.ceil(times5[i]) <= math.floor(times5[i + 1]):
                times5_final.append(k)
                data_values5_final.append(
                    slope_intercept(k, times5[i], data_values5[i], times5[i + 1], data_values5[i + 1]))
    elif isinstance(times5[i], float) and isinstance(times5[i + 1], int):
        if times5[i + 1] - times5[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times5[i]), times5[i + 1]):
                times5_final.append(p)
                data_values5_final.append(
                    slope_intercept(p, times5[i], data_values5[i], times5[i + 1], data_values5[i + 1]))
    elif isinstance(times5[i], int) and isinstance(times5[i + 1], float):
        times5_final.append(times5[i])
        data_values5_final.append(data_values5[i])
        if times5[i + 1] - times5[i] > 1:
            for o in integers_in_range(times5[i], math.floor(times5[i + 1])):
                times5_final.append(o)
                data_values5_final.append(
                    slope_intercept(o, times5[i], data_values5[i], times5[i + 1], data_values5[i + 1]))
times5_final.append(times5[-1])
data_values5_final.append(data_values5[-1])

print(times5_final)
print(data_values5_final)

# 第六组模拟数据string转numbers：
times6 = [float(x) for x in times6]
data_values6 = [float(y) for y in data_values6]
for i in range(0, len(times6)):
    if times6[i] - math.floor(times6[i]) == 0:
        times6[i] = int(times6[i])

for i in range(0, len(data_values6)):
    if data_values6[i] - math.floor(data_values6[i]) == 0:
        data_values6[i] = int(data_values6[i])
# 第六组模拟数据对齐：
times6_final = []
data_values6_final = []
for i in range(0, len(times6) - 1):
    if isinstance(times6[i], int) and isinstance(times6[i + 1], int):
        times6_final.append(times6[i])
        data_values6_final.append(data_values6[i])
        for j in integers_in_range_open(times6[i], times6[i + 1]):
            times6_final.append(j)
            data_values6_final.append(
                slope_intercept(j, times6[i], data_values6[i], times6[i + 1], data_values6[i + 1]))
    elif isinstance(times6[i], float) and isinstance(times6[i + 1], float):
        for k in integers_in_range_close(math.ceil(times6[i]), math.floor(times6[i + 1])):
            if math.ceil(times6[i]) <= math.floor(times6[i + 1]):
                times6_final.append(k)
                data_values6_final.append(
                    slope_intercept(k, times6[i], data_values6[i], times6[i + 1], data_values6[i + 1]))
    elif isinstance(times6[i], float) and isinstance(times6[i + 1], int):
        if times6[i + 1] - times6[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times6[i]), times6[i + 1]):
                times6_final.append(p)
                data_values6_final.append(
                    slope_intercept(p, times6[i], data_values6[i], times6[i + 1], data_values6[i + 1]))
    elif isinstance(times6[i], int) and isinstance(times6[i + 1], float):
        times6_final.append(times6[i])
        data_values6_final.append(data_values6[i])
        if times6[i + 1] - times6[i] > 1:
            for o in integers_in_range(times6[i], math.floor(times6[i + 1])):
                times6_final.append(o)
                data_values6_final.append(
                    slope_intercept(o, times6[i], data_values6[i], times6[i + 1], data_values6[i + 1]))
times6_final.append(times6[-1])
data_values6_final.append(data_values6[-1])

print(times6_final)
print(data_values6_final)

# 第七组模拟数据string转numbers：
times7 = [float(x) for x in times7]
data_values7 = [float(y) for y in data_values7]
for i in range(0, len(times7)):
    if times7[i] - math.floor(times7[i]) == 0:
        times7[i] = int(times7[i])

for i in range(0, len(data_values7)):
    if data_values7[i] - math.floor(data_values7[i]) == 0:
        data_values7[i] = int(data_values7[i])
# 第七组模拟数据对齐：
times7_final = []
data_values7_final = []
for i in range(0, len(times7) - 1):
    if isinstance(times7[i], int) and isinstance(times7[i + 1], int):
        times7_final.append(times7[i])
        data_values7_final.append(data_values7[i])
        for j in integers_in_range_open(times7[i], times7[i + 1]):
            times7_final.append(j)
            data_values7_final.append(
                slope_intercept(j, times7[i], data_values7[i], times7[i + 1], data_values7[i + 1]))
    elif isinstance(times7[i], float) and isinstance(times7[i + 1], float):
        for k in integers_in_range_close(math.ceil(times7[i]), math.floor(times7[i + 1])):
            if math.ceil(times7[i]) <= math.floor(times7[i + 1]):
                times7_final.append(k)
                data_values7_final.append(
                    slope_intercept(k, times7[i], data_values7[i], times7[i + 1], data_values7[i + 1]))
    elif isinstance(times7[i], float) and isinstance(times7[i + 1], int):
        if times7[i + 1] - times7[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times7[i]), times7[i + 1]):
                times7_final.append(p)
                data_values7_final.append(
                    slope_intercept(p, times7[i], data_values7[i], times7[i + 1], data_values7[i + 1]))
    elif isinstance(times7[i], int) and isinstance(times7[i + 1], float):
        times7_final.append(times7[i])
        data_values7_final.append(data_values7[i])
        if times7[i + 1] - times7[i] > 1:
            for o in integers_in_range(times7[i], math.floor(times7[i + 1])):
                times7_final.append(o)
                data_values7_final.append(
                    slope_intercept(o, times7[i], data_values7[i], times7[i + 1], data_values7[i + 1]))
times7_final.append(times7[-1])
data_values7_final.append(data_values7[-1])

print(times7_final)
print(data_values7_final)

# 第八组模拟数据string转numbers：
times8 = [float(x) for x in times8]
data_values8 = [float(y) for y in data_values8]
for i in range(0, len(times8)):
    if times8[i] - math.floor(times8[i]) == 0:
        times8[i] = int(times8[i])

for i in range(0, len(data_values8)):
    if data_values8[i] - math.floor(data_values8[i]) == 0:
        data_values8[i] = int(data_values8[i])
# 第八组模拟数据对齐：
times8_final = []
data_values8_final = []
for i in range(0, len(times8) - 1):
    if isinstance(times8[i], int) and isinstance(times8[i + 1], int):
        times8_final.append(times8[i])
        data_values8_final.append(data_values8[i])
        for j in integers_in_range_open(times8[i], times8[i + 1]):
            times8_final.append(j)
            data_values8_final.append(
                slope_intercept(j, times8[i], data_values8[i], times8[i + 1], data_values8[i + 1]))
    elif isinstance(times8[i], float) and isinstance(times8[i + 1], float):
        for k in integers_in_range_close(math.ceil(times8[i]), math.floor(times8[i + 1])):
            if math.ceil(times8[i]) <= math.floor(times8[i + 1]):
                times8_final.append(k)
                data_values8_final.append(
                    slope_intercept(k, times8[i], data_values8[i], times8[i + 1], data_values8[i + 1]))
    elif isinstance(times8[i], float) and isinstance(times8[i + 1], int):
        if times8[i + 1] - times8[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times8[i]), times8[i + 1]):
                times8_final.append(p)
                data_values8_final.append(
                    slope_intercept(p, times8[i], data_values8[i], times8[i + 1], data_values8[i + 1]))
    elif isinstance(times8[i], int) and isinstance(times8[i + 1], float):
        times8_final.append(times8[i])
        data_values8_final.append(data_values8[i])
        if times8[i + 1] - times8[i] > 1:
            for o in integers_in_range(times8[i], math.floor(times8[i + 1])):
                times8_final.append(o)
                data_values8_final.append(
                    slope_intercept(o, times8[i], data_values8[i], times8[i + 1], data_values8[i + 1]))
times8_final.append(times8[-1])
data_values8_final.append(data_values8[-1])

print(times8_final)
print(data_values8_final)

# 第九组模拟数据string转numbers：
times9 = [float(x) for x in times9]
data_values9 = [float(y) for y in data_values9]
for i in range(0, len(times9)):
    if times9[i] - math.floor(times9[i]) == 0:
        times9[i] = int(times9[i])

for i in range(0, len(data_values9)):
    if data_values9[i] - math.floor(data_values9[i]) == 0:
        data_values9[i] = int(data_values9[i])
# 第九组模拟数据对齐：
times9_final = []
data_values9_final = []
for i in range(0, len(times9) - 1):
    if isinstance(times9[i], int) and isinstance(times9[i + 1], int):
        times9_final.append(times9[i])
        data_values9_final.append(data_values9[i])
        for j in integers_in_range_open(times9[i], times9[i + 1]):
            times9_final.append(j)
            data_values9_final.append(
                slope_intercept(j, times9[i], data_values9[i], times9[i + 1], data_values9[i + 1]))
    elif isinstance(times9[i], float) and isinstance(times9[i + 1], float):
        for k in integers_in_range_close(math.ceil(times9[i]), math.floor(times9[i + 1])):
            if math.ceil(times9[i]) <= math.floor(times9[i + 1]):
                times9_final.append(k)
                data_values9_final.append(
                    slope_intercept(k, times9[i], data_values9[i], times9[i + 1], data_values9[i + 1]))
    elif isinstance(times9[i], float) and isinstance(times9[i + 1], int):
        if times9[i + 1] - times9[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times9[i]), times9[i + 1]):
                times9_final.append(p)
                data_values9_final.append(
                    slope_intercept(p, times9[i], data_values9[i], times9[i + 1], data_values9[i + 1]))
    elif isinstance(times9[i], int) and isinstance(times9[i + 1], float):
        times9_final.append(times9[i])
        data_values9_final.append(data_values9[i])
        if times9[i + 1] - times9[i] > 1:
            for o in integers_in_range(times9[i], math.floor(times9[i + 1])):
                times9_final.append(o)
                data_values9_final.append(
                    slope_intercept(o, times9[i], data_values9[i], times9[i + 1], data_values9[i + 1]))
times9_final.append(times9[-1])
data_values9_final.append(data_values9[-1])

print(times9_final)
print(data_values9_final)

# 第十组模拟数据string转numbers：
times10 = [float(x) for x in times10]
data_values10 = [float(y) for y in data_values10]
for i in range(0, len(times10)):
    if times10[i] - math.floor(times10[i]) == 0:
        times10[i] = int(times10[i])

for i in range(0, len(data_values10)):
    if data_values10[i] - math.floor(data_values10[i]) == 0:
        data_values10[i] = int(data_values10[i])
# 第十组模拟数据对齐：
times10_final = []
data_values10_final = []
for i in range(0, len(times10) - 1):
    if isinstance(times10[i], int) and isinstance(times10[i + 1], int):
        times10_final.append(times10[i])
        data_values10_final.append(data_values10[i])
        for j in integers_in_range_open(times10[i], times10[i + 1]):
            times10_final.append(j)
            data_values10_final.append(
                slope_intercept(j, times10[i], data_values10[i], times10[i + 1], data_values10[i + 1]))
    elif isinstance(times10[i], float) and isinstance(times10[i + 1], float):
        for k in integers_in_range_close(math.ceil(times10[i]), math.floor(times10[i + 1])):
            if math.ceil(times10[i]) <= math.floor(times10[i + 1]):
                times10_final.append(k)
                data_values10_final.append(
                    slope_intercept(k, times10[i], data_values10[i], times10[i + 1], data_values10[i + 1]))
    elif isinstance(times10[i], float) and isinstance(times10[i + 1], int):
        if times10[i + 1] - times10[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times10[i]), times10[i + 1]):
                times10_final.append(p)
                data_values10_final.append(
                    slope_intercept(p, times10[i], data_values10[i], times10[i + 1], data_values10[i + 1]))
    elif isinstance(times10[i], int) and isinstance(times10[i + 1], float):
        times10_final.append(times10[i])
        data_values10_final.append(data_values10[i])
        if times10[i + 1] - times10[i] > 1:
            for o in integers_in_range(times10[i], math.floor(times10[i + 1])):
                times10_final.append(o)
                data_values10_final.append(
                    slope_intercept(o, times10[i], data_values10[i], times10[i + 1], data_values10[i + 1]))
times10_final.append(times10[-1])
data_values10_final.append(data_values10[-1])

print(times10_final)
print(data_values10_final)

# 第十一组模拟数据string转numbers：
times11 = [float(x) for x in times11]
data_values11 = [float(y) for y in data_values11]
for i in range(0, len(times11)):
    if times11[i] - math.floor(times11[i]) == 0:
        times11[i] = int(times11[i])

for i in range(0, len(data_values11)):
    if data_values11[i] - math.floor(data_values11[i]) == 0:
        data_values11[i] = int(data_values11[i])
# 第十一组模拟数据对齐：
times11_final = []
data_values11_final = []
for i in range(0, len(times11) - 1):
    if isinstance(times11[i], int) and isinstance(times11[i + 1], int):
        times11_final.append(times11[i])
        data_values11_final.append(data_values11[i])
        for j in integers_in_range_open(times11[i], times11[i + 1]):
            times11_final.append(j)
            data_values11_final.append(
                slope_intercept(j, times11[i], data_values11[i], times11[i + 1], data_values11[i + 1]))
    elif isinstance(times11[i], float) and isinstance(times11[i + 1], float):
        for k in integers_in_range_close(math.ceil(times11[i]), math.floor(times11[i + 1])):
            if math.ceil(times11[i]) <= math.floor(times11[i + 1]):
                times11_final.append(k)
                data_values11_final.append(
                    slope_intercept(k, times11[i], data_values11[i], times11[i + 1], data_values11[i + 1]))
    elif isinstance(times11[i], float) and isinstance(times11[i + 1], int):
        if times11[i + 1] - times11[i] > 1:
            for p in integers_in_range_inverse(math.ceil(times11[i]), times11[i + 1]):
                times11_final.append(p)
                data_values11_final.append(
                    slope_intercept(p, times11[i], data_values11[i], times11[i + 1], data_values11[i + 1]))
    elif isinstance(times11[i], int) and isinstance(times11[i + 1], float):
        times11_final.append(times11[i])
        data_values11_final.append(data_values11[i])
        if times11[i + 1] - times11[i] > 1:
            for o in integers_in_range(times11[i], math.floor(times11[i + 1])):
                times11_final.append(o)
                data_values11_final.append(
                    slope_intercept(o, times11[i], data_values11[i], times11[i + 1], data_values11[i + 1]))
times11_final.append(times11[-1])
data_values11_final.append(data_values11[-1])

print(times11_final)
print(data_values11_final)

# 选取range最小的数据然后其他的把多余的去除：
minimum_index = min(len(times2_final), len(times3_final), len(times4_final), len(times5_final),
                    len(times6_final), len(times7_final), len(times8_final), len(times9_final), len(times10_final),
                    len(times11_final))

print(minimum_index)

# 观察后，选择2-11组数据，最多取到第69个数据。
# 求出平均标准学习曲线：
times_final = [x for x in range(0, 69)]
print(times_final)

mean_loaded = []
for i in range(0, 69):
    mean_loaded.append(
        round((data_values2_final[i] + data_values3_final[i] + data_values4_final[i] + data_values5_final[i]
               + data_values6_final[i] + data_values7_final[i] + data_values8_final[i] + data_values9_final[
                   i] + data_values10_final[i] +
               data_values11_final[i]) / 10, 3))
print(mean_loaded)

# 画出标准学习10次后的平均负载值图像：
plt.plot(times_final, mean_loaded, marker='o', linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Manual Scaling')

plt.grid(True)
plt.tight_layout()
cursor = mplcursors.cursor(hover=True)


@cursor.connect("add")
def on_hover(sel):
    index = sel.target.index
    x = times[index]
    y = data_values[index]
    sel.annotation.set_text(f'Time: {x}, StudiedValue: {y}')


plt.show()

# 求上限包络线:
max_line = []
for i in range(0, 69):
    max_line.append(round(mean_loaded[i] + math.sqrt((data_values2_final[i] - mean_loaded[i]) ** 2 + (
            data_values3_final[i] - mean_loaded[i]) ** 2 + (data_values4_final[i] -
                                                            mean_loaded[i]) ** 2 + (
                                                             data_values5_final[i] - mean_loaded[i]) ** 2 + (
                                                             data_values6_final[i] - mean_loaded[i]) ** 2 + (
                                                             data_values7_final[i] - mean_loaded[i]) ** 2 + (
                                                             data_values8_final[i] - mean_loaded[i]) ** 2 + (
                                                             data_values9_final[i] - mean_loaded[i]) ** 2 +
                                                     (data_values10_final[i] - mean_loaded[i]) ** 2 + (
                                                             data_values10_final[i] - mean_loaded[i]) ** 2 +
                                                     (data_values11_final[i] - mean_loaded[i]) ** 2 / 10), 3))
print(max_line)
# 求下限包络线:
min_line = []
for i in range(0, 69):
    min_line.append(round(mean_loaded[i] - math.sqrt((data_values2_final[i] - mean_loaded[i]) ** 2 + (
            data_values3_final[i] - mean_loaded[i]) ** 2 + (data_values4_final[i] -
                                                            mean_loaded[i]) ** 2 + (
                                                                 data_values5_final[i] - mean_loaded[i]) ** 2 + (
                                                                 data_values6_final[i] - mean_loaded[i]) ** 2 + (
                                                                 data_values7_final[i] - mean_loaded[i]) ** 2 + (
                                                                 data_values8_final[i] - mean_loaded[i]) ** 2 + (
                                                                 data_values9_final[i] - mean_loaded[i]) ** 2 +
                                                         (data_values10_final[i] - mean_loaded[i]) ** 2 + (
                                                                 data_values10_final[i] - mean_loaded[i]) ** 2 +
                                                         (data_values11_final[i] - mean_loaded[i]) ** 2 / 10), 3))
print(min_line)

# 画出带有上下包络线的标准学习曲线：
plt.plot(times_final, mean_loaded, marker='o', linestyle='-',color='blue')
plt.plot(times_final,max_line, marker='o',color='red',linestyle='--')
plt.plot(times_final,min_line, marker='o',color='yellow',linestyle='--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Manual Scaling')

plt.grid(True)
plt.tight_layout()
cursor = mplcursors.cursor(hover=True)


@cursor.connect("add")
def on_hover(sel):
    index = sel.target.index
    x = times[index]
    y = data_values[index]
    sel.annotation.set_text(f'Time: {x}, StudiedValue: {y}')

plt.show()

# 最后一步载入实时负载数据(100倍率以下）并根据加工效率优先来学习，风格暂定为均衡：
# 然后研究一次零件在一个周期内的加工总时长和给进倍率之间的关系（从ToProgram_Single到ToProgram_Single)
#


test_load =  []
final_line = []

