import gzip
import base64
import json
import pprint
import requests
from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()


auth = os.environ["AUTH"]


headers = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
    "authorization": str(auth),
    "Referer": "https://plataforma.devopspro.com.br/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


def auto_dict():
    return defaultdict(auto_dict)


def decompress_gzip(data):
    compressed_data = base64.b64decode(data)

    decompressed_data = gzip.decompress(compressed_data)
    decodedString = decompressed_data.decode("utf-8")
    return decodedString


def get_course():
    final_json_data = auto_dict()
    # :)
    for id in range(1, 1057):

        baseUrl = f"https://portal.devopspro.com.br/api/cursos/conteudo/{id}.json"

        response = requests.get(baseUrl, headers=headers)

        if response.status_code == 200:
            r = response.json()["content"]
            data = json.loads(decompress_gzip(r))

            lectureID = data["id"]
            lectureTitle = data["titulo"]
            lectureModuleID = data["capitulo"]["id"]
            lectureModule = data["capitulo"]["nome"]
            courseModule = data["capitulo"]["curso"]["nome"]
            lectureUrl = data["video_url_bunny"]

            pprint.pp(
                f"{courseModule} - {lectureModule} - [{lectureID}] {lectureTitle}"
            )

            final_json_data[courseModule][f"[{lectureModuleID}] {lectureModule}"][
                f"[{lectureID}] {lectureTitle}"
            ] = lectureUrl

        else:
            print(f"Erro: {response.status_code}")
    return final_json_data


if __name__ == "__main__":
    courses = get_course()
    with open("devops-pro.json", "w", encoding="UTF-8") as f:
        json.dump(courses, f, indent=4, ensure_ascii=False)
    pprint.pp(courses)
