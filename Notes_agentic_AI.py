# Given what you see in the out put what information  does ypur code 
# need to pull out of this response in orger to actually run the right function

# The code needs:
# 1. name - which function to call ('get_weahter')
# 2/ input - the argumnents to call it with ({'city': 'Charleston'})

# Example: If you think about a phone message someone left you: 
# "Call Sarah, ask her about the meeting." You need WHO TO CALL and 
# WHAT TO SAY. 

# Two pieces, and "what to say" already contains the specific content
# (the meeting), that is not a third separte item


# walk through and explain these following lines
# def get_weather(city):
#     return f"weather for {city}"

# tool_map = {"get_weather": get_weather}

# func = tool_map["get_weather"]
# result = func("Charleston")
# print(result)

# Line 120 creates a function named get_weather with an argument city
# Line 121 returns the weather for the given city
# Line 123 the get_weather function is being stored as the get weather key
# and the get weather key is being stored in key map

# Line 125 func is storing whatever value is behing the key "get_weahter" inside
# too map. Since the actual vaule stored in in tool map is the function get_weather 
# is a not a string but a function. Func is now the get_weather function - just 
# under a different name. Func and get weather are now the same thing

# Line 126 func is the same thing as get_weather so we are calling the function
# get_weather of Charleston 

# so the out put would return the weahter for charleston