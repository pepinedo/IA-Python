# --- B.1 ---

# El porcentaje de hogares que pertenece a la clase 1 (Ineficiente) es del 25%

# Tendría una precisión del 100% pero un accuracy del 0%, habiendo muchísimos Falsos Positivos. Sería inaceptable porque lo que quieren es, precisamente, evitar enviar técnicos a casas que no lo necesiten, y este modelo haría bien ese problema. 

# --- B.2 ---

# | Modelo               | Accuracy | Recall 
# | Dummy                | 0.631579 | 0
# | Regresión Logística  | 0.982456 | 0.9761
# | Random Forest        | 0.956140 | 0.928571   

# Descartaría el modelo Dummy porque tiene un Recall de 0, osea, que no va a acertar ningún positivo

# --- B.3 --- 

# | Modelo               | Accuracy Train | Accuracy Test
# | Regresión Logística  | 0.982456       | 0.989011
# | Random Forest        | 0.956140       | 1.000000 

# El RandomForest muestra señales clara de sobreajuste porque el test sale a 1. Aunque tenga peor rendimiento, es mas estable, como muestra el test.

# “El modelo es inestable y no generaliza bien.” 

# --- B.4 ---

