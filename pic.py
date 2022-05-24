import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/edenLee94/d3-file/main/infovis_data.csv')

x=df['region']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x,df['2020_fa70'],label='age70',)
ax.bar(x,df['2020_fa60'],label='age60')
ax.bar(x,df['2020_fa50'],label='age50')
ax.bar(x,df['2020_fa40'],label='age40')
ax.bar(x,df['2020_fa30'],label='age30')
ax.legend()
plt.title('2020 number of becoming farmer via age')
plt.xticks(rotation=45)
plt.show()
