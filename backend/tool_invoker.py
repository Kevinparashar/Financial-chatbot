from tools.summarizer import summarize_text
from tools.csv_analyzer import analyze_data
from tools.visualizer import plot_trend
from tools.comparator import compare_docs
from tools.web_reader import summarize_web_content
from tools.translator import translate_response

def invoke_tool(intent, file_data, query):
    if intent == "summarize":
        return summarize_text(file_data)
    elif intent == "analyze":
        return analyze_data(file_data, query)
    elif intent == "visualize":
        return plot_trend(file_data, query)
    elif intent == "compare":
        return compare_docs(file_data, query)
    elif intent == "web_summary":
        return summarize_web_content(query)
    elif intent == "translate":
        return translate_response(file_data, query)
    else:
        return "Sorry, I couldn't understand the request."