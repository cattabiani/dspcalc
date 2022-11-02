from tabulate import tabulate

class DspObj:
    def __init__(self, name, n, t, speed_multi, components={}):
        self.name = name
        self.n = n
        self.t = t
        self.speed_multi = speed_multi
        self.components = {k: v/n for k, v in components.items()}

    def speed(self):
        return self.n * self.speed_multi/self.t

    def n_facilities(self, n):
        return n/self.speed()



    def __str__(self):
        return f"{self.name}, {self.speed()} (n/s)\n   " + "\n   ".join([f"{k}: {v}" for k, v in self.components.items()])

class DspLibrary(dict):
    def __init__(self):
        self.add(DspObj("iron ore", 1, 1, 1))
        self.add(DspObj("copper ore", 1, 1, 1))
        self.add(DspObj("iron ingot", 1, 1, 1, {"iron ore": 1}))
        self.add(DspObj("copper ingot", 1, 1, 1, {"copper ore": 1}))
        self.add(DspObj("circuit board", 2, 1, 1, {"iron ingot": 2, "copper ingot": 1 }))
        self.add(DspObj("gear", 1, 1, 0.75, {"iron ingot": 1}))
        self.add(DspObj("magnetic coil", 2, 1, 0.75, {"magnet": 2, "copper ingot": 1}))
        self.add(DspObj("magnet", 1, 1.5, 1, {"iron ore": 1}))
        self.add(DspObj("electric motor", 1, 2, 0.75, {"iron ingot": 2, "gear":1, "magnetic coil": 1}))


    def add(self, obj):
        self[obj.name] = obj

    def calc_base_components(self, name, n=1, is_str = True):

        ans = {name: n}
        for k, i in self[name].components.items():
            for b, j in self.calc_base_components(k, i*n, False).items():
                ans[b] = ans.get(b, 0)+j[0]

        ans = {k : (v, self[k].n_facilities(v)) for k, v in ans.items()}

        if not is_str:
            return ans
        return tabulate([[k, v[0], v[1]] for k, v in ans.items()], headers=["obj", "n", "n facilities"])


    def __str__(self):
        return "\n".join([str(i) for i in self.values()])