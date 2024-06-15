from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def back_translation(input_text):
    #English to German using the Pipeline and T5
    translator_en_to_de = pipeline("translation_en_to_de", model='t5-base')
    #Germal to English using Bert2Bert model
    tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_de_en", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
    model_de_to_en = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_de_en")

    en_to_de_output = translator_en_to_de(input_text)
    translated_text = en_to_de_output[0]['translation_text']
    print("Translated text->",translated_text)
    #Ich ging ins Kino, um einen Film zu sehen.

    input_ids = tokenizer(translated_text, return_tensors="pt", add_special_tokens=False).input_ids
    output_ids = model_de_to_en.generate(input_ids)[0]
    augmented_text = tokenizer.decode(output_ids, skip_special_tokens=True)
    print("Augmented Text->",augmented_text)
    #I went to the cinema to see a film.

back_translation("I went to see a movie in the theater")