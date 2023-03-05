class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content
    
class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ''

    def write(self, string):
        self.content = string

    def save(self):
        with open(self.file, 'w') as file:
            file.write(self.content)
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriteCaretaker:
    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)

if __name__ == '__main__':
    caretaker = FileWriteCaretaker()

    writer = FileWriterUtility("GFC.txt")

    writer.write('first thing which is written')
    print(writer.content + '\n\n')

    caretaker.save(writer)

    writer.write('second thing which is written\n')

    print(writer.content + '\n\n')

    caretaker.undo(writer)
    print(writer.content + '\n\n')