import matplotlib.pyplot as plt
import folium
import webbrowser
import mpld3


def get_nof_squirrels_bycolors(df):
    if df.empty:
        print("The provided dataframe is empty. No plot will be generated.")
        return

    fur_color_counts = df['Primary Fur Color'].value_counts()
    plt.figure(figsize=(6, 3))
    fur_color_counts.plot(kind='bar', color='yellowgreen')
    plt.title('Number of Squirrels Per Fur Color')
    plt.xlabel('Fur Color')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=45)

    # Set the x-axis tick labels to the actual category names
    plt.xticks(range(len(fur_color_counts)), fur_color_counts.index)

    plt.tight_layout()
    html_plot = mpld3.fig_to_html(plt.gcf())
    with open('squirrel_plot.html', 'w') as file:
        file.write(html_plot)

# Distribution of Squirrels Per Area: Create a graph that shows the number of squirrels in different areas of NYC.


def get_squirrels_by_area(df):
    byarea_counts = df['Area Name'].value_counts()
    plt.figure(figsize=(5, 3))
    byarea_counts.plot(kind='bar', color='blue')
    plt.title('Distribution of Squirrels Per Area')
    plt.xlabel('Area')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=50)
    plt.tight_layout()
    html_area_plot = mpld3.fig_to_html(plt.gcf())
    with open('graph2.html', 'w') as f:
        f.write(html_area_plot)


# Map of White Squirrels: Create a map that marks the locations of white squirrels spotted during the census.

def plot_white_squirrels(df):
    if df.empty:
        print("The provided dataframe is empty. No plot will be generated.")
        return

    white_squirrels = df[df["Highlights in Fur Color"] == "White"]

    m = folium.Map(location=[white_squirrels["Squirrel Latitude (DD.DDDDDD)"].mean(),
                             white_squirrels["Squirrel Longitude (-DD.DDDDDD)"].mean()],
                   zoom_start=13)

    # Add markers for each white squirrel sighting
    for index, row in white_squirrels.iterrows():
        folium.Marker([row["Squirrel Latitude (DD.DDDDDD)"], row["Squirrel Longitude (-DD.DDDDDD)"]],
                      tooltip=row["Park Name"]).add_to(m)

    mapfile = "map.html"
    m.save(mapfile)
    webbrowser.open(mapfile)
    return
