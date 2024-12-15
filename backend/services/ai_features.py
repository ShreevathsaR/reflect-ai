from transformers import pipeline

def generate_ai_response(journal_text):

    sentiment_result = sentiment_analysis(journal_text)
    return {"Sentiment result": f"{sentiment_result}"}


def sentiment_analysis(journal_text):
    sentiment_pipeline = pipeline('sentiment-analysis', model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')

    journal_text = journal_text.json()

    print(journal_text)

    result = sentiment_pipeline(journal_text)
    return(result)