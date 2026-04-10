from collections import deque

def time_to_full_infection(grid: list[list[int]]) -> int:
    """
    Args:
        grid: An m×n grid where 0 = healthy and 1 = infected

    Returns:
        The number of steps until all cells are infected,
        or -1 if not all cells will become infected.
    """

    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])

    q = deque()

    num_infected = num_healthy = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                q.append((r, c))
                num_infected += 1
            else:
                num_healthy += 1

    if num_infected == m*n:
        return 0

    rounds = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if r > 0 and grid[r-1][c] == 0:
                grid[r-1][c] = 1
                num_infected += 1
                q.append((r-1 , c))
            if r < m-1 and grid[r+1][c] == 0:
                grid[r+1][c] = 1
                num_infected += 1
                q.append((r+1, c))
            if c > 0 and grid[r][c-1] == 0:
                grid[r][c-1] = 1
                num_infected += 1
                q.append((r, c-1))
            if c < n-1 and grid[r][c+1] == 0:
                grid[r][c+1] = 1
                num_infected += 1
                q.append((r, c+1))
        rounds += 1
        if num_infected == m * n:
            return rounds
        
    return -1

def time_to_full_infection_with_immunity(grid: list[list[int]]) -> int:
    """
    Args:
        grid: An m×n grid where 0 = healthy and 1 = infected, and 2 = immune

    Returns:
        The number of steps until all cells are infected,
        or -1 if not all cells will become infected.
    """

    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])

    q = deque()

    num_infected = num_healthy = num_immune = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                q.append((r, c))
                num_infected += 1
            elif grid[r][c] == 0:
                num_healthy += 1
            else:
                num_immune += 1

    assert num_infected + num_healthy + num_immune == m * n

    rounds = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if r > 0 and grid[r-1][c] == 0:
                grid[r-1][c] = 1
                num_infected += 1
                q.append((r-1 , c))
            if r < m-1 and grid[r+1][c] == 0:
                grid[r+1][c] = 1
                num_infected += 1
                q.append((r+1, c))
            if c > 0 and grid[r][c-1] == 0:
                grid[r][c-1] = 1
                num_infected += 1
                q.append((r, c-1))
            if c < n-1 and grid[r][c+1] == 0:
                grid[r][c+1] = 1
                num_infected += 1
                q.append((r, c+1))
        rounds += 1
        if num_infected + num_immune == m * n:
            return rounds
        
    return -1

def level_1():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result = time_to_full_infection(grid)
    print(result)

    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    result = time_to_full_infection(grid)
    print(result)

    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = time_to_full_infection(grid)
    print(result)

    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = time_to_full_infection(grid)
    print(result)

    grid = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = time_to_full_infection(grid)
    print(result)

def level_2():
    grid = [
        [0, 2, 0],
        [2, 1, 2],
        [0, 2, 0]
    ]
    result = time_to_full_infection_with_immunity(grid)
    print(result)
    assert result == -1

    grid = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 1]
    ]
    result = time_to_full_infection_with_immunity(grid)
    print(result)
    assert result == 2

    grid = [
        [1, 2, 0],
        [0, 2, 0],
        [0, 0, 0]
    ]
    result = time_to_full_infection_with_immunity(grid)
    print(result)
    assert result == 6

    grid = [
        [0, 1, 0],
        [0, 2, 0],
        [0, 2, 0]
    ]
    result = time_to_full_infection_with_immunity(grid)
    print(result)
    assert result == 3

def more_tests():
    # Test 1: Basic center infection
    assert time_to_full_infection([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

    # Test 2: Corner infections
    assert time_to_full_infection([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 2

    # Test 3: No infection source
    assert time_to_full_infection([[0, 0], [0, 0]]) == -1

    # Test 4: Already fully infected
    assert time_to_full_infection([[1, 1], [1, 1]]) == 0

    # Test 5: Single cell
    assert time_to_full_infection([[1]]) == 0
    assert time_to_full_infection([[0]]) == -1

    # Test 6: Linear spread (a line)
    assert time_to_full_infection([[1, 0, 0, 0, 0]]) == 4

    # Test 7: Larger grid
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert time_to_full_infection(grid) == 4

if __name__ == "__main__":
    # print("==== LEVEL 1 ====")
    # level_1()
    # print("==== LEVEL 2 ====")
    # level_2()

    more_tests()