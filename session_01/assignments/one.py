import random


def generate_sentence_by_gram(gram_str,target,split_char_rule='=',split_char_or='|'):

    rules = dict()
    for line in gram_str.split('\n'):
        if not line:
            continue
        stmt,expr = line.split(split_char_rule)
        rules[stmt.strip()] = expr.split(split_char_or)

    sentence = generator(rules,target)

    return sentence

def generator(rules,target):

    if target in rules:
        candidates = rules[target]
        candidate = random.choice(candidates).strip()
        return ' '.join(generator(rules,c.strip()) for c in candidate.split(' ') )
    else:
        return target


human = '''
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们
寻找 = 看看 | 找找 | 想找点
活动 = 乐子 | 玩的
'''

print(generate_sentence_by_gram(human,'human'))

host = """
host = 寒暄 报数 询问 业务相关 结尾
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""

print(generate_sentence_by_gram(host,'host'))


# 我的语法
my_first_grammar = '''
'''

def generate_n():
    generated = []
    for i in range(10):
        generated.append(generate_sentence_by_gram(host,'host'))
    return generated

print(generate_n())
