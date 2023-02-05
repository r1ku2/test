def output_txt(result):
    with open('last_log.txt', 'w',encoding='utf_8') as f:
        print(result, file=f)

# main
if __name__ == '__main__':
    output_txt("hoge")
