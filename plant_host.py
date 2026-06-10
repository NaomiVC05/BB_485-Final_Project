import pandas as pd
import matplotlib.pyplot as plt 


#Read in the tsv file and save as a pandas dataframe
df = pd.read_csv(
    "FungalTraits_DB - Naomi Villalobos.tsv",
    sep="\t") 


#Filter the dataframe by the Plant pathgentic capacity column to retain only the leaf/fruit/seed pathogens and assign this filted data frame as a new varible
leaf_pathogens = df[
    df["Plant_pathogenic_capacity_template"]
    .str.contains("leaf/fruit/seed_pathogen", na=False)]


#For the new dataframe, index it by the Specific_host column and get a count of the different values (summary function?)
host_counts = (
    leaf_pathogens["Specific_hosts"]
    .dropna()
    .value_counts())
pd.set_option('display.max_rows', None)

host_counts.to_csv("host_counts.csv")
print(host_counts)

#Use these counts to make a pie chart (or stacked bar chart)
top_hosts = host_counts.head(10)

plt.figure(figsize=(10,6))
top_hosts.plot(kind="bar")
plt.xlabel("Specific Host")
plt.ylabel("Count")
plt.title("Top 10 Hosts of Leaf/Fruit/Seed Pathogens")
plt.tight_layout()
plt.savefig("top10_hosts.png")

