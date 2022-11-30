import sys
from transformers import pipeline, set_seed


# 5 texts with a length of 350 are generated
def get_context(question):
    generator = pipeline('text-generation', model='malteos/gpt2-xl-german-covid-19')
    set_seed(42)
    context = generator(question, max_length=350, num_return_sequences=5, do_sample=True, pad_token_id=50256)
    return context

def best_answer(question):
    answers = []
    dict_contexts = get_context(question)

    for unit in dict_contexts:
        contexts = [unit['generated_text']]
        questions = [question]

        qa_pipeline = pipeline(
        "question-answering",
        model="svalabs/rembert-german-question-answering",
        tokenizer="svalabs/rembert-german-question-answering"
        )        
        answers.append(qa_pipeline(context=contexts, question=questions, max_answer_len = 200))
        
    best_score = max(unit['score'] for unit in answers)
    for unit in answers:
        if best_score == unit['score']:
            return unit['answer']

        
if __name__ == "__main__":
    question = input("Please enter a question: ")
    while question != "Bye":
        answer = best_answer(question)
        print("Answer: {}\n".format(answer))
        question = input("Please enter a question: ")
