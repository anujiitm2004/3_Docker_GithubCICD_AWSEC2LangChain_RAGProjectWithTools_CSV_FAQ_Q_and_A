import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db
from langchain_helper import llm
from langchain_core.messages import HumanMessage

st.title("Codebasics Q&A 🌱")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

# if question:
#
#     # chain = get_qa_chain()
#     #Anuj
#     print("-------chain printing--------")
#     #print(chain)
#     print("-------chain printing end--------")
#
#     # Anuj end
#     response = get_qa_chain(question)
#
#     st.header("Answer")
#     st.write(response["result"])
if question:
    result = get_qa_chain(question)

    st.header("Answer")

    if isinstance(result, list) and len(result) == 3:
        # Tool-based result (llm.invoke().content)
        st.write(result[1])
        st.caption(f"🔧 Answer generated using TOOL. The tool Name is : `{result[0]}'")
        # st.code("\n\n".join([str(m) for m in result[1]]))
        # for item in result[1]:
        #     st.code(print(item))
        #     st.code(print())

        st.code(result[2])
    elif isinstance(result, dict) and "result" in result:
        # Vectorstore Retrieval result
        st.write(result["result"])
        st.caption("📚 Answer generated using VECTORSTORE")
        filled_prompt = result["PROMPT"].format(**result["input"])
        st.subheader("🧠 Filled Prompt Used by LLM:")
        st.code(filled_prompt)
        # if result["source_documents"]:
        #     st.subheader("📄 Source Documents")
        #     for i, doc in enumerate(result["source_documents"]):
        #         st.markdown(f"**Source {i + 1}:**")
        #         st.code(doc.page_content)

    else:
        st.write("⚠️ Unexpected response format.")


# if __name__ == "__main__":
#         # Tool test
#         query = HumanMessage("Can you multiply 6 by 9?")
#         tool_response = llm.invoke([query])
#         print("TOOL TEST OUTPUT:")
#         print(tool_response)







