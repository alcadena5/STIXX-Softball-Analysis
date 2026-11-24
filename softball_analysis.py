import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned softball dataset
data = pd.read_csv("STIXX_02_Clean.csv")

# Display the first five records
print("STX STIXX Softball Player Statistics")
print(data.head())

# Display the total number of records
print("Total Player Records:", len(data))

# Display the teams
print("Teams:")
print(data["Team"].unique())


# Calculate total hits by team
team_hits = data.groupby("Team")["Hits"].sum()

print("\nTotal Hits by Team:")
print(team_hits)

# Calculate batting average by team
team_at_bats = data.groupby("Team")["At_Bats"].sum()
team_average = team_hits / team_at_bats

print("\nBatting Average by Team:")
print(team_average.round(3))

# Find the top 10 batting records
top_players = data.sort_values("Batting_Average", ascending=False).head(10)

print("\nTop 10 Batting Records:")
print(top_players[["Player_ID", "Player_Name", "Team", "Batting_Average"]])


# Graph 1: Total Hits by Team
team_hits = team_hits.sort_values(ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(team_hits.index, team_hits.values, color="royalblue")
plt.title("Total Hits by STX STIXX Team")
plt.xlabel("Total Hits")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("team_hits.png", dpi=300)
plt.close()


# Graph 2: Batting Average by Team
team_average = team_average.sort_values(ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(team_average.index, team_average.values,
         color="royalblue")
plt.title("Batting Average by STX STIXX Team")
plt.xlabel("Batting Average")
plt.ylabel("Team")
plt.xlim(0, 1)
plt.tight_layout()
plt.savefig("team_batting_average.png", dpi=300)
plt.close()


# Graph 3: Top 10 Individual Batting Records
top_players = top_players.sort_values("Batting_Average")

player_labels = top_players["Player_Name"] + " (" + top_players["Player_ID"] + ")"

plt.figure(figsize=(10, 6))
plt.barh(player_labels, top_players["Batting_Average"],
         color="royalblue")
plt.title("Top 10 Individual Batting Records")
plt.xlabel("Batting Average")
plt.ylabel("Player")
plt.xlim(0, 1)
plt.tight_layout()
plt.savefig("top_10_players.png", dpi=300)
plt.close()

print("\nAll three graphs were created successfully!")

