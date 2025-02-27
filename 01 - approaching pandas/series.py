import pandas as pd

edades = pd.Series(
    {
        "Pedro": 28,
        "maria":22,
    },
    name="edad"
)

edades = pd.Series(
    [20,21,22],
    index=["Maria","hola","asd"],
    name="edad"
)

esperanza_adicional = pd.Series(
    [51.4,64,45],
    index=["Maria","hola","asd"],
    name="esperanza"
)

print(edades)
print(esperanza_adicional)
sum = edades + esperanza_adicional
print(sum)

