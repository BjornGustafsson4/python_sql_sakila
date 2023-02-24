import connect
import queries
import graphs
import time


#remove later
start = time.time()


login_dic= connect.login()


#top20_result= queries.top_rentals(login_dic)
#graphs.top20_graph(top20_result)


popular_df= queries.popular(login_dic)
graphs.popular_graph(popular_df)


#remove later
end= time.time()
total= (end - start) * 10**3
print(f"Execution time: {total} ms")