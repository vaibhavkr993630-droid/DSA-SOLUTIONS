class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def mask(c):
            return 1 << (ord(c) - ord('a'))

        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = p

                for k in range(1, LOG):
                    parent[k][u] = parent[k - 1][parent[k - 1][u]]

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        bit = [0] * (n + 1)

        def update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        initial = [0] * n
        stack = [(0, 0, 0)]

        while stack:
            u, p, curr = stack.pop()
            curr ^= mask(s[u])
            initial[u] = curr

            for v in adj[u]:
                if v != p:
                    stack.append((v, u, curr))

        s = list(s)
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = mask(s[u]) ^ mask(c)
                s[u] = c

                update(tin[u], delta)
                if tout[u] + 1 < n:
                    update(tout[u] + 1, delta)

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                pu = initial[u] ^ prefix(tin[u])
                pv = initial[v] ^ prefix(tin[v])

                path_mask = pu ^ pv ^ mask(s[w])
                ans.append((path_mask & (path_mask -1)) == 0)

        return ans