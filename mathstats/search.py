import re
#delite "" or ''

def isemail(txt):
    return re.compile(r"^.+?\@\w+?\.\w{2,3}$", re.I | re.S).match(txt)

def isfloat(txt):
    return re.compile(r"^\d+?(?:\.|\,)\d+?$", re.S).match(txt)

def url_inspect(txt):
    return re.match(re.compile(r"^(?P<schema>https?)://(?P<host>.+?)/(?P<path>[^?]+?)?(?:\?|$)(?P<params>.+?)?$", re.I | re.S), txt).groupdict()


def spliter(str):
    kek = re.split('[\n,"\s()\.\']+',str.lower())
    return [x for x in kek if x]

def word_analysis(str):
    words_set = set(spliter(str))
    words_dict = {}
    for word in words_set:
        words_dict[word] = str.lower().count(word) 
    return words_dict


def sentence_analysis(str):
    sentences_array = [x for x in str.split('.') if x]
    count_words = []
    for sentence in sentences_array:
        words_array = spliter(sentence)
        count_words.append(len(words_array))
    
    result = {}
    result['average'] = sum(count_words) / len(count_words)
    result['median'] = sorted(count_words)[len(count_words) // 2] 

    return result

def n_gramm(str, k = 10, n = 4):
    result = {}
    words_array = spliter(str)
    words_array = list(filter(lambda x: len(x)>=n, words_array))
    for gramm in words_array:
        for word in words_array:
            result[gramm] = word.count(gramm)
    print(result)


def main(str):
    for i,j in word_analysis(str).items():
        print('{}--{}'.format(i,j))
    print('='*100)
    math = sentence_analysis(str)
    print('average - {}\nmedian - {}'.format(math['average'],math['median']))  

if __name__ == "__main__":
    main()