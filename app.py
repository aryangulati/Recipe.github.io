import gradio as gr
from transformers import pipeline

# Load a pre-trained model from Hugging Face
generator = pipeline("text-generation", model="gpt2")  # You can replace 'gpt2' with a more specific model if needed.

# Function to generate recipe suggestions
def suggest_recipe(ingredients):
    if not ingredients.strip():
        return "Please provide some ingredients!"
    
    prompt = f"I have these items in my fridge: {ingredients}. What can I make?"
    try:
        # Generate text with the model
        result = generator(prompt, max_length=100, temperature=0.7, num_return_sequences=1)
        return result[0]["generated_text"]
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=suggest_recipe, 
    inputs=gr.Textbox(label="Enter ingredients (separated by commas)"), 
    outputs=gr.Textbox(label="Recipe Suggestions"), 
    title="Recipe Suggestion AI",
    description="Enter ingredients you have in your fridge, separated by commas, and get recipe ideas!"
)

# Launch the app
iface.launch()
