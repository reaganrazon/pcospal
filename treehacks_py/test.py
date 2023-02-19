# import iris

# hostname="k8s-743d0686-a6e900d2-91ad558ada-e138f0bd75318090.elb.us-east-1.amazonaws.com"
# port=1972
# namespace="USER"
# connection_string=hostname+':'+str(port)+'/'+namespace
# username="SQLAdmin"
# password="B!pM7XVUjuj11"
# connection = iris.connect(connection_string, username=username, password=password)

# cursor = connection.cursor()
# def execute_sql_commands(cursor, commands_list):
#     for command in commands_list:
#         cursor.execute(command)


# drop_user_table="DROP TABLE IF EXISTS user_table"
# execute_sql_commands(cursor, [drop_user_table])

# create_user_table= "CREATE TABLE user_table(follicle_r int, follicle_l int, weight_gain int,  hair_growth int, skin_darkening int,  cycle_r int,  fast_food float,  pcos int)"
# execute_sql_commands(cursor, [create_user_table])