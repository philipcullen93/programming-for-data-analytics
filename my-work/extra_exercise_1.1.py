import pandas as pd
import matplotlib.pyplot as plt

# creates a dataframe using the data from the .csv file
df = pd.read_csv("https://raw.githubusercontent.com/andrewbeattycourseware/PFDA-courseware/refs/heads/main/code/data/projectedbirths-cso.csv")

# displays the dataframe, I used this to see if the correct data was pulled 
print(df.head())

# create a simple plot using the data provided
plt.plot(df['Year'], df['VALUE'])
plt.xlabel('Year')
plt.ylabel('Birth Rate')
plt.title('Projected Birth rates by Year')
plt.show()

plt.savefig("my-work/projected_births.png")