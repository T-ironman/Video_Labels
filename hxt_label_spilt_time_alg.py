def hxt_label_spilt_time_alg(label_lists,value):
    labels = {}
    sum = 0
    ret_labels = []
    for label_list in label_lists:
        if label_list in labels:
            labels[label_list] = labels[label_list] + 1
        else:
            labels[label_list] = 1
    #print(labels)
    '''
    sum：出现频率总和
    '''
    for label in labels:
        sum = sum + labels[label]
    #print(sum)

    for label in labels:
        labels[label] = labels[label]/sum
    #print(labels)

    for label in labels:
        if (labels[label] < value) is not True:
            ret_labels.append(label)
        else:
            continue
    return ret_labels



if __name__ == "__main__":
    label_lists = ['a','b','a','b','c','a']
    hxt_label_spilt_time_alg(label_lists,0.5)
