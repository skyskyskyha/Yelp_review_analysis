For the whole code and data, please refer to:
https://drive.google.com/drive/folders/1N78wtIsKqqWN5b6xWfa6nI3uh13ecaBT

Yelp review data analysis via GPT and sentiment analysis

We trained a GPT model based on GPT-3.5-turbo and did sentiment analysis
on the Yelp review data from Atlanta from post COVID-19 era.

We choose part of them for prompt engineering and remaining for training.

GPT_train.py

This is the main train file

This is the scattor plot for prediction and actual ratings
![Alt text](scatter_prediction_vs_actual.png)


This is the line plot for prediction and actual ratings
![Alt text](predictions_vs_actuals.png)

This is the error difference between prediction and actual ratings
![Alt text](prediction_error_line_plot.png)


Fine tuning result:
![Alt text](predictions_vs_actuals_finetuning.png)
![Alt text](prediction_error_line_plot_finetuning.png)

Fine tuning result for asian:
![Alt text](predictions_vs_actuals_finetuning-asian.png)
![Alt text](prediction_error_line_plot_finetuning-asian.png)

Fine tuning result for europe:
![Alt text](predictions_vs_actuals_finetuning-europe.png)
![Alt text](prediction_error_line_plot_finetuning-europe.png)

Fine tuning result for american:
![Alt text](predictions_vs_actuals_finetuning-american.png)
![Alt text](prediction_error_line_plot_finetuning-american.png)
