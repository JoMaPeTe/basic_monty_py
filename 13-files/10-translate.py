from translate import Translator

with open('message.txt','r') as my_message:
        message_text = my_message.read()
        print(f'Original message:{message_text}')
        print('Translating...')
        translator_de = Translator(to_lang='de')
        translator_ru = Translator(to_lang='ru')
        translation_de = translator_de.translate(message_text)
        translation_ru = translator_ru.translate(message_text)
        print(f'Translated message:{translation_de}')
        print('-------------------------------------------')
        print(f'Translated message:{translation_ru}')
        with open('translated_message_de.txt', 'w') as my_translation_de:
            text = my_translation_de.write(translation_de)

        with open('translated_message_ru.txt', 'w', encoding='utf-8') as my_translation_ru:
            text = my_translation_ru.write(translation_ru)
        