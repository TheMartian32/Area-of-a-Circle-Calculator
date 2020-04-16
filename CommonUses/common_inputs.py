'''
A simple module for a series of commands I use commonly.
'''


class repeat_question():
    def ask_for(self, prompt, error_msg=None, _type=None):
        """ While the desired prompt is not given, it repeats the prompt. """
        while True:
            inp = input(prompt).strip()
            if not inp:
                if error_msg:
                    print(error_msg)
                continue

            if _type:
                try:
                    inp = _type(inp)
                except ValueError:
                    if error_msg:
                        print(error_msg)
                    continue
            return inp


# my first USEFUL and NEEDED module for my code. 4-7-20
# mod on python discord wrote this actually. Other comment was from my code which sorta didnt work.
