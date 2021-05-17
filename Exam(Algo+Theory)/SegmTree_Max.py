class Node:  # узел дерева(вершина)
    def __init__(self, value: int, segm: tuple):
        self.value = value
        self.segm = segm  # храним отрезок
        self.left = self.right = None  # ссылки на левого и правого потомка
        #  вершины дерева, у которых нету потомков - листья
        #  вершина, у которой нету предка - корень
        #  дерево отрезков - двоичное дерево


def get_max(x, y):
    if x > y:
        return x
    return y


# дерево строим сверху вниз(от корня к листьям)(так как алгоритм рекурсивный, то корень строится последним)
def build_tree(a: list, left: int, right: int) -> Node:
    #  работаем без слайсов, так как слайсы генерят копии массивов
    if left == right:  # эта штука для случая дерева/ поддерева из одного элемента
        node = Node(a[left], (left, left))
        return node

    x = build_tree(a, left, (right + left)//2)  # строим левую часть дерева
    y = build_tree(a, (right+left)//2 + 1, right)  # строим правую часть дерева
    node = Node(get_max(x.value, y.value), (left, right))
    node.left = x
    node.right = y
    return node


def segm_max(tree: Node, left: int, right: int):
    if left == tree.segm[0] and right == tree.segm[1]:
        return tree.value
    elif right < (tree.segm[0] + tree.segm[1])//2 + 1:
        return segm_max(tree.left, left, right)
    elif left > (tree.segm[0] + tree.segm[1])//2:
        return segm_max(tree.right, left, right)
    else:
        return get_max(segm_max(tree.left, left, tree.left.segm[1]), segm_max(tree.right, tree.right.segm[0], right))


n = int(input())
a = list(map(int, input().split()))
tree = build_tree(a, 0, n-1)

i = 1
while True:
    if n == i:
        break
    elif n > i:
        i *= 2
    else:
        a += [0 for k in range(i - n)]
        break

m = int(input())

res = []
for i in range(m):
    left, right = map(int, input().split())
    res += [segm_max(tree, left, right)]

print(*res)