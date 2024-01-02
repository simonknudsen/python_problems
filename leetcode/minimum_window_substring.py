class Solution:

    def create_holder(self, s):
        return {c:-1 for c in s}

    def is_complete(self, h, t):
        return sorted(t) == sorted("".join(h["collected"]))

    def minWindow(self, s: str, t: str) -> str:
        in_progress = []
        best = None
        all_chars = list(set(t))
        baseline = dict(zip(all_chars,[0] * len(all_chars)))
        for c in t:
            baseline[c] += 1
        print(baseline)
        for i in range(len(s)):
            #print(f"best={best} in_progress={in_progress}")
            c = s[i]
            if baseline.get(c):
                new = {"start": i, "chars": baseline.copy()}
                in_progress.append(new)
                in_progress2 = in_progress.copy()

                for p in in_progress:
                    if p["chars"].get(c):
                        if p["chars"][c] == 1:
                            p["chars"].pop(c)
                        elif p["chars"][c] > 0:
                            p["chars"][c] -= 1
                    if len(p["chars"]) == 0:
                        p["end"] = i
                        if not best:
                            best = p
                        elif p["end"] - p["start"] < best["end"] - best["start"]:
                            best = p
                        in_progress2.remove(p)
                    # remove too long
                    if best and p["start"] < best["start"]:
                        in_progress2.remove(p)
                    # remove not enough chars left
                    #if sum(p["chars"].values()) > len(s) - i:
                    #    in_progress2.remove(p)
                in_progress = in_progress2
        #print(f"best={best} in_progress={in_progress}")
        print(f"best={best}")
        if best:
            return s[best["start"]:best["end"] + 1]
        return ""

