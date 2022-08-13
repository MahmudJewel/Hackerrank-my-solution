def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        substr=string[i:i+k]
        # print(substr, i, i+k)
        substr=set(substr)
        # st=''
        # for i in substr:
        #     st=st+i
        # print(st)
        substr=''.join(substr)
        print(substr)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)