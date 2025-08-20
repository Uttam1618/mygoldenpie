# Pandas Cheat Sheet

```python
import pandas as pd
```
## Read / Write
```python
df = pd.read_csv("file.csv")
df.to_csv("out.csv", index=False)
pd.read_excel("file.xlsx", sheet_name=0)
pd.to_parquet("file.parquet")
```
## Inspect
```python
df.head(); df.tail(); df.sample(5)
df.info(); df.describe(numeric_only=True)
df.shape; df.columns; df.dtypes
```
## Select / Filter
```python
df["col"]; df[["a","b"]]
df.loc[rows, cols]        # label
df.iloc[rows, cols]       # position
df.query("age >= 18 and city == 'Sydney'")
df[(df.age>=18) & (df.city=="Sydney")]
```
## Add / Modify Columns
```python
df["bmi"] = df["w"]/ (df["h"]/100)**2
df = df.assign(bmi=lambda d: d["w"]/(d["h"]/100)**2)
df.rename(columns={"old":"new"}, inplace=True)
```
## Missing Values
```python
df.isna().sum()
df.fillna(0, inplace=True)
df.dropna(subset=["a","b"], inplace=True)
```
## Sort / Unique
```python
df.sort_values(["city","age"], ascending=[True,False])
df["city"].unique(); df["city"].value_counts()
```
## Groupby / Aggregate
```python
df.groupby("city")["salary"].agg(["mean","median","count"])
df.groupby(["city","dept"]).agg(avg=("salary","mean"), n=("id","count"))
```
## Merge / Join / Concat
```python
pd.merge(left, right, on="id", how="left")
pd.concat([df1, df2], axis=0, ignore_index=True)
```
## Dates
```python
df["date"] = pd.to_datetime(df["date"])
df["y"] = df["date"].dt.year; df["m"] = df["date"].dt.month
df.set_index("date").resample("M")["sales"].sum()
```
## Quick Plot
```python
df.plot(x="date", y="sales")
```