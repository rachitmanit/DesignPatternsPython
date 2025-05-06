# Idea is to add a Dynamic decorator over file object by intercepting few methods
# and just let the decorator class work same as file class for remaining methods
class FileWithLogging:
  def __init__(self, file):
    self.file = file

  def writelines(self, strings):
    self.file.writelines(strings)
    print(f'Written {len(strings)} lines to file')

  def __getattr__(self, item):
    return getattr(self.__dict__['file'], item)

  def __setattr__(self, key, value):
    if key == 'file':
        self.__dict__[key] = value
    else:
      setattr(self.__dict__['file'], key, value)

  def __delattr__(self, item):
    delattr(self.file, item)

if __name__ == '__main__':
    f = FileWithLogging(open("hello.txt", 'w'))
    f.writelines(["hello", "world"])
    f.write("\nThis is written without writelines methods call. This uses getattr")
    f.close()