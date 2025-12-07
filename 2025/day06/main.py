def result(filename) -> int:
    with open(filename) as file:
        rows = file.read().strip("\n").splitlines()
    
    width = max(len(r) for r in rows)
    rows = [r.ljust(width) for r in rows]
    
    # Build list of columns
    cols = []
    for c in range(width):
        col = "".join(rows[r][c] for r in range(len(rows)))
        cols.append(col)
    
 
    problems = []
    block = []
    for col in cols:
        if col.strip() == "":
            if block:
                problems.append(block)
                block = []
        else:
            block.append(col)
    if block:
        problems.append(block)
    
    # PART 1
    part1 = 0
    for block in problems:
        block_rows = ["".join(col[i] for col in block) for i in range(len(rows))]
        nums = [int(r.strip()) for r in block_rows[:-1] if r.strip()]
        op   = block_rows[-1].strip()
        if op == "+":
            part1 += sum(nums)
        else:
            prod = 1
            for n in nums:
                prod *= n
            part1 += prod
    
    # PART 2 
    part2 = 0
    for block in problems:
        nums = []
        for col in reversed(block):
            digits = col[:-1].strip()  
            if digits:
                nums.append(int("".join(digits)))
        op = block[0][-1].strip() 
        if op == "+":
            part2 += sum(nums)
        else:
            prod = 1
            for n in nums:
                prod *= n
            part2 += prod
    
    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
