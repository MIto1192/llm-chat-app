from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.chains import RetrievalQA

# from langchain.memory import ConversationBufferMemory


def ask_question(question: str) -> str:
    llm = OpenAI(model_name="gpt-3.5-turbo")
    template = """Question: {question}

    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer = llm_chain.run(question)
    return answer

# 元ver
# def create_conversational_chain():
#     llm = OpenAI(model_name="gpt-3.5-turbo")
#     template = """あなたは関西弁を巧みに使いこなす親切で気のいい狐です。人間と会話をしています。

# {chat_history}
# 人間: {input}
# 狐:"""
#     prompt = PromptTemplate(
#         input_variables=["chat_history", "input"], template=template
#     )
#     memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history")
#     chain = LLMChain(
#         llm=llm,
#         prompt=prompt,
#         verbose=True,
#         memory=memory,
#     )
#     return chain

# 会話履歴考慮しない（pipeline使用ver）
# def create_conversational_chain():
#     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#     template = """あなたは関西弁を巧みに使いこなす親切で気のいい狐です。人間と会話をしています。
#                     人間: {input}
#                     狐:"""
#     print(template)
#     prompt = PromptTemplate(
#         input_variables=["input"], template=template
#     )
#     chain = prompt | llm
#     return chain

# 会話履歴の情報を使用するタイプ(添付ファイルなし用)
# def create_conversational_chain():
#     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#     template = """あなたは関西弁を巧みに使いこなす親切で気のいい狐です。人間と会話をしています。
#                     {chat_history}
#                     人間: {input}
#                     狐:"""
#     print(template)
#     prompt = PromptTemplate(
#         input_variables=["input"], template=template
#     )
#     memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history")
#     chain = LLMChain(
#         llm=llm,
#         prompt=prompt,
#         verbose=True,
#         memory=memory,
#     )
#     return chain

# 会話履歴の情報を使用するタイプ(添付ファイルあり・シンプル)
def create_conversational_chain():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    template =  """# 命令書:
                    あなたは関西弁を巧みに使いこなす親切で気のいい狐です。人間と会話をしています。
                    以下のファイル内容を参考情報として会話内容を続けてください。
                  # ファイル内容:
                   {context}
                  # 会話内容:  
                    {chat_history}
                    人間: {input}
                    狐:{human_input}"""

    print(template)
    prompt = PromptTemplate(
        input_variables=["input", "context","chat_history","human_input",], template=template
    )
    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history",input_key="human_input")
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,
    )
    return chain

# 以下は今後作成予定
# 会話履歴の情報を使用するタイプ(添付ファイルあり用・embeddingを用いて入力テキストに類似度高い情報のみ参考情報に埋め込み)
# def create_conversational_chain():
#     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#     template =  """# 命令書:
#                     あなたは関西弁を巧みに使いこなす親切で気のいい狐です。人間と会話をしています。
#                     以下の参考情報をもとに会話内容を続けてください。
#                   # 参考情報:
#                    {context}
#                   # 会話内容:  
#                     {chat_history}
#                     人間: {input}
#                     狐:"""

#     print(template)
#     prompt_qa = PromptTemplate(
#         input_variables=["context", "question"], template=template
#     )
#     chain_type_kwargs = {"prompt": prompt_qa}
#     memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history")
#     chain = LLMChain(
#         llm=llm,
#         prompt=prompt,
#         verbose=True,
#         memory=memory,
#     )
#     return chain
