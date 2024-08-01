class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        def dfs(node, parent):
            if parent:
                parents[node.val] = parent
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        dfs(root, None)

        queue = deque()
        queue.append(target)
        dist = 0
        visited = set()
        visited.add(target)

        while queue and dist != k:
            size = len(queue)
            for _ in range(size):
                removed = queue.popleft()

                if removed.left and removed.left not in visited:
                    queue.append(removed.left)
                    visited.add(removed.left)

                if removed.right and removed.right not in visited:
                    queue.append(removed.right)
                    visited.add(removed.right)

                if removed.val in parents and parents[removed.val] not in visited:
                    queue.append(parents[removed.val])
                    visited.add(parents[removed.val])

            dist += 1

        ans = []
        while queue:
            ans.append(queue.popleft().val)

        return ans

        