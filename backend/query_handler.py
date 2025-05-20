def detect_intent(query):
    query = query.lower()
    if "summary" in query or "summarize" in query:
        return "summarize"
    elif "trend" in query or "chart" in query or "visualize" in query:
        return "visualize"
    elif "compare" in query or "difference" in query:
        return "compare"
    elif "average" in query or "total" in query or "stat" in query:
        return "analyze"
    elif "link" in query or "url" in query:
        return "web_summary"
    elif "translate" in query or "language" in query:
        return "translate"
    else:
        return "default"