def summarize_text(text):
    if isinstance(text, str):
        words = text.split()
        return " ".join(words[:100]) + "..."
    return "Cannot summarize tabular data."
