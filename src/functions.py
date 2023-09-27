import matplotlib.pyplot as plt
import folium
import webbrowser


def get_nof_squirrels_bycolors(df):
    fur_color_counts = df['Primary Fur Color'].value_counts()
    plt.figure(figsize=(10, 6))
    fur_color_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Squirrels Per Fur Color')
    plt.xlabel('Fur Color')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # save plot to file
    plt.savefig('squirrel_colors.png')
    # Show the plot
    plt.show()



# Map of White Squirrels: Create a map that marks the locations of white squirrels spotted during the census.

def plot_white_squirrels(df):

    white_squirrels = df[df["Highlights in Fur Color"] == "White"]

    m = folium.Map(location=[white_squirrels["Squirrel Latitude (DD.DDDDDD)"].mean(), 
                             white_squirrels["Squirrel Longitude (-DD.DDDDDD)"].mean()], 
                   zoom_start=13)

    # Add markers for each white squirrel sighting
    for index, row in white_squirrels.iterrows():
        folium.Marker([row["Squirrel Latitude (DD.DDDDDD)"], row["Squirrel Longitude (-DD.DDDDDD)"]],
                      tooltip=row["Park Name"]).add_to(m)
        
    mapfile= "map.html"
    m.save(mapfile)
    webbrowser.open(mapfile)
    return 
