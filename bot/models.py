from django.db import models

# Create your models here.
class Clickboard(models.Model):
    #author =
    create_date = models.DateTimeField('date created', auto_now=True)
    name = models.CharField(max_length=25)
    commands = models.TextField()

    def __init__(self):
        self.commands = []

    def __str__(self):
        return self.name

    def add_command(self, command):
        self.commands += command + '\n'
        self.save()

    def edit_command(self, index, new_command):
        commands_list = self.commands.split('\n')
        if index < len(commands_list):
            commands_list[index] = new_command
            self.commands = '\n'.join(commands_list)
            self.save()

    def delete_command(self, index):
        commands_list = self.commands.split('\n')
        if index < len(commands_list):
            del commands_list[index]
            self.commands = '\n'.join(commands_list)
            self.save()

    def search_command(self, index):
        commands_list = self.commands.split('\n')
        if index < len(commands_list):
            return commands_list[index]

    def command_count(self):
        commands_list = self.commands.split('\n')
        return len(commands_list)

# komandy

    def add_title(self, title):
        self.html += f"<title>{' '.join(title)}</title>\n"

    def add_header(self, header):
        level = header[0]
        text = ' '.join(header[1:])
        self.html += f"<h{level}>{text}</h{level}>\n"

    def add_paragraph(self, paragraph):
        text = ' '.join(paragraph)
        self.html += f"<p>{text}</p>\n"

    def add_image(self, image):
        src = image[0]
        alt = ' '.join(image[1:])
        self.html += f"<img src='{src}' alt='{alt}'>\n"

    def add_link(self, link):
        href = link[0]
        text = ' '.join(link[1:])
        self.html += f"<a href='{href}'>{text}</a>\n"

    # builder

    def build_html(self):
        self.html = ""
        commands_list = self.commands.split('\n')
        for commandline in commands_list:
            command = commandline.strip().split()
            if command[0] == "title":
                self.add_title(command[1:])
            elif command[0] == "header":
                self.add_header(command[1:])
            elif command[0] == "paragraph":
                self.add_paragraph(command[1:])
            elif command[0] == "image":
                self.add_image(command[1:])
            elif command[0] == "link":
                self.add_link(command[1:])
            else:
                print(f"Model Clickboard function Build_html. Unknown command: {command} for instance {self.name}")
        return self.html