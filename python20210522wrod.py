def get_fortune():
    import random
    results = ["大吉","吉","小吉","凶","大凶","末凶"]
    return random.choice(results)
result = get_fortune()
print("今日運勢:",result)
