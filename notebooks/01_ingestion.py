# Read sales CSV

df = spark.read.csv(
    "/FileStore/sales.csv",
    header=True,
    inferSchema=True
)

display(df)