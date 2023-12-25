"""def door_mat_design(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    design = '\n'.join(pattern + [welcome] + pattern[::-1])
    print(design)

if __name__ == "__main__":
    N, M = map(int, input().split())
    door_mat_design(N, M)"""


"""def door_mat(N,M):
    pattern = [('.|.'*(2*i+1)).center(M,'-') for i in range(N//2)]
    welcome = 'WELCOME TO PYTHON'.center(M,'-')
    design = '\n'.join(pattern+[welcome]+pattern[::-1])
    print(design)
    


if __name__ == "__main__":
    N,M = map(int,input().split())
    door_mat(N,M)"""



def door_math(N,M):
    pattern = [('.|.'*(2*i*1)).center(M,'-') for i in range(N//2)]
    welcome = 'WELCOME'.center(M,'-')
    design = '\n'.join(pattern+[welcome]+pattern[::-1])
    print(design)

if __name__ == "__main__":
    N,M = map(int,input().split())
    door_math(N,M)






















