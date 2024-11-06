import pandas as pd
import plotly.express as px
 
# data 
data = {
    "Ship Name": [
        "USS George Washington", "USS John Adams", "USS Thomas Jefferson", "USS James Madison",
        "USS James Monroe", "USS John Quincy Adams", "USS Andrew Jackson",
        "USS Martin Van Buren", "USS Germantown", "USS John Tyler"
    ],
    "Maintenance Start Date": ["1/1/25", "3/6/25", "7/4/25", "5/18/25", "1/18/26", "4/14/26", "11/11/26", "2/1/27", "8/22/27", "4/1/28"],
    "Maintenance End Date": ["9/18/25", "7/25/25", "2/16/26", "2/2/27", "5/4/27", "9/14/27", "1/28/28", "12/12/27", "5/28/28", "4/1/29"],
    "Docking Start Date": ["1/1/25", "3/6/25", "11/15/25", "6/16/25", "3/14/26", "8/11/26", "3/13/27", "2/28/27", "9/1/27", "5/2/28"],
    "Docking End Date": ["6/1/25", "4/15/25", "2/16/26", "1/23/27", "9/14/26", "1/1/27", "11/12/27", "10/28/27", "4/15/28", "7/11/28"]
}
 
# Convert data to DataFrame
df = pd.DataFrame(data)
 
# Prepare data for Gantt chart
tasks = []
 
for _, row in df.iterrows():
    # Maintenance task
    tasks.append(dict(
        Task=row['Ship Name'],
        Start=pd.to_datetime(row['Maintenance Start Date'], format="%m/%d/%y"),
        Finish=pd.to_datetime(row['Maintenance End Date'], format="%m/%d/%y"),
        Type="Maintenance"
    ))
   
    # Docking task
    tasks.append(dict(
        Task=row['Ship Name'],
        Start=pd.to_datetime(row['Docking Start Date'], format="%m/%d/%y"),
        Finish=pd.to_datetime(row['Docking End Date'], format="%m/%d/%y"),
        Type="Docking"
    ))
 
# Convert tasks to DataFrame
tasks_df = pd.DataFrame(tasks)
 
# Create Gantt chart with Plotly
fig = px.timeline(
    tasks_df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Type",
    title="Ship Maintenance and Docking Schedule",
    labels={"Task": "Ship Name", "Type": "Task Type"}
)
 
# Update layout to improve readability
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Ship Name",
    xaxis=dict(tickformat="%b %Y"),  # Format x-axis dates
    bargap=0.2
)
 
# Show the chart
fig.show()