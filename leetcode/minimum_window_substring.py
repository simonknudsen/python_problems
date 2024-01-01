class Solution:

    def create_holder(self, s):
        return {c:-1 for c in s}

    def is_complete(self, h, t):
        return sorted(t) == sorted("".join(h["collected"]))

    def minWindow(self, s: str, t: str) -> str:
        #chars = {}
        in_progress = []
        best = None
        #for i in range(len(s)):
        #    c = s[i]
        #    if chars[c]:
        #        chars[c].append(i)
        #    else:
        #        chars[c] = [i]
        for i in range(len(s)):
            print(f"best={best} in_progress={in_progress}")
            c = s[i]
            if c in t:
                in_progress2 = in_progress.copy()
                for p in in_progress:
                    if p["chars"].count(c) > 0:
                        p["chars"].remove(c)
                    if len(p["chars"]) == 0:
                        p["end"] = i
                        if not best:
                            best = p
                        elif p["end"] - p["start"] < best["end"] - best["start"]:
                            best = p
                        in_progress2.remove(p)
                new = {"start": i, "chars": list(t)}
                new["chars"].remove(c)
                in_progress2.append(new)
                in_progress = in_progress2
        if best:
            return s[best["start"]:best["end"] + 1]
        return ""

