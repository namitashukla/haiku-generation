# Evaluation Script 

Evaluation script implementing evaluation metrics for Poems generated (Haiku) - 

- **Metric 1:** accesses the quality of text
  - GRUEN: https://aclanthology.org/2020.findings-emnlp.9.pdf
  - Github: https://github.com/WanzhengZhu/GRUEN

- **Metric 2:** accesses the structure of text
  - Mean Syllable count for each line (should be 5-7-5 for Haiku)



# Steps to run via terminal 

- Ensure all installs and setup have been made 
- Make sure you can access the GRUEN folder (the file imports greun.py file)
- Pass the csv data path file into the command line
  - The csv must have 3 columns namely ['sent_1', 'sent_2', 'sent_3'] that each has 1 line of the corresponding poem
  - File running Example 

```
python evaluation.py '/content/drive/MyDrive/output.csv'
```

- The file would print the mean, median and quantile of the scores achieved for each poem.

# reference on how to run
Please follow the Evaluation.ipynb step by step to get an easy understanding of the metric score generation 