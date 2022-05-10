# 구간 합 계산
data, prefix_sum = [10, 20, 30, 40, 50], [0]
for i in range(len(data)):
    prefix_sum.append(data[i] + prefix_sum[i])
left, right = 3, 4
print(prefix_sum[right] - prefix_sum[left - 1])
