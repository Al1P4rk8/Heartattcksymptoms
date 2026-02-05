import tkinter as tk
from tiny_checker import DESCRIPTIONS, load_symptoms

# Color palette
BG_COLOR = "#F5F5F5"
TEXT_COLOR = "#2C3E50"
EMERGENCY_COLOR = "#E74C3C"
BUTTON_COLOR = "#3498DB"

class HeartCheckerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Heart Symptom Checker")
        self.window.geometry("700x550")
        self.window.configure(bg=BG_COLOR)
        
        # Initialize variables
        self.current_question = 0
        self.user_symptoms = []
        self.total_score = 0
        self.symptoms = load_symptoms()
        
        # Show first screen
        self.show_welcome_screen()
    
    def clear_window(self):
        """Remove all widgets from window"""
        for widget in self.window.winfo_children():
            widget.destroy()
    
    def show_welcome_screen(self):
        # Red header
        header = tk.Frame(self.window, bg=EMERGENCY_COLOR, height=120)
        header.pack(fill="x")
        
        title = tk.Label(
            header,
            text="Heart Symptom Checker",
            font=("Freight", 28, "bold"),
            bg=EMERGENCY_COLOR,
            fg="white"
        )
        title.pack(pady=35)
        
        # Main content
        content = tk.Frame(self.window, bg=BG_COLOR)
        content.pack(fill="both", expand=True, padx=50, pady=40)
        
        # Warning box
        warning = tk.Label(
            content,
            text="IMPORTANT NOTICE",
            font=("Freight", 14, "bold"),
            bg=BG_COLOR,
            fg=EMERGENCY_COLOR
        )
        warning.pack(pady=(0, 10))
        
        disclaimer = tk.Label(
            content,
            text="This tool cannot replace medical judgment or diagnose heart attacks.\nIt cannot and should not replace immediate medical attention.",
            font=("Atkinson Hyperlegible", 12),
            bg=BG_COLOR,
            fg="#666666",
            wraplength=550,
            justify="center"
        )
        disclaimer.pack(pady=20)
        
        # Continue button
        button = tk.Button(
            content,
            text="Continue →",
            command=self.show_question_screen,
            font=("Freight", 15, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            activebackground="#2980B9",
            relief="flat",
            padx=50,
            pady=15,
            cursor="hand2"
        )
        button.pack(pady=30)
        
        # Small footer text
        footer = tk.Label(
            content,
            text="Press Continue when ready to begin",
            font=("Atkinson Hyperlegible", 10),
            bg=BG_COLOR,
            fg="#999999"
        )
        footer.pack()
    
    def show_question_screen(self):
        """Display current symptom question"""
        self.clear_window()
        
        # Get current symptom
        symptom = self.symptoms[self.current_question]
        
        # Show the question
        question = tk.Label(
            self.window,
            text=f"Do you have {symptom['name']}?",
            font=("Freight", 20),
            bg=BG_COLOR
        )
        question.pack(pady=50)
        
        # YES button
        yes_btn = tk.Button(
            self.window,
            text="YES",
            command=self.on_yes_clicked,
            font=("Freight", 14, "bold"),
            bg="#27AE60", 
            fg="white",
            width=20,
            pady=10
        )
        yes_btn.pack(pady=10)
        
        # NO button
        no_btn = tk.Button(
            self.window,
            text="NO",
            command=self.on_no_clicked,
            font=("Freight", 14, "bold"),
            bg="#95A5A6",  
            fg="white",
            width=20,
            pady=10
        )
        no_btn.pack(pady=10)
        
        # NOT SURE button
        notSure_btn = tk.Button(
            self.window,
            text="NOT SURE",
            command=self.on_not_sure_clicked,
            font=("Freight", 14, "bold"),
            bg=BUTTON_COLOR,  
            fg="white",
            width=20,
            pady=10
        )
        notSure_btn.pack(pady=10)
    
    def on_yes_clicked(self):
        """User clicked YES button"""
        symptom = self.symptoms[self.current_question]
        self.user_symptoms.append(symptom)
        self.total_score += symptom["weight"]
        self.current_question += 1
        
        # Check if done
        if self.current_question >= len(self.symptoms):
            self.show_result_screen()
        else:
            self.show_question_screen()
    
    def on_no_clicked(self):
        """User clicked NO button"""
        self.current_question += 1
        
        # Check if done
        if self.current_question >= len(self.symptoms):
            self.show_result_screen()
        else:
            self.show_question_screen()
    def on_not_sure_clicked(self):
        """User clicked NOT SURE button"""
        # Check if past the last question
        if self.current_question >= len(self.symptoms):
            print("All questions done!")
            return  # Exit the function
        
        self.clear_window()
        
        # Getting symptom info
        symptom = self.symptoms[self.current_question]
        description = DESCRIPTIONS[symptom["name"]]
        
        # Show description in window
        desc_label = tk.Label(
            self.window,
            text=description,
            font=("Atkinson Hyperlegible", 12),
            bg=BG_COLOR,
            fg="#333333",
            wraplength=600,
            justify="left"
        )
        desc_label.pack(pady=30)
        
        # Button to go back
        button = tk.Button(
            self.window,
            text="Got it, ask me again",
            command=self.show_question_screen,
            font=("Freight", 14, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            pady=10,
            padx=30
        )
        button.pack(pady=20)
    
   

    def show_result_screen(self):
        """Show final results"""
        self.clear_window()
        
        # Import and calculate risk
        from tiny_checker import calculate_risk
        risk_level = calculate_risk(self.user_symptoms, self.total_score)
        
        # Determine header color based on risk
        if risk_level == "Emergency":
            header_color = EMERGENCY_COLOR
        elif risk_level == "A&E":
            header_color = "#E67E22"  # Orange
        elif risk_level == "GP":
            header_color = "#F39C12"  # Yellow
        else:  # Monitor
            header_color = "#27AE60"  # Green
        
        # Colored header
        header = tk.Frame(self.window, bg=header_color, height=120)
        header.pack(fill="x")
        
        # Title
        title = tk.Label(
            header,
            text="RESULTS",
            font=("Freight", 28, "bold"),
            bg=header_color,
            fg="white"
        )
        title.pack(pady=35)
        
        # Main content
        content = tk.Frame(self.window, bg=BG_COLOR)
        content.pack(fill="both", expand=True, padx=50, pady=40)
        
        # Risk level
        risk_label = tk.Label(
            content,
            text=f"Risk Level: {risk_level}",
            font=("Freight", 20, "bold"),
            bg=BG_COLOR,
            fg=header_color
        )
        risk_label.pack(pady=20)
        
        # Get appropriate message
        if risk_level == "Emergency":
            message = "Your symptoms could be serious.\nIt's safest to call emergency services right now."
        elif risk_level == "A&E":
            message = "These symptoms may need prompt medical attention.\nPlease go to A&E or urgent care as soon as possible."
        elif risk_level == "GP":
            message = "Your symptoms don't strongly suggest an emergency,\nbut it's important to speak with a GP soon."
        else:  # Monitor
            message = "Your answers don't indicate typical heart-related warning signs.\nIf symptoms change or worsen, seek medical care."
        
        # Message label
        message_label = tk.Label(
            content,
            text=message,
            font=("Atkinson Hyperlegible", 13),
            bg=BG_COLOR,
            fg="#333333",
            wraplength=500,
            justify="center"
        )
        message_label.pack(pady=30)
        
        # Start Over button
        button = tk.Button(
            content,
            text="Start Over",
            command=self.restart,
            font=("Freight", 14, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            relief="flat",
            padx=40,
            pady=12,
            cursor="hand2"
        )
        button.pack(pady=20)
    def restart(self):
        """Restart the assessment"""
        self.current_question = 0
        self.user_symptoms = []
        self.total_score = 0
        self.show_welcome_screen()
    
    def run(self):  
        self.window.mainloop()


if __name__ == "__main__":  
    app = HeartCheckerGUI()
    app.run()