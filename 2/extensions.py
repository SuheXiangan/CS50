def main():
    words = input('File name:').strip().lower()
    
    if words.endswith('.jpg') or words.endswith('.jepg'):
        print('image/jpeg')
    elif words.endswith('.gif'):
        print('image/gif')
    elif words.endswith(".png"):
        print('image/png')
    elif words.endswith('.pdf'):
        print('application/pdf')
    elif words.endswith('.txt'):
        print('text/plain')
    elif words.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')

main()