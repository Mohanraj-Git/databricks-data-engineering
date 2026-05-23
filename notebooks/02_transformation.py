from pyspark.sql.functions import col

clean_df = df.filter(
    col("amount").isNotNull()
)

display(clean_df)