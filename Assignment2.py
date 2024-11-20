# Task 1

class BrowsingHistory:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    def add_page(self, page):
        """Add a new page to the stack."""
        self.stack.append(page)
        print(f"Page '{page}' added to browsing history.")

    def remove_page(self):
        """Remove the most recently visited page from the stack."""
        if self.is_empty():
            print("No pages to remove.")
            return None
        page = self.stack.pop()
        print(f"Page '{page}' removed from browsing history.")
        return page

    def count_pages(self):
        """Check how many pages have been viewed in the browsing session."""
        return len(self.stack)

    def is_empty(self):
        """Check if the current browsing session is empty."""
        return len(self.stack) == 0

    def display_history(self):
        """Display the current browsing history."""
        if self.is_empty():
            print("No browsing history.")
        else:
            print("Browsing history:")
            for page in reversed(self.stack):
                print(page)

# Example usage:
history = BrowsingHistory()
history.add_page("https://example.com")
history.add_page("https://example.com/about")
history.add_page("https://example.com/contact")

# Display history
history.display_history()

# Remove the most recent page
history.remove_page()

# Display history again
history.display_history()

# Check how many pages have been viewed
print(f"Number of pages viewed: {history.count_pages()}")

# Check if the browsing session is empty
print(f"Is browsing session empty? {history.is_empty()}")