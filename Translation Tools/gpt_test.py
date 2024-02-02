from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """\
You are a Translator helping me Translate the text contents of the game pokemon fire red from English to hebrew,
please translate accourding to the conventions below:
everything that is in brackets [] keep it in english adn in brackets in the correct location in the sentence.
Special charcters are to be kept as they are, with no translation, special charcters are words that starts with a \.

look at the following examples of my translations and learn from it how I translate words you are not familiar with:
Example 1:
PROF. OAK may not look like much,
but he's the authority on POKéMON.

Many POKéMON TRAINERS hold him in
high regard.
###Translated##
Translation:
פרופסור אוק אולי לא נראה ככה
אבל הוא איש מאוד חשוב
בעולם הפוקימונים."""},
    {"role": "user", "content": """OAK: Come see me sometime.

After all, I want to know how your
POKéDEX is coming along."""}
  ]
)

print(completion.choices[0].message)
