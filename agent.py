from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from tools import get_weather, get_joke, get_news

# Load knowledge
documents = TextLoader("data.txt").load()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embeddings)

# LLM pipeline
pipe = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=100,
    do_sample=False,
    repetition_penalty=1.2
)
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt template
prompt = PromptTemplate.from_template(
    "Answer briefly using the context.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
)

retriever = db.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

qa_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

def ask_agent(query):
    q = query.lower()

    if "weather" in q:
        city = query.split()[-1]
        return get_weather(city)

    if "joke" in q:
        return get_joke()

    if "news" in q:
        return get_news()

    result = qa_chain.invoke(query)
    return result.split("Question:")[0].strip()