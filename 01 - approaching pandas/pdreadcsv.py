import pandas as pd
from pathlib import Path
# Lectura de datos
# Sep por defecto es coma, si fuera ; cambiar
cairo = pd.read_csv("../data/datos_cairo.csv",
                    sep = "," ,
                    )
DATA_DIRECTORY = Path("../data")
cairo = pd.read_csv(DATA_DIRECTORY / "datos_cairo.csv")

print(cairo)
