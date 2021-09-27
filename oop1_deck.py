import collections
from random import choice  # 从一个序列中随机选取一个

# 用于构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])
diamonds_1_card = Card('1', 'diamonds')
print(diamonds_1_card)

# sorted(diy_list, key=diy_rank_func) 用于排序自定义list


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
        # 实现该方法后，可以用[]检索元素，eg.使用deck[::]；
        # 也可以使用for item in list:迭代

    @staticmethod  # 不涉及对属性操作的函数，声明为静态函数
    def spades_high(_card):
        rank_value = FrenchDeck.ranks.index(_card.rank)
        return rank_value * len(suit_values) + suit_values[_card.suit]


deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

print(choice(deck))

print(Card('Q', 'hearts') in deck)

# 排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


for card in sorted(deck, key=deck.spades_high):
    print(card)
