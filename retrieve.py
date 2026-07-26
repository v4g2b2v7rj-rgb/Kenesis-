import sqlite3
from functions import env_format_memory, format_user_memory, get_all_env,search_env_memory

# rows = get_all_env()
# print(env_format_memory(rows))
thing = "macbook"
search = search_env_memory(thing)
print(search)

