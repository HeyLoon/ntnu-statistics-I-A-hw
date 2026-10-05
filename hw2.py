import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False 
df = pd.read_excel('data1.xlsx', sheet_name='data1')
scorpio_df = df[df['Zodiac'] == '10. 天蠍座(10/24-11/22) Scorpio']
cols = ['CT', 'B5_AnxietyBattery', 'B1_GameTime', 'B2_VideoTime']
titles = ['CT (手機成癮分數)', 'B5_AnxietyBattery (焦慮電量)', 'B1_GameTime (遊戲時間)', 'B2_VideoTime (影音時間)']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten() 

for i, col in enumerate(cols):
    mean_val = scorpio_df[col].mean()
    median_val = scorpio_df[col].median()
    skew_val = scorpio_df[col].skew()
    
    sns.histplot(scorpio_df[col], kde=True, ax=axes[i], color='skyblue', bins=15)
    
    axes[i].axvline(mean_val, color='red', linestyle='--', label=f'平均數: {mean_val:.1f}')
    axes[i].axvline(median_val, color='green', linestyle='-', label=f'中位數: {median_val:.1f}')
    
    axes[i].set_title(f"{titles[i]} (偏態: {skew_val:.2f})", fontsize=14)
    axes[i].set_xlabel("數值")
    axes[i].set_ylabel("人數 (Count)")
    axes[i].legend()
plt.tight_layout()
plt.show()
