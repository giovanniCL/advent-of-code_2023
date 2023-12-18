
# with open("input.txt", "r") as input_file:
#     input_text = input_file.read()

# tokens = [token.strip() for token in input_text.split(",")]

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

class Box:
    def __init__(self, power_multiplier):
        self.labels = []
        self.label_focal_length_map = {}
        self.power_multiplier = power_multiplier

    def __repr__(self):
        return str(self.labels)
    
    def __contains__(self, lens):
        return lens.label in self.labels
    
    def find_lens(self, lens):
        return self.labels.index(lens.label)
    
    def remove_lens(self, lens):
        if lens not in self: return
        lens_i = self.find_lens(lens)
        self.labels[lens_i] = None
        self.labels = [l for l in self.labels if l]
        self.label_focal_length_map.pop(lens.label)

    def add_lens(self, lens):
        if lens not in self:
            self.labels.append(lens.label)
        self.label_focal_length_map[lens.label] = lens.focal_length

    def get_focal_power(self):
        return sum([self.power_multiplier * (i + 1) * int(self.label_focal_length_map[label]) for i, label in enumerate(self.labels)])


def hash(str):
    current = 0
    for c in str:
        current += ord(c)
        current *= 17
        current %= 256
    return current

def split_and_get_op(token):
    if "=" in token: op = "="
    else: op = "-"
    return token.split(op), op

def part_1(tokens):
    return sum(map(hash, tokens))

def part_2(tokens, boxes):
    for token in tokens:
        instruction = split_and_get_op(token)
        lens = Lens(instruction[0][0], instruction[0][1])
        box_num = hash(lens.label)
        box = boxes[box_num]
        if instruction[1] == "=":
            box.add_lens(lens)
        else: box.remove_lens(lens)
    total = 0
    for box in boxes:
        total += box.get_focal_power() 
    return total

def main():
    with open("input.txt", "r") as input_file:
        input_text = input_file.read()
    tokens = [token.strip() for token in input_text.split(",")]
    boxes = [Box(i + 1) for i in range(256)]
    result_part_1 = part_1(tokens)
    result_part_2 = part_2(tokens, boxes)
    print(f"Sum of hashes of instructions: {result_part_1}")
    print(f"Total focusing power of lenses: {result_part_2}")

if __name__ == "__main__":
    main()


