<h1>«Расширение набора текстовых данных путем перефразирования исходных данных»</h1>

Входные данные: предложения с различной степенью семантической и синтаксической изменчивости
Выходные данные: новые варианты перефразированных предложений для введенных пользователем на вход данных

Язык исходного текста: английский

Используемые технологии:
* язык программирования Python
* предобученные модели сетей:
  - [BERT](https://github.com/google-research/bert)
  - [T5](https://research.google/blog/exploring-transfer-learning-with-t5-the-text-to-text-transfer-transformer/)
  - [GPT-2](https://openai.com/index/better-language-models/)
* библиотека [transformers](https://huggingface.co/docs/transformers/main_classes/pipelines) HuggingFace

Источники:
1. Qizhe Xie, Zihang Dai, Eduard Hovy, Minh-Thang Luong, Quoc V. Le Unsupervised Data Augmentation for Consistency Training ([статья](https://arxiv.org/abs/1904.12848) [код](https://github.com/google-research/uda)) – метод back translation
2. Ekin D. Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, Quoc V. Le AutoAugment: Learning Augmentation Policies from Data ([статья](https://arxiv.org/abs/1805.09501)) – остальные методы
3. Su Wang, Rahul Gupta, Nancy Chang, Jason Baldridge A Task in a Suit and a Tie: Paraphrase Generation with Semantic Augmentation ([статья](https://arxiv.org/abs/1811.00119)) - методы оценки, архитектуры
4. Аугментация текста ([источник](https://nrao-prashanthi.medium.com/crafting-data-magic-how-paraphrasing-enhances-machine-learning-through-data-augmentation-a64cccdf80ca))
