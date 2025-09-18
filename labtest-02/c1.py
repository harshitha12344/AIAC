def dedupe_emails(emails):
    """
    Returns the first occurrence of each email (case-insensitive), preserving original order.
    """
    seen = set()
    result = []
    for email in emails:
        key = email.lower()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result

# Unit tests
def test_dedupe_emails():
    assert dedupe_emails(['A@x.com', 'a@x.com', 'B@y.com']) == ['A@x.com', 'B@y.com']
    assert dedupe_emails(['a@x.com', 'A@x.com', 'b@y.com', 'B@y.com']) == ['a@x.com', 'b@y.com']
    assert dedupe_emails([]) == []
    assert dedupe_emails(['A@x.com']) == ['A@x.com']
    assert dedupe_emails(['A@x.com', 'B@y.com', 'C@z.com']) == ['A@x.com', 'B@y.com', 'C@z.com']

if __name__ == "__main__":
    test_dedupe_emails()
    print("All tests passed.")

    # Example input
    emails = ['Alice@Example.com', 'alice@example.com', 'Bob@Mail.com', 'BOB@mail.com', 'Charlie@site.org']
    print("Input emails:", emails)
    print("Deduped emails:", dedupe_emails(emails))
    # Prompt the user for a comma-separated list of emails and print the deduped result
    user_input = input("Enter emails separated by commas: ")
    user_emails = [e.strip() for e in user_input.split(",") if e.strip()]
    print("Deduped emails from input:", dedupe_emails(user_emails))
