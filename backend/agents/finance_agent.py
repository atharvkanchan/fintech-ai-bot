
def advice(summary):
    if not summary: return "No data"
    top = max(summary, key=summary.get)
    return f"Reduce spending in {top}"
