# string - medium
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        n = len(s)
        # key ideas:
        # 1) pre-built the knowledge dict 
        # 2) process the string s w/ an auxiliary array activated if
        # a left bracket is detected
        d = dict()
        for k, v in knowledge:
            d[k] = v

        final, aux = [], []
        for i in range(n):
            if s[i] == ')':
                e = ''.join(aux)
                final.append(d[e] if e in d else '?')
                aux = []

            else:
                if aux:
                    aux.append(s[i])
                else:
                    if i > 0 and s[i - 1] == '(':
                        aux.append(s[i])
                    else:
                        if s[i] != '(':
                            final.append(s[i])

        return ''.join(final)

s, knowledge = "hi(name)", [["a","b"]]
s, knowledge = "(a)(a)(a)aaa", [["a","yes"]]
s, knowledge = "(name)is(age)yearsold", [["name","bob"],["age","two"]]

Solution().evaluate(s, knowledge)