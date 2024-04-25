import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 假设图片文件名分别是'image1.png', 'image2.png', 'image3.png', 'image4.png'
image_paths = ['prediction_error_line_plot_finetuning-american.png',
               'prediction_error_line_plot_finetuning-asian.png',
               'prediction_error_line_plot_finetuning-europe.png',
               'prediction_error_line_plot_finetuning-latin.png']
titles = ['American', 'Asian', 'Europe', 'Latin']

# 创建一个2x2的图表
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for ax, image_path, title in zip(axs.ravel(), image_paths, titles):
    img = mpimg.imread(image_path)
    ax.imshow(img)
    ax.set_title(title)
    ax.axis('off')  # 关闭坐标轴

plt.tight_layout()
# plt.show()
plt.savefig("prediction_error.png")