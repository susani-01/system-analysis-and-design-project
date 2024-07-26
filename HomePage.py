import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the main frame
        self.main_frame = tk.Frame(self)

        # Create the header label
        self.header_label = tk.Label(self.main_frame, text="E-Learning Management System", font=("Arial", 24))
        self.header_label.pack(pady=20)

        # Create the navigation bar
        self.navigation_bar = tk.Frame(self.main_frame)

        # Create the courses button
        self.courses_button = tk.Button(self.navigation_bar, text="Courses", command=self.open_courses)
        self.courses_button.pack(padx=10)

        # Create the tests button
        self.tests_button = tk.Button(self.navigation_bar, text="Tests", command=self.open_tests)
        self.tests_button.pack(padx=10)

        # Create the assignments button
        self.assignments_button = tk.Button(self.navigation_bar, text="Assignments", command=self.open_assignments)
        self.assignments_button.pack(padx=10)

        # Create the about button
        self.about_button = tk.Button(self.navigation_bar, text="About", command=self.open_about)
        self.about_button.pack(padx=10)

        # Pack the navigation bar
        self.navigation_bar.pack()

        # Create the main content area
        self.main_content_area = tk.Frame(self.main_frame)

        # Create the welcome label
        self.welcome_label = tk.Label(self.main_content_area, text="Welcome to the E-Learning Management System!")
        self.welcome_label.pack(pady=20)

        # Create the login button
        self.login_button = tk.Button(self.main_content_area, text="Log In", command=self.open_login)
        self.login_button.pack(pady=20)

        # Pack the main content area
        self.main_content_area.pack()

        # Pack the main frame
        self.main_frame.pack()

    def open_courses(self):
        # TODO: Implement this method to open the courses page
        pass

    def open_tests(self):
        # TODO: Implement this method to open the tests page
        pass

    def open_assignments(self):
        # TODO: Implement this method to open the assignments page
        pass

    def open_about(self):
        # TODO: Implement this method to open the about page
        pass

    def open_login(self):
        # TODO: Implement this method to open the login page
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("E-Learning Management System")

    home_page = HomePage(root)
    home_page.pack()

    root.mainloop()
