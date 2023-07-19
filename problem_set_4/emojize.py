import emoji


def main():
    emoji_alias = input("Input: ").strip().lower()
    print(f"Output: {alias_to_emoji(emoji_alias)}")


def alias_to_emoji(alias):
    convert = emoji.emojize(alias, language="alias")
    return convert


main()

