

class Vocabulary:
    def __init__(self, d={}):
        #print('Hello from __init__!')
        self.d = d
        
    def __len__(self):
        return len(self.d)
    
    def __setitem__(self, word, value):
        #print('Hello from __setitem__!')
        if isinstance(value, str):
            value = (value,)
        self.d[word] = value
        
    def __getitem__(self, word):
        return self.d[word]
    
    def __delitem__(self, word):
        del self.d[word]
        
    def __str__(self):
        s = ''
        for word, value in self.d.items():
            s += f"{word} => {', '.join(value)}\n"
            #s += str(word) + ' => ' + ', '.join(value) + '\n'
        return s
    
    def count(self, word=None):
        if word != None:
            return len(self.d[word])
        else:
            all_words = set()
            for ru_words in self.d.values():
                for w in ru_words:
                    all_words.add(w)
            return all_words
    
    def contains(self, word):
        return word in self.d
    
    def is_empty(self):
        return not self.d


v = Vocabulary({
    'put': ('поставить', 'опустить'),
    'strike':  ('удар', 'забастовка', 'сильное воздействие')
})
v['hello'] = 'привет'
v['go'] = ('перемещение', 'идти', 'ходьба')
v['hi'] = 'привет'

print(v)
#print(str(v))

v.count('hello')
v.count('strike')
v.count()
v.contains('hello')
v.contains('world')
v.is_empty()
v2 = Vocabulary()
v2.is_empty()

