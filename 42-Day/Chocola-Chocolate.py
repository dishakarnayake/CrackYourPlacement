def min_cost_to_break_chocolate(m, n, x_costs, y_costs):
    x_costs.sort(reverse=True)
    y_costs.sort(reverse=True)

    total_cost = 0
    h_segments = 1  # initially we have 1 horizontal segment
    v_segments = 1  # initially we have 1 vertical segment

    i = 0  # pointer for x_costs
    j = 0  # pointer for y_costs

    while i < len(x_costs) and j < len(y_costs):
        if x_costs[i] >= y_costs[j]:
            total_cost += x_costs[i] * v_segments
            h_segments += 1
            i += 1
        else:
            total_cost += y_costs[j] * h_segments
            v_segments += 1
            j += 1

    # Add remaining x_costs if any
    while i < len(x_costs):
        total_cost += x_costs[i] * v_segments
        i += 1

    # Add remaining y_costs if any
    while j < len(y_costs):
        total_cost += y_costs[j] * h_segments
        j += 1

    return total_cost

def main():
    t = int(input().strip())  # number of test cases
    for _ in range(t):
        input()  # consume blank line
        m, n = map(int, input().strip().split())
        x_costs = [int(input().strip()) for _ in range(m - 1)]
        y_costs = [int(input().strip()) for _ in range(n - 1)]
        
        result = min_cost_to_break_chocolate(m, n, x_costs, y_costs)
        print(result)

if __name__ == "__main__":
    main()