import gradio as gr
import requests

API_URL = "http://localhost:8000/ask"

def query_agent(user_query):
    try:
        response = requests.post(API_URL, json={"query": user_query})
        if response.ok:
            return response.json().get("response", "No response received.")
        else:
            return f"❌ Error: {response.status_code}"
    except Exception as e:
        return f"⚠️ Exception: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## 🔍 SmolAgent Web Interface")

    with gr.Row():
        query_box = gr.Textbox(label="Enter your query", lines=2, placeholder="Ask something about Japan...")
        submit_btn = gr.Button("Ask")

    output_box = gr.Textbox(label="Response", lines=8)

    submit_btn.click(query_agent, inputs=[query_box], outputs=[output_box])

demo.launch()
