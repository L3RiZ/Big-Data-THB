import pandas as pd 
import matplotlib.pyplot as plt

# Read CSV

df_sets01 = pd.read_csv('./Lego/sets01.csv', delimiter=',')
df_sets02 = pd.read_csv('./Lego/sets02.csv', delimiter=',')
df_sets03 = pd.read_csv('./Lego/sets03.csv', delimiter=',')
df_themes = pd.read_csv('./Lego/themes.csv', delimiter=',')
df_inventories = pd.read_csv('./Lego/inventories.csv', delimiter=',')
df_inventory_parts = pd.read_csv('./Lego/inventory_parts.csv', delimiter=',')
df_colors = pd.read_csv('./Lego/colors.csv', delimiter=',')

# Merge

df_sets = pd.concat([df_sets01, df_sets02, df_sets03])
df_sets_themes = pd.merge(df_sets, df_themes, left_on='theme_id', right_on='id', sort=True)
df_sets_themes.drop(columns='id', inplace=True)
df_with_inventories = pd.merge(df_sets_themes, df_inventories, on="set_num", sort=True)
df_with_inventory_parts = pd.merge(df_with_inventories, df_inventory_parts, left_on='id', right_on='inventory_id', sort=True)
df_with_inventory_parts.drop(columns='id', inplace=True)
df_with_colors = pd.merge(df_with_inventory_parts, df_colors, left_on='color_id', right_on='id', sort=True)
df_with_colors.drop(columns='id', inplace=True)

#Visualise 

df_sets['year'].value_counts(sort=False).sort_index().plot(kind='bar', figsize=(10, 5))
plt.savefig('lego1.pdf')

df_sets_themes[df_sets_themes['name_y'].str.contains("Star Wars")]['year'].value_counts().sort_index().plot(kind='bar', figsize=(10, 5), ylim=(0,100))
plt.savefig('lego2.pdf')

print(df_with_colors)