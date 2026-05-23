result = clean_df.groupBy(
    "product"
).sum("amount")

display(result)