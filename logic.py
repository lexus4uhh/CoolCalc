import math

class AppLogic:
    def __init__(self, window):
        self.window = window
        self.safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

    def process_input(self, text):
        text = text.strip()
        if not text:
            return ""

        if text.startswith("/"):
            return self.execute_command(text[1:])
        
        return self.calculate(text)

    def calculate(self, expression):
        expr = expression.replace("^", "**")
        try:
            result = eval(expr, {"__builtins__": {}}, self.safe_dict)
            return str(result)
        except Exception:
            return "Error"

    def execute_command(self, command_text):
        parts = command_text.split()
        cmd = parts[0].lower()
        args = parts[1:]

        try:
            if cmd == "font" and args:
                if args[0] == "reset":
                    size = 12
                else:
                    size = int(args[0])
                self.window.update_font_size(size)
                return f"Font size set to {size}"
            
            elif cmd == "size" and args:
                if args[0] == "reset":
                    w, h = 250, 60
                else:
                    w = int(args[0]) if args[0] != '~' else self.window.width()
                    h = int(args[1]) if args[1] != '~' else self.window.height()
                self.window.resize(w, h)
                return f"Size set to {w}x{h}"
            
            elif cmd == "pos" and args:
                if args[0] == "reset":
                    screen = self.window.screen().geometry()
                    x = screen.width()//2 - self.window.width()//2
                    y = 100
                else:
                    x = int(args[0]) if args[0] != '~' else self.window.x()
                    y = int(args[1]) if args[1] != '~' else self.window.y()
                self.window.move(x, y)
                return f"Position set to ({x}, {y})"
            
            elif cmd == "theme" and args:
                if args[0] == "dark":
                    self.window.update_colors(bg="#2d2d2d", border="#555555", text="#ffffff")
                    return "Dark theme applied"
                elif args[0] == "light":
                    self.window.update_colors(bg="#f0f0f0", border="#767676", text="#333333")
                    return "Light theme applied"
                else:
                    return "Unknown theme"

            return "Unknown command"
        except Exception as e:
            return f"Cmd Error: {e}"