def get_data(filename):
    with open(filename) as file:
        sections = file.read().split('\n\n')
    page_rules = sections[0].splitlines()
    page_numb = [line.split(',') for line in sections[1].splitlines()]
    return page_rules, page_numb

def rule_map(page_rules):
    rule = {}
    for n in page_rules:
        before, after = map(int, n.split('|'))
        if before not in rule:
            rule[before] = set()
        rule[before].add(after)
    return rule

def is_update_in_order(update, rule_map):
    for i, curr in enumerate(update):
        for next in update[i+1:]:
            if curr in rule_map and next in rule_map[curr]:
                continue
            return False
    return True

def correct_update(update, rule_map):
    sorted_update= []
    update_set = set(update)
    dependency_cnt = {page:0 for page in update_set}

    for curr, next in rule_map.items():
        if curr in update_set:
            for n in next:
                if n in update_set:
                    dependency_cnt[n] += 1

    #pages with no dependencies
    queue = [page for page in update if dependency_cnt[page] == 0]

    while queue:
        page = queue.pop(0)
        sorted_update.append(page)
        for n in rule_map.get(page, []):
            if n in update_set:
                dependency_cnt[n] -= 1
                if dependency_cnt[n] == 0:
                    queue.append(n)

    return sorted_update

def sum_middle_numbers(lists):
    mid_numbs = []
    for list in lists:
        n = len(list)
        mid_numbs.append(list[n//2])
    return sum(mid_numbs)


def result(filename) -> int:
    page_rules, page_numb = get_data(filename)
    page_ordering_rules = rule_map(page_rules)
    valid_updates, invalid_update = [], []
    mid_numbs1, mid_numbs2 = [], []

    for i, update in enumerate(page_numb, start=1):
        update = list(map(int, update))
        n1 = len(update)
        if is_update_in_order(update, page_ordering_rules):
            valid_updates.append(update)
        else:
            
            corrected = correct_update(update, page_ordering_rules)
            invalid_update.append(corrected)
           
    part1 = sum_middle_numbers(valid_updates)
    part2 = sum_middle_numbers(invalid_update)

    return part1, part2
if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    # print('Answer:', result('input.txt'))