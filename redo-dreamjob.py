import textwrap  # For fancy text formatting

def print_fancy(text, border_char="*", border_width=30):
    """Prints the given text with a decorative border."""
    border = border_char * border_width
    formatted_text = textwrap.fill(text, width=border_width - 4)
    print(border)
    print(formatted_text)
    print(border)


def main():
    """Prompts user for name, dream job, and inspiration, then displays them in an engaging format."""

    name = input("Enter your name: ")
    dream_job = input("What's your dream job? ")
    inspiration = input("Who or what inspires you to chase this dream? ")

    # Create a border design using a heart symbol 
    heart_border = " ".join(["♥"] * 15)

    print_fancy(f"Greetings, {name.upper()}!", border_char=heart_border)
    print_fancy(f"Your dream job: {dream_job.title()}", border_char=heart_border)
    print_fancy(f"Inspired by: {inspiration}", border_char=heart_border)

    # Additional inspirational message
    inspirational_message = """May your passion for {dream_job} guide you,
and the inspiration from {inspiration} fuel your journey!
Never stop dreaming and chasing your goals.""".format(dream_job=dream_job, inspiration=inspiration)
    print(textwrap.fill(inspirational_message, width=70))


if __name__ == "__main__":
    main()

