from Tools.scripts.objgraph import ignore


class Unique():
    def __init__(self, massive: list, ignore_case: bool = False, **kwargs):
        self.massive = massive
        self.current = 0
        self.ignore_case = ignore_case
        self.kwargs = kwargs
        self.ignore()
        self.delete_repeats()
        self.end = len(self.massive)

    def ignore(self):
        if self.ignore_case:
            for i in range(len(self.massive)):
                if type(self.massive[i]) == str:
                    self.massive[i] = self.massive[i].lower()

    def delete_repeats(self):
        k = 1
        for i in range(1, len(self.massive)):
            if self.massive[i] not in self.massive[0:k]:
                self.massive[k] = self.massive[i]
                k += 1
            else:
                self.massive[i] = None
        self.massive = self.massive[0:k + 1]

    def __next__(self):
        self.current += 1
        if self.current < self.end:
            return self.massive[self.current - 1]
        raise StopIteration

    def __iter__(self):
        return self


# A = Unique(['a', 'A', 'b', 'B', 12], ignore_case=True)
# for i in A:
#     print(i)