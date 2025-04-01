import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 设置字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['pdf.fonttype'] = 42  # 使用 Type 42 字体避免字体嵌入问题
plt.rcParams['ps.fonttype'] = 42

prompt_id = np.arange(10)
task_id = np.arange(10)
selection_frequency = np.array([
    [606, 43, 84, 41, 41, 33, 41, 65, 35, 11] ,
    [58, 599, 85, 36, 46, 55, 31, 39, 36, 15] ,
    [30, 35, 639, 23, 28, 22, 63, 109, 40, 11] ,
    [57, 99, 60, 443, 37, 100, 55, 48, 19, 82] ,
    [42, 65, 107, 52, 458, 102, 33, 79, 31, 31] ,
    [17, 59, 23, 33, 22, 654, 61, 90, 31, 10] ,
    [14, 65, 111, 62, 17, 75, 520, 100, 13, 23] ,
    [11, 67, 75, 16, 30, 92, 71, 587, 13, 38] ,
    [26, 99, 66, 40, 57, 40, 26, 14, 621, 11] ,
    [47, 58, 67, 45, 54, 108, 43, 107, 71, 400]
    ])

# 创建热力图
plt.figure(figsize=(12, 10))
ax = sns.heatmap(selection_frequency, annot=True, fmt="d", cmap="YlOrRd", 
                 xticklabels=prompt_id, yticklabels=task_id, annot_kws={"size": 14})

# 设置标题和标签
plt.title('Task Embeddings Selection Frequency', fontsize=24)
plt.xlabel('Key ID', fontsize=20)
plt.ylabel('Task ID', fontsize=20)

# 调整刻度标签大小
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# 调整颜色条
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=16)

# 保存图像
plt.savefig("histogram_heatmap.pdf", bbox_inches='tight')
# plt.show()