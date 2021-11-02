import pandas as pd 
df = pd.read_csv("../data/TF2_test_metrics.csv")
print ( df.T.rename({"Unnamed: 0":"Metrics"})) 