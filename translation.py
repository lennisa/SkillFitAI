from deep_translator import GoogleTranslator

def translate_answers(answers, language):

    if language == "English":
        return answers

    translated_answers = []

    for ans in answers:

        try:

            translated = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(ans)

            translated_answers.append(
                translated
            )

        except Exception:

            translated_answers.append(ans)

    return translated_answers