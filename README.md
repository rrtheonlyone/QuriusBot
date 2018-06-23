# QuriusBot Server
----
This server uses python's NLTK library to perfrom natural language processing on raw html to analyse its content, understand its meaning and generate a summary along with quiz questions for it.

## Setup:
1. Install dependencies
2. Sign up for Microsoft Cognitive API to get a key
3. Store API Key in util/secrets.py as ocp_key
4. Run `app.py`

## API Documentation:

### Summary ###
Returns json containing summary and related links for a html webpage.

* **URL**

  /summary

* **Method:**

  `POST`

* **Data Params**

  `data=[string]` where data is the raw html

* **Success Response:**

  * **Code:** 200
    **Content:** `{ summary : "This is a summary", related_links : [{title: "Title1", link: "Link1"}, {title: "Title2", link: "Link2"}]`

### Quiz
Returns json containing quiz questions for any html_webpage

* **URL**

  /quiz

* **Method:**

  `POST`

* **Data Params**

  `data=[string]` where data is the raw html

* **Success Response:**

  * **Code:** 200
    **Content:** `[{"question": "Question1", "type": "FILL_IN_THE_BLANKS", answer: "Answer1"}, {"question": "Question2", "type": "True_False", answer: "Answer1"}]
