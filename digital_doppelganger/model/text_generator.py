from transformers import pipeline

def generate_response(prompt, user_style):
    generator = pipeline("text-generation", model="gpt-3")
    input_text = f"Style: {user_style}\nPrompt: {prompt}"
    response = generator(input_text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
