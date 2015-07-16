import StringIO
 
class Queue(object):
    def __init__(self):
        self.a = []
 
    def enqueue(self, b):
        self.a.insert(0, b)
 
    def dequeue(self):
        return self.a.pop()
 
    def isEmpty(self):
        return self.a == []
 
    def size(self):
        return len(self.a)
 
def getheight(node):
    if not node:
        return 0
    else:
        return max(getheight(node.left), getheight(node.right)) + 1
 
def add_padding(ipstr, pad_length):
    ipstr = ipstr.strip()
    padding = ' ' * (pad_length - len(ipstr))
    return ''.join([padding, ipstr])
 
def show(root):
    max_pretty_print_height = 7
    output = StringIO.StringIO()
    keys = []
    if root:
        current_level = Queue()
        next_level = Queue()
        current_level.enqueue(root)
        depth = 0
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            output.write('%s ' % current_node.key if current_node else 'NUL ') 
            next_level.enqueue(current_node.left if current_node else current_node)
            next_level.enqueue(current_node.right if current_node else current_node)
 
            if current_level.isEmpty():
                if sum([i is not None for i in next_level.a]):
                    current_level, next_level = next_level, current_level
                    depth = depth + 1
                output.write('\n')
 
    if getheight(root) > 0:
        skip_start = spaces * pad_length
        skip_mid = (2 * spaces - 1) * pad_length
 
        key_start_spacing = ' ' * skip_start
        key_mid_spacing = ' ' * skip_mid
 
        keys = output.readline().split(' ')
        padded_keys = (self.add_padding(key, pad_length) for key in keys)
 
        padded_str = key_mid_spacing.join(padded_keys)
        complete_str = ''.join([key_start_spacing, padded_str])
 
        pretty_output.write(complete_str)
        current_depth = spaces
        spaces = spaces // 2
 
        if spaces > 0:
            pretty_output.write('\n')
 
            cnt = 0
            while cnt < current_depth:
                inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                symbol_start_spacing = ' ' * (skip_start-cnt-1)
                symbol_mid_spacing = ' ' * (skip_mid-2*(cnt+1))
                pretty_output.write(''.join([symbol_start_spacing, symbol]))
                for i in keys[1:-1]:
                    pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                pretty_output.write('\n')
                cnt = cnt + 1
    return pretty_output