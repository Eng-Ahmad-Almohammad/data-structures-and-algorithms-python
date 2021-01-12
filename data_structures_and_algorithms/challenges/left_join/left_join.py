def left_join(h1,h2):
    '''
    I am assuming h1 and h2 are dictionaries
    '''
    if len(h1) > 0:
        output = []

        for key in h1:
            value1 = h1[key]
            if key in h2:
                value2 = h2[key]

            else:
                value2 = None
            output.append([key,value1,value2])
        return output
    else:
        return 'Your left hashmap is empty'

if __name__=='__main__':
    h1 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outift': 'garb',
        'guide': 'usher',
    }

    h2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }
    print(left_join(h1,h2))