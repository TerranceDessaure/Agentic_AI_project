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

# Why the LLM can't directly execute code ( it only outputs with structure intent)
#
# An LLM doesn't directly execute code because it its mainly designed to understand
# and generate text, not run programs. Instead, it produces a structured intent or tool
# call describing what need to be done. Then, a separate tool or runtime actually excutes
# the code and sends the result back to the LLM. This separation also helps keep the system 
# secure and controlled

# Why the tool description text matters so much (it's the only thing the model sees to decide)
#
# Too descriptions matter because they're basically the model's instructions for how and when to
# a tool. The model relies on that description to understand what the tool does, what inputs it needs,
# and when it's appropriate to call it. So, if the description  is unclear or incomplete, the model can
# easily choose the wrong tool or use it incorrectly.

# Why .name and .input are separate fields doing separte jobs
#
# the raw output we got earlier was 
# ToolUseBlock(input={'city': 'Charleston'}, name='get_weather', ...)
# . name holds 'get_weather'  and get_weather holds the funcion get weather
# .input hold the key city and the city is assigned is in Charleston

# Why dictionary lookup (tool_map[...]) is the bridge between "a string the model gave you"
# and an actual calliable function
#
# The dictionary lookup is the bridge because the model only gives us a tool name
# as a string, not the actual function. tool_map[...] takes that name and finds the 
# corresponding callable function in our code. In other words, it turns the model's "I want to use
# this tool" into "here's the actual function to run."


