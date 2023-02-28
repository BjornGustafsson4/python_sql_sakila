import pandas as pd
import numpy as np
import function


#runs SQL query to find top rented shows
def top_rentals(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT f.title, COUNT(i.film_id) AS number_of_occurrences FROM rental r "
        "JOIN inventory i ON r.inventory_id = i.inventory_id "
        "JOIN film f ON i.film_id = f.film_id "
        "GROUP BY f.title ORDER BY number_of_occurrences DESC;")
    result= cursor.fetchall()
    result_df= pd.DataFrame(result, columns=["title", "number_of_occurrences"])
    return result_df


def rental_date(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT f.title, r.rental_date FROM rental r "
        "JOIN inventory i ON r.inventory_id = i.inventory_id "
        "JOIN film f ON i.film_id = f.film_id "
        "ORDER BY f.title, r.rental_date;")
    result= cursor.fetchall()
    result_df = pd.DataFrame(result, columns=["title", "rental_date"])
    return result_df


#Runs SQL query and finds top 15 per month
def popular(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT i.film_id, f.title, COUNT(i.film_id) AS 'rentals_per_month', EXTRACT(YEAR_MONTH FROM r.rental_date) AS 'dates' "
        "FROM rental r " 
        "JOIN inventory i ON r.inventory_id = i.inventory_id "
        "JOIN film f ON i.film_id = f.film_id "
        "GROUP BY i.film_id, dates "
        "ORDER BY dates, rentals_per_month DESC;")
    result= cursor.fetchall()
    pop_df = pd.DataFrame(result, columns=["id", "title", "rented_per_month", "YM"])
    ym_unique = np.unique(pop_df["YM"], return_index= True)
    ym_dic = dict(map(list, zip(*ym_unique)))
    result_df = pd.DataFrame(columns=["id", "title", "rented_per_month", "YM"])
    for ym in ym_dic:
        ym_index= ym_dic.get(ym)
        q= pd.DataFrame(pop_df.iloc[ym_index:(ym_index + 15)])
        result_df= pd.concat([result_df, q])
        result_df = result_df.reset_index(drop= True)
    for index in result_df.index:
        result_df["YM"][index] = f"{str(result_df['YM'][index])[:4]}-{str(result_df['YM'][index])[-2:]}"


    return result_df