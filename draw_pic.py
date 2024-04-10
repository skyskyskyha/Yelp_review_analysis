import matplotlib.pyplot as plt
import numpy as np


predictions = []
actuals = []

with open("gpt3.5-fine-tuning-result.txt", "r") as data:
    lines = data.readlines()
    for line in lines:
        # print(line)
        prediction, actual = int(line[0]), int(line[2])
        predictions.append(prediction)
        actuals.append(actual)

plt.scatter(range(len(predictions)), predictions, color='blue', label='Predictions')
plt.scatter(range(len(actuals)), actuals, color='red', label='Actuals', alpha=0.5)

plt.legend()

plt.title('Comparison of Predictions and Actuals')
plt.xlabel('Sample Index')
plt.ylabel('Rating')

plt.grid(True)

plt.show()
plt.clf()


errors = np.array(predictions) - np.array(actuals)


plt.plot(errors, label='Prediction Error', marker='o')
plt.axhline(y=0, color='r', linestyle='--')


plt.legend()


plt.title('Prediction Errors')
plt.xlabel('Sample Index')
plt.ylabel('Error')


plt.grid(True)


plt.savefig('prediction_error_line_plot_finetuning.png')
plt.clf()


plt.figure(figsize=(10, 6))
plt.plot(predictions, label='Predictions', marker='o', linestyle='-', color='blue')
plt.plot(actuals, label='Actuals', marker='x', linestyle='-', color='red')

# 添加图表装饰
plt.title('Predictions vs. Actuals')
plt.xlabel('Sample Index')
plt.ylabel('Rating')
plt.legend()
plt.grid(True)


plt.savefig('predictions_vs_actuals_finetuning.png')


plt.clf()