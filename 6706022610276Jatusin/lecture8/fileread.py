def main():
    infile = open('flife.txt','r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
    main()