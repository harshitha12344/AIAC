def slugify(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove characters except alnum, spaces, hyphen
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789 -"
    text = "".join(c for c in text if c in allowed)
    # Replace spaces with hyphen
    result = []
    prev = ""
    for c in text:
        if c == " ":
            c = "-"
        if c == "-" and prev == "-":
            continue
        result.append(c)
        prev = c
    text = "".join(result)
    # Collapse multiple hyphens already handled above
    # Trim leading and trailing hyphens
    text = text.strip("-")
    return text

def test_slugify(input_text, expected_slug):
    assert slugify(input_text) == expected_slug

if __name__ == "__main__":
    user_input = input("Enter text to slugify: ")
    print(slugify(user_input))
    # Modified slugify to return uppercase output
    def slugify_upper(text: str) -> str:
        return slugify(text).upper()

    # Example usage
    user_input = input("Enter text to slugify (uppercase output): ")
    print(slugify_upper(user_input))
    # Run some test cases
    test_slugify("Hello World!", "hello-world")
    test_slugify("Python--Rocks!!", "python-rocks")
    test_slugify("  Multiple   Spaces  ", "multiple-spaces")
    test_slugify("Already-a-slug", "already-a-slug")
    print("All tests passed.")
    # Example: process a list of strings and print their slugs
    sample_list = ['Hello World!', 'AI & You', 'Set13-C2']
    slugs = [slugify(s) for s in sample_list]
    print(slugs)
    # Convert sample_list items to uppercase slugs and print
    upper_slugs = [slugify_upper(s) for s in sample_list]
    print(upper_slugs)