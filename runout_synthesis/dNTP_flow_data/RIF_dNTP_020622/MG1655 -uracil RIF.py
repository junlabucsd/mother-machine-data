import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_0=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 0 +uracil_sorted.xlsx")
#df_5=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 5 -uracil_sorted.xlsx")
df_10=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 10 +uracil_sorted.xlsx")
#df_20=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 20 -uracil_sorted.xlsx")
df_40=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 40 +uracil_sorted.xlsx")
df_80=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 80 +uracil_sorted.xlsx")
df_240=pd.read_excel("H:/From_SCIENCE/Documents/PhD/Flow data/2022/June/RIF dNTP 020622/MG1655 RIF 240 +uracil_sorted.xlsx")

df_0["Time"]="0"
#df_5["Time"]="5"
df_10["Time"]="10"
#df_20["Time"]="20"
df_40["Time"]="40"
df_80["Time"]="80"
df_240["Time"]="240"

sns.set_style(style="dark")
sns.set_palette(palette="deep")
sns.set_context("paper")
sns.set(font="Arial")
_, ax = plt.subplots()

frames=[df_0, df_10, df_40, df_80, df_240]
dataframe = pd.concat(frames, ignore_index=True)
df_wide = dataframe.pivot(index="Channel", columns="Time", values="Events")

plot=sns.lineplot(x="Channel", y="Events", hue="Time", data=dataframe, ax=ax, legend="auto")
ax.set_prop_cycle(None)
df_wide.plot.area(stacked=False, alpha=0.5, ax=ax, legend=False)
#plt.fill_between(dataframe.Channel.values, dataframe.Events.values, 0, alpha=0.2)
plot.set_xlabel("Chromosome Equivalents")
plot.set_ylabel("Events")
plot.set_title("MG1655 +Ura + RIF", fontweight="bold")
plt.xticks([44,88],[2,4], fontweight="bold")
plt.show()
