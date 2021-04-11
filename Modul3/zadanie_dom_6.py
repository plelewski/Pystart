def filter_words(ll:list) -> list:
    return [x for x in ll if 4 < len(x) < 8]

print(filter_words(['osa', 'programowanie', 'palec', 'fotka']))
