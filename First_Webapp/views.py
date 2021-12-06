from django.shortcuts import render

from First_Webapp import counter


def home(request):
    return render(request, 'index.html', {'Key': 'i am from python'})


def result(request):
    age = request.GET['user_age']
    name = request.GET['user_name']
    msg = f' hello {name} your age is {age}'
    article = request.GET['article']
    var_dict, words_count = counter.count(article)
    # words = article.split()  # to split the text for counting
    # words_count = len(words)
    # dict_words = {}
    #
    # for word in words:
    #     if word in dict_words:
    #         dict_words[word] += 1
    #     else:
    #         dict_words[word] = 1
    #
    # var_dict = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'result.html',
                  {'Key1': age, 'Key2': name, 'Key3': msg, 'Key4': article, 'Key5': words_count,
                   'Key6': var_dict})
