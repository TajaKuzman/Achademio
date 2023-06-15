# Achademio - an AI-based assistant for writing research papers

An AI assistant, based on the GPT-3.5 model by OpenAI, that will improve your efficienty in writing research papers. It can:
- rewrite your text in academic style
- write a paragraph in academic style from your bullet point list
- proofread your text and higlight the errors

Let me know if you would like to have any other functionalities!

Use:
1. Clone this repository.
2. Install streamlit: `pip install streamlit install pip-run --user` and streamlit-chat: `pip install streamlit_chat`
3. Create an OpenAI account to get a API key (see https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0). Save the API key in line 5 of `achademio.py` or in a separate file (make sure that you do not share it with anyone). The model is based on the GPT-3.5 model which will cost you $0.0015/1K tokens for input and $0.002/1K tokens. You can track your expenses in the `Manage account` menu item under `Personal` at https://platform.openai.com/. New users get $18 for free, so the service won't cost you anything at the start.
4. Run the streamlit python script in your command line with the following command: `python -m streamlit run achademio.py`
5. A website will open in your browser where you can use the chatbot to improve your academic texts.