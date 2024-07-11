import json
import os
from azure.functions import HttpRequest, HttpResponse
import openai

# Access the environment variable
openai.api_key = os.environ["sk-proj-vysI1nI3blSjEW3zXgw5T3BlbkFJ9YIbWTlobqwmmqixNg4X"]

def main(req: HttpRequest) -> HttpResponse:
    movie_id = req.params.get('movie_id')
    if not movie_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            movie_id = req_body.get('movie_id')

    if movie_id:
        # Example movie data
        movie = {"title": "Movie 1", "year": 2022}

        # Generate summary using OpenAI API (dummy example, replace with actual API call)
        summary = f"Summary of {movie['title']} released in {movie['year']}."

        return HttpResponse(json.dumps({"summary": summary}), mimetype="application/json", status_code=200)
    else:
        return HttpResponse(
            "Please pass a movie_id on the query string or in the request body",
            status_code=400
        )
