class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], op: str, right: List[int]) -> List[int]:
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r)))
            return res

        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                ans.extend(compute(self.diffWaysToCompute(expression[:i]), expression[i], self.diffWaysToCompute(expression[i+1:])))
        return ans
