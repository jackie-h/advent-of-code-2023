
def day1():
    print('Day 1 trebuchet')
    x = 0

    with open('day1_input.txt') as f:
        lines2 = f.readlines()
        x = calibrate(lines2)
    return x


def calibrate(lines):
    total = 0
    for line in lines:
        print(line)
        #nums = [x for x in line if x.isdigit()]

        nums = extract_nums(line)
        if len(nums) > 0:
            print(nums)
            val = nums[0] + nums[len(nums) - 1]
            total += int(val)
            print(total)
    return total


def extract_nums(line):
    index = 0
    vals = []
    for x in line:
        if x.isdigit():
            vals.append(x)
        elif line.startswith('one', index):
            vals.append('1')
        elif line.startswith('two', index):
            vals.append('2')
        elif line.startswith('three', index):
            vals.append('3')
        elif line.startswith('four', index):
            vals.append('4')
        elif line.startswith('five', index):
            vals.append('5')
        elif line.startswith('six', index):
            vals.append('6')
        elif line.startswith('seven', index):
            vals.append('7')
        elif line.startswith('eight', index):
            vals.append('8')
        elif line.startswith('nine', index):
            vals.append('9')
        index += 1
    return vals


if __name__ == '__main__':
    print(day1())
