class Privileges():
    """Object used for managing user's privileges."""

    def __init__(self, privileges=["can add post"]):
        """Grant ability to add post by default."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints out user's privileges in list form."""
        for privilege in self.privileges:
            print("This user " + privilege + "s.")
