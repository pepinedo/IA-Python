# --- A.1 ---

# Considero que es más importante, para la empresa, ahorrarse enviar al técnico a una casa eficiente. Osea, un Falso Positivo. No es algo CRITICO un falso negativo, asiq le doy menos importancia

# --- A.2 ---

# Tener un 95% de accuracy quiere decir que tiene un 95% de acertar el resultado, pero no sabemos en cuanta proporción hay falsos positivos (que son los que nos interesan) ni falsos negativos. Necesitamos conocer el Recall, que es la proporción de positivos acertados. 

# Ese 95% puede ser inútil o, incluso, peligroso, cuando los Falsos Positivos son MUY CAROS y la Recall es muy baja. Osea, que habría muchos Falsos Positivos. 

# --- A.3 ---

# Para una detección temprana, usaría el modelo A
# Para una auditoría costosa, usaría el modelo B ya que los positivos que acierta, los acierta en muy buena proporción. Habría muy pocos casos de Falsos Positivos, haciendo perder el mínimo dinero en enviar técnicos cuando no se les necesita. 