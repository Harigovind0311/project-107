import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
book_df = df.loc[df['book_id']=='TRL_abc']
print(book_df.groupby('name')['place'].mean())

library_df = df.loc[df['library_place'] == 'TRL_abc']
print


fig.show()