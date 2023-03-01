import function
import queries
import graphs
import time


#remove later
start = time.time()


function.folder_create()
login_dic= function.login()


graph_name= "top"
top_result= queries.top_rentals(login_dic)
graphs.top_graph(top_result, graph_name)


graph_name= "popular"
popular_df= queries.popular(login_dic)
graphs.popular_graph(popular_df, graph_name)


function.graph_open()


#remove later
end= time.time()
total= (end - start) * 10**3
print(f"Execution time: {total} ms")