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


#Finds actors from most rented to least
def actors(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT CONCAT(a.first_name, ' ', a.last_name) AS full_name, COUNT(fa.actor_id) AS 'in_film' FROM film f "
                    "JOIN film_actor fa ON f.film_id = fa.film_id "
                    "JOIN actor a ON fa.actor_id = a.actor_id "
                    "GROUP BY fa.actor_id "
                    "ORDER BY in_film DESC;")
    result= cursor.fetchall()
    result_df = pd.DataFrame(result, columns=["full_name", "times_in_film"])
    return result_df


#Finds top 15 most popular rentals per month
def popular(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT i.film_id, f.title, c.name AS 'genre', COUNT(i.film_id) AS 'rentals_per_month', EXTRACT(YEAR_MONTH FROM r.rental_date) AS 'dates' FROM rental r "
        "JOIN inventory i ON r.inventory_id = i.inventory_id "
        "JOIN film f ON i.film_id = f.film_id "
        "JOIN film_category fc ON i.film_id = fc.film_id "
        "JOIN category c ON fc.category_id = c.category_id "
        "GROUP BY i.film_id, dates, genre "
        "ORDER BY dates, rentals_per_month DESC;")
    result= cursor.fetchall()
    pop_df = pd.DataFrame(result, columns=["id", "title", "genre", "rented_per_month", "YM"])
    ym_unique = np.unique(pop_df["YM"], return_index= True)
    ym_dic = dict(map(list, zip(*ym_unique)))
    result_df = pd.DataFrame(columns=["id", "title", "rented_per_month", "YM"])
    dicti = {}
    for ym in ym_dic:
        if ym == 200602:
            continue
        else:
            ym_index= ym_dic.get(ym)
            q= pd.DataFrame(pop_df.iloc[ym_index:(ym_index + 15)])
            dicti[ym] = np.sum(q["rented_per_month"])
            q.sort_values(by=["rented_per_month"])
            result_df= pd.concat([result_df, q])


    #Adds color to bars by finding the most and least rented months
    result_df["color"] = "gold"
    v = list(dicti.values())
    k = list(dicti.keys())
    top_g= ym_dic.get(k[v.index(max(v))])
    bottom_r= ym_dic.get(k[v.index(min(v))])
    result_df["color"].loc[top_g:top_g + 15] = "darkgreen"
    result_df["color"].loc[bottom_r:bottom_r + 15] = "crimson"


    #Fixes YM from YYYYMM to YYYY-MM
    for index in result_df.index:
        result_df["YM"][index] = f"{str(result_df['YM'][index])[:4]}-{str(result_df['YM'][index])[-2:]}"
    result_df = result_df.reset_index(drop= True)
    return result_df


#Finds revanue per month
def revenue(login_d):
    db_connect= function.sql_connect(login_d)
    cursor= db_connect.cursor()
    cursor.execute("SELECT SUM(p.amount) as 'amount', EXTRACT(YEAR_MONTH FROM r.rental_date) as 'year_and_month' FROM rental r "
                    "JOIN payment p ON r.rental_id = p.rental_id "
                    "GROUP BY year_and_month "
                    "ORDER BY year_and_month;")
    result= cursor.fetchall()
    result_df = pd.DataFrame(result, columns=["income", "year_and_month"])
    for index in result_df.index:
        result_df["year_and_month"][index] = f"{str(result_df['year_and_month'][index])[:4]}-{str(result_df['year_and_month'][index])[-2:]}"
        if result_df["year_and_month"][index] == "2006-02":
            result_df["year_and_month"][index] = f"{result_df['year_and_month'][index]} (incomplete)"
    return result_df