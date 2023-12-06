
class Record:
    red = 0
    green = 0
    blue = 0


def day2():
    print('Day 2')
    x = 0

    with open('day2_input.txt') as f:
        lines2 = f.readlines()
        x = cube_conundrum(lines2, 12, 13, 14)
    return x


def cube_conundrum(lines, red, green, blue):
    input = []
    output = []
    index = 1
    mins = []
    for line in lines:
        parts = line.split(':')
        head = parts[0]
        tail = parts[1]
        reveals = tail.split(';')
        recs = []
        for reveal in reveals:
            vals = reveal.split(',')
            record = Record()
            for val in vals:
                num,colour = val.strip().split(' ')
                print(num)
                print(colour)
                match colour:
                    case 'red':
                        record.red = int(num)
                    case 'blue':
                        record.blue = int(num)
                    case 'green':
                        record.green = int(num)
            recs.append(record)
        ok = True
        min = None
        for r in recs:
            if r.blue > blue or r.green > green or r.red > red:
                ok = False

            if min is None:
                min = Record()
                min.blue = r.blue
                min.red = r.red
                min.green = r.green
            else:
                if r.blue > min.blue:
                    min.blue = r.blue
                if r.red > min.red:
                    min.red = r.red
                if r.green > min.green:
                    min.green = r.green
        mins.append(min.red * min.green * min.blue)
        if ok:
            output.append(index)
        input.append(recs)
        index += 1
    print(output)
    return (sum(output),sum(mins))




if __name__ == '__main__':
    print(day2())
