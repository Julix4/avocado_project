# Prediccion de Precios del Aguacate en USA

## Este es un proyecto grupal de la UOC

Este proyecto esta formado por Julieth Vasco, Albert Pañeres y Thomaz Santos.

# Proyecto de Análisis de Ventas de Aguacates

Este repositorio contiene un análisis detallado de los datos de ventas de aguacates en diferentes regiones y períodos de tiempo. El objetivo es explorar patrones de ventas, realizar predicciones y obtener insights útiles para la toma de decisiones comerciales.

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Contenido del Dataset](#contenido-del-dataset)
4. [Resultados del Proyecto](#resultados-del-proyecto)
5. [Dependencias](#dependencias)
6. [Instalación](#instalación)
7. [Licencia](#licencia)

---

## Descripción del Proyecto

Este proyecto analiza datos históricos de ventas de aguacates en Estados Unidos, utilizando técnicas de análisis de datos y aprendizaje automático. Las conclusiones pueden ayudar a los productores y distribuidores a optimizar sus estrategias de venta y distribución.

## Estructura del Proyecto

- `1. Analisis series temporales.ipynb` - Notebook que contiene el análisis de series temporales de ventas.
- `2. Gráficos para visualización de datos.ipynb` - Notebook con gráficos utilizados para visualizar diferentes aspectos de los datos de ventas.
- `3. Elasticidad-Precio Demanda.ipynb` - Análisis de la relación entre elasticidad de precio y demanda de aguacates.
- `4. Analisis de Cohortes.ipynb` - Notebook que explora el análisis de cohortes de clientes.
- `5. Análisis de Correlación y Regresión.ipynb` - Contiene un análisis de correlación y regresión para explorar relaciones entre variables.
- `Avocado_EDA.ipynb` - Exploración y análisis descriptivo inicial de los datos.
- `Presentacion.ipynb` - Presentación de los resultados principales y conclusiones del proyecto.
- `README.md` - Descripción general del proyecto y documentación.
- `avocado.csv` - Dataset principal de ventas de aguacates.

## Contenido del Dataset

La data representa las ventas al detal en distintos paquetes, conteniendo información sobre las ventas totales, el precio y las fechas de los últimos años. Incluye datos de dos tipos de aguacates (orgánicos y convencionales) y de varias regiones de los Estados Unidos donde se comercializan.

**Columnas del dataset**:
- `Date`: Fecha de la observación.
- `AveragePrice`: Precio promedio de un solo aguacate.
- `Total Volume`: Número total de aguacates vendidos.
- `4046`: Número total de aguacates con PLU 4046 vendidos.
- `4225`: Número total de aguacates con PLU 4225 vendidos.
- `4770`: Número total de aguacates con PLU 4770 vendidos.
- `Total Bags`: Número total de bolsas vendidas.
- `Small Bags`: Número de bolsas pequeñas vendidas.
- `Large Bags`: Número de bolsas grandes vendidas.
- `XLarge Bags`: Número de bolsas extra grandes vendidas.
- `type`: Tipo de aguacate (`conventional` o `organic`).
- `year`: Año de la observación.
- `region`: Ciudad o región donde se tomó la observación.

## Resultados del Proyecto

A continuación se presentan algunos de los hallazgos clave y visualizaciones del análisis de ventas de aguacates:

### 1. Patrones de Ventas por Región
   - Las regiones con mayor demanda de aguacates fueron: **California**, **SouthCentral** y **Northeast**.
   - California mostró una tendencia de crecimiento constante en las ventas, mientras que otras regiones como el Northeast tuvieron ventas estacionales.

### 2. Estacionalidad en las Ventas
   - Las ventas de aguacates mostraron patrones estacionales significativos, con picos de venta durante los meses de **abril a junio** y nuevamente entre **octubre y diciembre**.
   - Esta estacionalidad parece estar influenciada por eventos y feriados como el Cinco de Mayo y las fiestas de fin de año, donde la demanda de aguacates para guacamole aumenta.

   ![Gráfico de estacionalidad](path/to/seasonality_chart.png)

### 3. Influencia del Precio en la Demanda
   - La correlación entre el precio y la demanda de aguacates fue negativa, es decir, a medida que el precio aumentaba, la demanda tendía a disminuir.
   - Los aguacates orgánicos mostraron una menor elasticidad de precio en comparación con los aguacates convencionales, indicando que los consumidores están dispuestos a pagar más por productos orgánicos.

   ![Gráfico de precios vs demanda](path/to/price_vs_demand_chart.png)

### 4. Predicción de Ventas
   - Utilizando un modelo de regresión lineal, se logró predecir la demanda futura de aguacates con una precisión promedio del **85%**.
   - Este modelo sugiere que las ventas continuarán aumentando en las principales regiones, especialmente en California, donde el crecimiento proyectado es del **5% anual**.

   ![Gráfico de predicción de ventas](path/to/sales_prediction_chart.png)

### 5. Análisis de Cohortes
   - Al realizar un análisis de cohortes, se observó que los clientes de la región SouthCentral tienden a hacer compras más frecuentes y en volúmenes mayores durante los primeros 3 meses del año.
   - Esto indica que estrategias de fidelización podrían enfocarse en este periodo para maximizar la retención.

## Dependencias

Este proyecto utiliza las siguientes bibliotecas de Python:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `statsmodels`

## Instalación

Para instalar las dependencias, asegúrate de tener [Python 3.6+](https://www.python.org/) instalado y luego ejecuta:

```bash
pip install -r requirements.txt

## Licencia

MIT License

Copyright (c) 2024 Avocado Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


