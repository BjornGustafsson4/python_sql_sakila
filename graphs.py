import plotly.graph_objects as go


def top20_graph(result_df):
    most_watched= go.Figure([go.Bar(
        x= result_df["title"],
        y= result_df["number_of_occurrences"],
        marker_color="fuchsia"
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


    most_watched.show()


def popular_graph(result_df):
    x_m= [
        result_df["YM"],
        result_df["title"]]
    
    
    popular_fig= go.Figure(go.Bar(
        x= x_m,
        y= result_df["rented_per_month"]
    ))


    popular_fig.update_layout(barmode="relative")

    popular_fig.show()