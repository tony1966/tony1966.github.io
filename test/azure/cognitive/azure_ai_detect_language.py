import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client(endpoint, key):
    credential=AzureKeyCredential(key)
    client=TextAnalyticsClient(endpoint=endpoint,
                               credential=credential)
    return client

if __name__ == '__main__':
    load_dotenv()
    key=os.environ.get('AZURE_AI_API')
    endpoint='https://tony-test1.cognitiveservices.azure.com/'
    client=authenticate_client(endpoint, key)
    docs=['我爱你',
          "Je t'aime",
          'I love you',
          '我愛你',
          '愛してます',
          '사랑해요']
    response=client.detect_language(documents=docs)
    for id, r in enumerate(response):   
        print(f'"{docs[id]}" : {r.primary_language.name}')  