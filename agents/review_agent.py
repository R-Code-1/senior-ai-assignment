import openai, os, json
openai.api_key = os.getenv("OPENAI_API_KEY")
SYSTEM_PROMPT = """You are an intelligent agent that categorizes app reviews. For each review, return the topic (e.g., "Delivery partner rude"), category (issue/request/feedback), and reason in JSON format."""
def classify_review(review_text):
    resp = openai.ChatCompletion.create(
        model="gpt-4o", messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":f"Review: {review_text}"}
        ], temperature=0.3
    )
    output = resp['choices'][0]['message']['content']
    try:
        return json.loads(output)
    except:
        return {"topic":"uncategorized","category":"unknown","reason":"parse error"}