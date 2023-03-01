import function
import plotly.graph_objects as go
import numpy as np


def top_graph(result_df, name):
    most_watched= go.Figure([go.Bar(
        x= result_df["title"],
        y= result_df["number_of_occurrences"],
        marker= dict(
        color= result_df["number_of_occurrences"],
        colorscale="Viridis",
        )
    )])
    

    most_watched.update_layout(
        title= dict(
            text= "Most rented films",
            font= dict(
                family= "Open Sans",
                size=22)),
        xaxis_title= dict(
            text= "Times rented",
            font= dict(
                family= "Open Sans",
                size=18)),
        yaxis_title= dict(
            text= "Name of movie",
            font= dict(
                family= "Open Sans",
                size=18)),
        font= dict(
            family= "Open Sans",
            size=10))

    path= f"{function.cwd()}\\graphs\\{name}.html"
    most_watched.write_html(path)


def popular_graph(pop_df, name):
    x_m= [pop_df["YM"], pop_df["title"]]
    
    popular_fig= go.Figure(go.Bar(
        x= x_m,
        y= pop_df["rented_per_month"],
        marker_color= pop_df["color"],
        customdata= np.transpose([pop_df['title'], pop_df['genre']]),
        hovertemplate= 'Amount: %{y} <br>%{x} <br>%{customdata[1]}'
    ))

    popular_fig.update_layout(barmode="relative")

    path= f"{function.cwd()}\\graphs\\{name}.html"
    popular_fig.write_html(path)