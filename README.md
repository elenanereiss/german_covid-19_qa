# German COVID-19 Question Answering Pipeline

This repository contains a simple COVID-19 Question Answering pipeline for German. It uses a [German GPT2 model](https://huggingface.co/malteos/gpt2-xl-german-covid-19) that generates a context and a [German RemBERT model](https://huggingface.co/svalabs/rembert-german-question-answering) that extracts an answer.

To start Question Answering you need to install huggingface transformers with the command `pip install transformers`.

To start pipeline run `python3 ask.py`. You can enter a question in the terminal. To stop pipeline enter `Bye`. This look like:

```bash
/home/user/german_covid-19_qa> python3 ask.py
Please enter a question: Wie kann ich mich und andere vor einer Ansteckung schützen?
Answer:
Schutz vor einer Übertragung bietet eine gute medizinische Grundversorgung mit einem vollständigen Impfschutz, z. B. mit AstraZeneca oder Johnson&Johnson und eine lokale Behandlung der Symptome.

Please enter a question: Wie wird die 7-Tage-Hospitalisierungsinzidenz berechnet?
Answer:
Die Anzahl der wöchentlichen Hospitalisierungen je 100.000 Einwohner innerhalb von sieben Tagen ohne Berücksichtigung der Daten zur Zahl der Neuinfektionen in einer Stadt werden durch die Hospitalisierungsinzidenz multipliziert. Die Werte werden mit 100.000 (gerundet) berechnet, indem die jeweiligen Krankenhäuser jeweils durch 100.000 geteilt werden.

Please enter a question: Bye
```
