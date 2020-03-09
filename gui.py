import tkinter as tk
from tkinter import messagebox


class Controller:
    """Creates a controller for the given Binary Search Tree"""

    def __init__(self, tree):
        self.tree = tree

        self.root = tk.Tk()
        self.root.title('Binary Tree Visualizer')
        self.root.resizable(0, 0)

        width = int(self.root.winfo_screenwidth() * 0.7)
        height = int(self.root.winfo_screenheight() * 0.9)

        self.root.geometry(f'{width}x{height}+200+0')

        self.canvas = tk.Canvas(self.root, width=int(width * 0.75), height=height, bg='#ffffff', bd=5, relief='ridge')
        self.canvas.pack(side=tk.RIGHT)

        self.frame = tk.Frame(self.root, width=int(width * 0.25), height=height, bg='#b0e0e6', bd=5, relief='ridge')
        self.frame.pack(side=tk.LEFT)

        self.canvas_point = (int(width * 0.75) // 2, height // 2)

        self.var = tk.StringVar()

        tk.Label(self.frame, text='Enter Node\n(Integer key value)', font=('Comic sans MS', 15, 'bold'), fg='#0000ff',
                 bg='#b0e0e6').place(relx=0.09, rely=0.02)
        self.entry = tk.Entry(self.frame, textvar=self.var, font=('Comic sans MS', 12), justify='center')
        self.entry.place(relx=0.08, rely=0.12)

        insert = tk.Button(self.frame, text=' ' * 10 + 'Insert' + ' ' * 10, command=self._insert,
                           font=('Comic sans MS', 13, 'bold'), fg='#ffffff', bg='#0000ff')
        delete = tk.Button(self.frame, text=' ' * 10 + 'Delete' + ' ' * 10, command=self._delete,
                           font=('Comic sans MS', 13, 'bold'), fg='#ffffff', bg='#0000ff')
        search = tk.Button(self.frame, text=' ' * 10 + 'Search' + ' ' * 10, command=self._search,
                           font=('Comic sans MS', 13, 'bold'), fg='#ffffff', bg='#0000ff')

        insert.place(relx=0.075, rely=0.2)
        delete.place(relx=0.070, rely=0.265)
        search.place(relx=0.065, rely=0.33)

        self.heading = tk.Label(self.frame, text='', font=('Comic sans MS', 15, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.key = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.level = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.parent = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.n_children = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.left_child = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.right_child = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.predecessor = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')
        self.successor = tk.Label(self.frame, text='', font=('Comic sans MS', 13, 'bold'), fg='#0000ff', bg='#b0e0e6')

        self.heading.place(relx=0.07, rely=0.5)
        self.key.place(relx=0.07, rely=0.58)
        self.level.place(relx=0.07, rely=0.62)
        self.parent.place(relx=0.07, rely=0.66)
        self.n_children.place(relx=0.07, rely=0.7)
        self.left_child.place(relx=0.07, rely=0.74)
        self.right_child.place(relx=0.07, rely=0.78)
        self.predecessor.place(relx=0.07, rely=0.82)
        self.successor.place(relx=0.07, rely=0.86)

        self.entry.focus()
        self.root.mainloop()

    def _insert(self):
        key = self._checkKey()
        if key is None: return
        if self.tree.insert(key) is False:
            messagebox.showerror('Duplicate node detected', 'Duplicate nodes are not allowed in a Binary Search Tree')
        else: self._draw(key=key)
        self.var.set('')
        self.entry.focus()

    def _delete(self):
        key = self._checkKey()
        if key is None: return
        if self.tree.delete(key) is False:
            messagebox.showerror('Node not found', 'The request node is not present in the Binary Search Tree')
        else: self._draw(key=key, delete=True)
        self.var.set('')
        self.entry.focus()

    def _search(self):
        key = self._checkKey()
        if key is None: return

        node = self.tree.search(key)
        if node is None:
            messagebox.showerror('Node not found', 'The request node is not present in the Binary Search Tree')
        else: self._draw(node=node)
        self.var.set('')
        self.entry.focus()

    def _checkKey(self):
        try:
            return int(self.var.get())
        except:
            messagebox.showerror('Unsupported format', 'The key value of a node should be an integer value')
            self.var.set('')
            return None

    def _circle(self, p, radius, color='#ffffff'):
        self.canvas.create_oval(p[0] - radius, p[1] - radius, p[0] + radius, p[1] + radius, fill=color)

    def _drawNodes(self, node, p1, p2, dx, key):
        if node is None: return

        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])
        p1 = p2
        dx = dx // 2

        self._drawNodes(node.left, (p1[0], p1[1]), (p2[0] - dx, p2[1] + 60), dx, key)
        self._drawNodes(node.right, (p1[0], p1[1]), (p2[0] + dx, p2[1] + 60), dx, key)

        if node.key == key:
            self._circle(p2, 20, '#00ff00')
        else:
            self._circle(p2, 20)

        self.canvas.create_text(p2[0], p2[1], font=('Comic Sans MS', 10, 'bold'), text=node.key)

    def _draw(self, key=None, node=None, delete=False):
        if node is None: node = self.tree.search(key)
        if not delete: self._showProperties(node)

        self.canvas.delete('all')
        h = self.tree.height()
        x, y = self.canvas_point
        self._drawNodes(self.tree.root, (x, y - (30 * h)), (x, y - (30 * h)), 65 * h, node.key if node else None)

    def _showProperties(self, node):
        parent = node.parent.key if node.parent else '-'
        children = node.left, node.right
        l = node.left.key if node.left else '-'
        r = node.right.key if node.right else '-'

        predecessor = self.tree.predecessor(node.key)
        successor = self.tree.successor(node.key)
        predecessor = predecessor if predecessor else '-'
        successor = successor if successor else '-'

        self.heading['text'] = 'Node Properties\n-----------------'
        self.key['text'] = f'Key : {node.key}'
        self.level['text'] = f'Level : {self.tree.level(node.key)}'
        self.parent['text'] = f'Parent : {parent}'
        self.n_children['text'] = f'Number of children : {2 - children.count(None)}'
        self.left_child['text'] = f'Left Child : {l}'
        self.right_child['text'] = f'Right Child : {r}'
        self.predecessor['text'] = f'Inorder Predecessor : {predecessor}'
        self.successor['text'] = f'Inorder Successor : {successor}'

