import csv

from deep_translator import GoogleTranslator
from fuzzywuzzy import fuzz
from tqdm import tqdm

google_translator = GoogleTranslator(source='hi', target='en')

lexicons = {

}

with open('HI-toxicWords.csv', mode ='r') as file:
    csv_file = csv.DictReader(file)
    for lines in csv_file:
        split_connotations = lines['Negative Connotations'].split(',')
        for index, item in enumerate(split_connotations):
            item_list = item.strip().split()
            for token in item_list:
                if token not in lexicons and token not in ['का', 'कि', 'की', 'के']:
                    lexicons[token] = 0
                if token not in ['का', 'कि', 'की', 'के']:
                    lexicons[token] += 1

# Sort in alphabetical order
keys = list(lexicons.keys())
keys.sort()
sorted_lexicon = {key: lexicons[key] for key in keys}

english_slur = {

}

for item in tqdm(lexicons):
    english_slur[item] = google_translator.translate(item)

final_array_slur = {

}

done = []
for index1, lexicon in  enumerate(sorted_lexicon):
    array_slur = []
    total_slur = 0
    current_index = 0
    if index1 not in done:
        current_element = lexicon

        done.append(index1)
        total_slur += sorted_lexicon[current_element]
        # array_slur.append((current_element, sorted_lexicon[current_element]))
        array_slur.append((current_element, english_slur[current_element], sorted_lexicon[current_element]))

        while current_index < len(array_slur):
            for index2, lexicon_temp in enumerate(sorted_lexicon):
                if (index2 not in done and
                    ((fuzz.ratio(current_element, lexicon_temp) >= 80) or
                     (fuzz.ratio(current_element, lexicon_temp) >= 50 and fuzz.ratio(english_slur[current_element],
                                                                                     english_slur[lexicon_temp]) >= 80))):
                    done.append(index2)
                    total_slur -= sorted_lexicon[lexicon_temp]
                    # array_slur.append((lexicon_temp, sorted_lexicon[lexicon_temp]))
                    array_slur.append((lexicon_temp, english_slur[lexicon_temp], sorted_lexicon[lexicon_temp]))
            current_index += 1
            if current_index < len(array_slur):
                current_element = array_slur[current_index][0]
        final_array_slur[str(array_slur)] = total_slur

sorted_final_array_slur = sorted(final_array_slur.items(), key=lambda x:x[1])
for item in sorted_final_array_slur:
    print(-item[1])
for item in sorted_final_array_slur:
    print(item[0])
