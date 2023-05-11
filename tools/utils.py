import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import folium 

# function to get the total number of counts of evictions per selected feature
def get_count_plot(df, feature):
    """
    This function aims to get the total counts of evictions for each category in a certain feature, and
    display the result in the form of a barplot.
    """
    # first get the data frame for the value counts
    counts_df = df[[feature]].value_counts().reset_index(name='counts')

    # specify the values for x-axis and y-axis
    x = list(counts_df[feature])
    y = list(counts_df['counts'])

    # plot the barplot
    fig, ax = plt.subplots()
    fig.set_figwidth(20)
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=8)
    plt.xlabel(feature, labelpad = 10)
    plt.ylabel('counts')
    plt.title("Number of Evictions per " + feature)
    plt.bar(x, y)
    
    
def reason_for_evict(df, names):
    """
    This function aims to get the total number of the reasons for eviction for each different reason,
    and display the result in the form of a barplot.
    The arugument 'names' is a list of the names for certain eviction reasons that you want to look into.
    """

    #self.names = names
    reasons = df[names]

    columnNames = reasons.columns

    # create an empty dictionary for the reasons that has TRUE input for future counts
    trues_oc = {}

    # get the total number of TRUE observations for each reason of eviction and print it 
    for i in reasons.columns:
        trues_oc[i] = reasons[i].sum()
    print(trues_oc)

    # make it into a dataframe for plotting purpose
    argh = pd.DataFrame(trues_oc, ['True'], columnNames).reset_index()
    #print(argh)

    # print the result
    reasons_list = [column for column in argh.columns]
    #print(reasons_list)
    reasons_bar = argh.plot(figsize=(8,5), x='index', y=reasons_list[1:], kind='bar', rot=0)
    plt.xlabel('Reasons', labelpad = 10)
    plt.ylabel('counts')
    plt.title("Reasons count for Different Reasons for Eviction")
    plt.legend(loc='best', fontsize='7')

# function to create heat map for counts of evictions in sf based on zip
def create_map(df, zips, feature, title_desc = ''):
    """
    This function aims to get the total number of the reasons for eviction per zip code on a map of sf.
    
    df = dataframe reading from
    zips = zips column name
    feature = desired feature
    title_desc = additional comments for title
    """
    
    sf_geo = r'/home/jovyan/sf_geojson/updated-file.json'
    # initiating a Folium map with LA's longitude and latitude
    m = folium.Map(location = [37.7749, -122.4194], zoom_start = 11)
    # creating a choropleth map
    m.choropleth(
        geo_data = sf_geo,
        fill_opacity = 0.7,
        line_opacity = 0.2,
        data = df,
        # refers to which key within the GeoJSON to map the ZIP code to
        key_on = 'feature.properties.id',
        # first element contains location information, second element contains feature of interest
        columns = [zips, feature],
        fill_color = 'RdYlGn',
        legend_name = (' ').join(feature.split(' ')).title() + ' ' + title_desc + ' Across SF'
    )
    folium.LayerControl().add_to(m)
    # save map with filename based on the feature of interest
    m.save(outfile = feature + '_map.html')

