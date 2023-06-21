
import pandas as pd 
import matplotlib.pyplot as plt 

flood = pd.read_excel('number_of_severe_floods_in_europe.xlsx')

year = flood['year']
floods = flood['number_of_severe_floods']
colors = ['#4F709C', '#EA906C']

fig, ax = plt.subplots()
plt.plot(
         year,
         floods,
         marker = 'o',
         linestyle = 'solid',
         color = colors[0]
        )

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(colors[1])
ax.spines['left'].set_color(colors[1])

plt.xticks(color=colors[1])
plt.yticks(color=colors[1])

plt.xlim(1980, 2011)

plt.show()

