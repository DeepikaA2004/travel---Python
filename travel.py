def max_people_travel_together(N, M):
    return (N * 5) + (M * 7)

# Input
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, M = map(int, input().strip().split())

    # Output
    print(max_people_travel_together(N, M))
