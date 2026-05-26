# Databricks notebook source
# %fs ls /

# COMMAND ----------

Storagelocation = "dbfs:/pipelines/ceadbba1-340d-4283-8e15-99981087c464"

# COMMAND ----------

files = dbutils.fs.ls(Storagelocation)
display(files)

# COMMAND ----------

files = dbutils.fs.ls(f"{Storagelocation}/system/events")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`dbfs:/pipelines/ceadbba1-340d-4283-8e15-99981087c464/system/events`

# COMMAND ----------

# %sql
# Describe extended hive_metastore.default.cn_daily_customer_books

# COMMAND ----------

#dbfs:/pipelines/ceadbba1-340d-4283-8e15-99981087c464/schemas/default/tables/cn_daily_customer_books

files = dbutils.fs.ls(f"{Storagelocation}/schemas/default/tables")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM hive_metastore.default.cn_daily_customer_books

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM hive_metastore.default.fr_daily_customer_books
