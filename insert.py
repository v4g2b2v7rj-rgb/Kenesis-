from functions import gen_object_action, insert_env_data

obj, act, time_state, Date, importance = gen_object_action()

print(insert_env_data(obj, act, time_state, Date, importance))
