def generate_kmers_rec(length):
    if length == 1:
        return ['A', 'T', 'G', 'C']
    else:
        result = []
        for seq in generate_kmers_rec(length - 1):
            for base in ['A', 'T', 'G', 'C']:
                result.append(seq + base)
        print result

#generate_kmers_rec(1)
generate_kmers_rec(2)
