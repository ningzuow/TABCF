import pandas as pd

# 读取原始 glass.csv
df = pd.read_csv("data/glass/glass.csv")

# 把 Type 转成二分类：Type==1 -> "1", 其他 -> "0"
df["Type"] = df["Type"].apply(lambda x: "1" if x == 1 else "0")

# 保存处理后的文件
df.to_csv("data/glass/glass.csv", index=False)

print("处理完成，新的数据保存到 data/glass/glass.csv")
print(df["Type"].value_counts())
