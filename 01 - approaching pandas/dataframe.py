import pandas as pd

df1 = pd.DataFrame(
    {
        "x":pd.Series([3,2.5,-1], index=["a","b","c"]),
        "color": pd.Series(["r","g","b"], index=["a","b","c"])  
    }
)
print(df1)
# Columnas = x y color
print(df1.info())
# 2 primeros y tail 2 ultimos
print(df1.head(2))
print(df1.columns)



