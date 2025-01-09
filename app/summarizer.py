from langchain import OpenAI

def generate_summary(objects):
    llm = OpenAI(temperature=0.7)
    prompt = f"Crie um resumo para os seguintes objetos detectados: {', '.join(objects)}."
    return llm(prompt)
