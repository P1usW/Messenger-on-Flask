import json
import requests
from flask import current_app

def translate(texts, target_language) -> json:

    folder_id = current_app.config['FOLDER_ID_YANDEX']
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }
    IAM_TOKEN = current_app.config['IAM_TOKEN_YANDEX']

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    return json.loads(response.content.decode('utf-8-sig'))['translations'][0]['text']


