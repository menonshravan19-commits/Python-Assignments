# 1. Loading the Taxis Dataset 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("taxis")

# 2. Handling Missing Values
print("Missing values per column:\n", df.isnull().sum())

# Numerical columns — impute with median (robust to outliers, unlike mean)
numerical_cols = ['fare', 'tip', 'tolls', 'distance', 'total', 'passengers']
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# payment is categorical but reasonably guessable — impute with mode
df['payment'] = df['payment'].fillna(df['payment'].mode()[0])

# Location fields are critical and can't be meaningfully guessed —
# a wrong borough would corrupt every visualization that groups by it —
# so drop rows missing these instead of imputing
critical_cols = ['pickup_zone', 'dropoff_zone', 'pickup_borough', 'dropoff_borough']
df = df.dropna(subset=critical_cols)

print("\nAfter cleaning:\n", df.isnull().sum())

# 3. Visualizations using Matplotlib/Pandas Plot
# Line Chart
df['pickup'] = pd.to_datetime(df['pickup'])
df_sorted = df.sort_values('pickup')

plt.figure(figsize=(12, 6))
plt.plot(df_sorted['pickup'], df_sorted['fare'])
plt.xlabel('Pickup Time'); plt.ylabel('Fare ($)')
plt.title('Fare Over Time')
plt.xticks(rotation=45); plt.tight_layout()
plt.show()

# Bar Chart
fare_by_borough = df.groupby('pickup_borough')['fare'].sum()

plt.figure(figsize=(8, 5))
fare_by_borough.plot(kind='bar')
plt.xlabel('Pickup Borough'); plt.ylabel('Total Fare ($)')
plt.title('Total Fare by Pickup Borough')
plt.tight_layout(); plt.show()

# Pie Chart
payment_counts = df['payment'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%')
plt.title('Trips by Payment Method')
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['distance'], bins=30, edgecolor='black')
plt.xlabel('Distance (miles)'); plt.ylabel('Frequency')
plt.title('Distribution of Trip Distance')
plt.tight_layout(); plt.show()

# Box Plot
plt.figure(figsize=(8, 5))
df.boxplot(column='tip', by='pickup_borough')
plt.xlabel('Pickup Borough'); plt.ylabel('Tip ($)')
plt.title('Tip Distribution by Pickup Borough')
plt.suptitle('')  # pandas auto-adds a second title; this removes it
plt.tight_layout(); plt.show()

# 4. Visualizations using Seaborn
# Count Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='pickup_borough')
plt.title('Trip Count by Pickup Borough')
plt.tight_layout(); plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='distance', y='fare', hue='pickup_borough')
plt.title('Distance vs Fare by Pickup Borough')
plt.tight_layout(); plt.show()

# Heatmap
corr_cols = ['distance', 'fare', 'tip', 'tolls', 'total']
corr_matrix = df[corr_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout(); plt.show()

# Pair Plot
sns.pairplot(df, vars=['distance', 'fare', 'tip', 'total'], hue='pickup_zone')
plt.show()

# Violin Plot
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='payment', y='fare')
plt.title('Fare Distribution by Payment Method')
plt.tight_layout(); plt.show()
