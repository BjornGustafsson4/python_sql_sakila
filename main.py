import function
import queries
import graphs


function.folder_create()
login_dic= function.login()


top_result= queries.top_rentals(login_dic)
graphs.top_graph(top_result)


popular_df= queries.popular(login_dic)
graphs.popular_graph(popular_df)


actor_df= queries.actors(login_dic)
graphs.actor_graph(actor_df)


rev_df= queries.revenue(login_dic)
graphs.revenue_graph(rev_df)


function.graph_open()