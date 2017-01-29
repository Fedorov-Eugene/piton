import re
#delite "" or ''

def spliter_80lvl(str):
    kek = re.split('[\n,"\s()\.\']+',str.lower())
    return [x for x in kek if x]

def word_analysis(str):
    words_set = set(spliter_80lvl(str))
    words_dict = {}
    for word in words_set:
        words_dict[word] = str.lower().count(word) 
    return words_dict


def sentence_analysis(str):
    sentences_array = [x for x in str.split('.') if x]
    count_words = []
    for sentence in sentences_array:
        words_array = spliter_80lvl(sentence)
        count_words.append(len(words_array))
    
    result = {}
    result['average'] = sum(count_words) / len(count_words)
    result['median'] = sorted(count_words)[len(count_words) // 2] 

    return result

def n_gramm(str, k = 10, n = 4):
    result = {}
    words_array = spliter_80lvl(str)
    words_array = list(filter(lambda x: len(x)>=n, words_array))
    for gramm in words_array:
        for word in words_array:
            result[gramm] = word.count(gramm)
    print(result)


def main():
    pass

if __name__ == "__main__":
    main()