from transformers import pipeline

# Create a text generation pipeline
nlp_model = pipeline('text-generation', model='gpt2')

def get_ai_response(player_input):
    response = nlp_model(player_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

# Example usage
player_input = "I'm stuck in this level. How can I beat the boss?"
ai_response = get_ai_response(player_input)
print(ai_response)
