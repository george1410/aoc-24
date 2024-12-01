with open("./inputs/1") as file:
    lines = [line.rstrip() for line in file]

xs, ys = zip(*[map(int, line.split()) for line in lines])
xs, ys = sorted(xs), sorted(ys)

diffs = [abs(xs[i] - ys[i]) for i in range(len(xs))]

similarity_scores = [x * ys.count(x) for x in xs]

print(f"Part 1: {sum(diffs)}")
print(f"Part 2: {sum(similarity_scores)}")
