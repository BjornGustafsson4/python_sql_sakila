import function
import plotly.graph_objects as go
import numpy as np


def top_graph(result_df):
    watched_fig= go.Figure([go.Bar(
        x= result_df["title"],
        y= result_df["number_of_occurrences"],
        marker= dict(
            color= result_df["number_of_occurrences"],
            colorscale="Viridis"
        ))])
    

    watched_fig.update_layout(
        title= dict(
            text= "Most rented films",
            x= 0.5,
            font= dict(size=22)),
        xaxis_title= dict(
            text= "Name of movie",
            font= dict(size=18)),
        yaxis_title= dict(
            text= "Times rented",
            font= dict(size=18)))


    path= f"{function.cwd()}\\graphs\\top.html"
    watched_fig.write_html(path)


def popular_graph(pop_df):
    x_m= [pop_df["YM"], pop_df["title"]]
    

    popular_fig= go.Figure(go.Bar(
        x= x_m,
        y= pop_df["rented_per_month"],
        marker_color= pop_df["color"],
        customdata= np.transpose([pop_df['title'], pop_df['genre']]),
        hovertemplate= 'Amount: %{y} <br>%{x} <br>%{customdata[1]}'
    ))


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
    actor_fig= go.Figure([go.Bar(
        x= act_df["full_name"],
        y= act_df["times_in_film"],
        marker= dict(
            color= act_df["times_in_film"],
            colorscale="Viridis"
        ))])
    

    actor_fig.update_layout(
        title= dict(
            text= "Most watched staring actors",
            x= 0.5,
            font= dict(size=22)),
        xaxis_title= dict(
            text= "Name of actor",
            font= dict(size=18)),
        yaxis_title= dict(
            text= "Times in rented movie",
            font= dict(size=18)))

    path= f"{function.cwd()}\\graphs\\actor.html"
    actor_fig.write_html(path)


def revenue_graph(rev_df):
    revenue_fig= go.Figure(go.Pie(
        labels= rev_df['year_and_month'],
        values= rev_df['income'],
        hole= 0.6,
    ))

    revenue_fig.update_traces(
        hoverinfo= 'label+percent', 
        textinfo= 'label+value')
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