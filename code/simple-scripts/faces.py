def main():
    msg = input("")
    final = convert(msg)
    print(final)

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()
