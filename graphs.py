import function
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np


def top_graph(result_df):
    watched_fig= make_subplots(rows=2, cols= 1,
                               subplot_titles=("Most rented films", "Least rented films"))


    watched_fig.add_trace(go.Bar(
        x= result_df["title"].iloc[:15],
        y= result_df["number_of_occurrences"],
        marker= dict(
            color= result_df["number_of_occurrences"],
            colorscale="Viridis")),
        row= 1, col= 1)
    
    watched_fig.add_trace(go.Bar(
        x= result_df["title"].iloc[-15:],
        y= result_df["number_of_occurrences"].iloc[-15:],
        marker= dict(
            color= result_df["number_of_occurrences"],
            colorscale="Viridis_r")),
        row= 2, col= 1)

    watched_fig.update_yaxes(title_text= "Times rented", 
                            row= 1, col= 1)
    watched_fig.update_yaxes(title_text= "Times rented", 
                            row= 2, col= 1)
    
    watched_fig.update_annotations(font_size=20)


    path= f"{function.cwd()}\\graphs\\top.html"


    watched_fig.write_html(path)


def popular_graph(pop_df):
    x_m= [pop_df["YM"], pop_df["title"]]
    

    popular_fig= go.Figure(go.Bar(
        x= x_m,
        y= pop_df["rented_per_month"],
        marker_color= pop_df["color"],
        customdata= np.transpose([pop_df['title'], pop_df['genre']]),
        hovertemplate= 'Amount: %{y} <br>%{x} <br>%{customdata[1]}'))


    popular_fig.update_layout(
        barmode="relative",
        title= dict(
            text= "Top 15 rentals per month",
            x= 0.5,
            font= dict(size=22)),
        yaxis_title= dict(
            text= "Times rented",
            font= dict(size=18)))


    path= f"{function.cwd()}\\graphs\\popular.html"
    popular_fig.write_html(path)


def actor_graph(act_df):
    actor_fig= make_subplots(rows= 2, cols= 1,
                             subplot_titles= ("Most rented actors", "Least rented actors"))


    actor_fig.add_trace(go.Bar(
        x= act_df["full_name"].iloc[:15],
        y= act_df["times_in_film"].iloc[:15],
        marker= dict(
            color= act_df["times_in_film"],
            colorscale="Viridis")),
            row= 1, col= 1)
    

    actor_fig.add_trace(go.Bar(
        x= act_df["full_name"].iloc[-15:],
        y= act_df["times_in_film"].iloc[-15:],
        marker= dict(
            color= act_df["times_in_film"],
            colorscale="Viridis_r")),
            row= 2, col= 1)
    
    actor_fig.update_layout(showlegend=False)

    path= f"{function.cwd()}\\graphs\\actor.html"
    actor_fig.write_html(path)


def revenue_graph(rev_df):
    revenue_fig= go.Figure(go.Pie(
        labels= rev_df['year_and_month'],
        values= rev_df['income'],
        texttemplate= "%{label} <br> %{value:$,s} <br>(%{percent})",
        hole= 0.6))

    revenue_fig.update_traces(
        hoverinfo= 'label+percent')
    revenue_fig.update_layout(
        title= dict(
            text= "Rental Income per month",
            x= 0.5,
            font= dict(size=22)),
        annotations= [dict(
            text=f"Total: ${sum(rev_df['income'])}", 
            x=0.5, y=0.5, 
            font_size=20, 
            showarrow=False)])


    path= f"{function.cwd()}\\graphs\\revenue.html"
    revenue_fig.write_html(path)