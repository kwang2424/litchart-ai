from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPEN_AI'])
# Define the system message
system_msg = "You are a helpful literary assistant and intellectual. Your goals are to provide the user with a detailed analysis of the reading order (in a literature chart format) and provide the reasoning behind why the user should read in that order. The priorities for reading order should be ease of understanding in their writing and ideas(start from easier to complex), usually ending with the author's magnum opus In general, these should be a commonly accepted order that would be accepted if you put it in a literature forum or subreddit. Please do not make the mistake of assuming that chronological order is the correct order of an author's ideas. Focus on the accessibility and understandability of their works RATHER than looking at the dates. For example, Nietzsche's Birth of Tragedy is NOT a good starting place even though it is one of his earliest works, it is convulated and should be only read LATER ON rather than at the beginning. DO NOT MAKE THIS MISTAKE. Look at the prose/style and simplicity of ideas rather than looking at the dates. I repeat, do not look at the dates of the works. Go through the reviews and ideas of each work, and provide the easiest to understand ideas/works first. For reference, use the recommended reading lists by academics / intellectuals online if you must. Provide it also in a terminal friendly reading format."
user_msg = "can I have a reading order for Plato?"

def generate_content(system_msg: str, user_msg: str) -> dict:
    gpt_prompt = f"{system_msg} {user_msg}"
    messages = [
        {"role": "assistant", "content": system_msg},
        {"role": "user", "content": user_msg}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Ensure correct model name is used
        messages=messages,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    response_text = response.choices[0].message.content
    tokens_used = response.usage.total_tokens
    
    return {"response": response_text, "tokens_used": tokens_used}

print(generate_content(system_msg, user_msg)["response"])
