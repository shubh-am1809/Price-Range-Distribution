import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset .csv")
df = df[['Price range']].dropna()
price_counts = df['Price range'].value_counts().sort_index()

plt.figure()
price_counts.plot(kind='bar')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Restaurant Price Ranges')
plt.tight_layout()

plt.savefig("output/price_range_distribution.png")
plt.close()

total_restaurants = price_counts.sum()
price_percentage = (price_counts / total_restaurants) * 100

result = pd.DataFrame({
    'Price Range': price_counts.index,
    'Restaurant Count': price_counts.values,
    'Percentage (%)': price_percentage.round(2)
})


result.to_csv("output/price_range_percentage.csv", index=False)


print("\nPrice Range Distribution:\n")
print(result)
print("\nBar chart saved as output/price_range_distribution.png")
