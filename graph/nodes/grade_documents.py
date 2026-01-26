from typing import Dict, Any
from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Arguments:
        state (dict): The current state of the graph

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """
    print("----CHECK DOCUMENT RELEVANT TO QUESTION----")

    question = state["question"]
    documents = state.get("documents") or []

    filtered_docs = []
    web_search = False
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )

        grade = score.binary_score

        if isinstance(grade, str) and grade.lower() == "yes":
            print("-----GRADE: DOCUMENT RELEVANT TO QUESTION----")
            filtered_docs.append(d)
        else:
            print("-----GRADE: DOCUMENT NOT RELEVANT TO QUESTION----")
            web_search = True
            continue

    if not filtered_docs:
        web_search = True

    return {"question": question, "documents": filtered_docs, "web_search": web_search}