from miner.field import Field
from miner.field import Field

class View:
    def __init__(self, field):
        self.field=field # type: miner.field.Field

    def display_field(self):
        for row in self.field.data:
            for cell in row:
                if cell.is_open:
                    if cell.mines_count==Cell.MINE:
                        print('* ', end='')
                    else:
                        print(str(cell.mines_count), end=' ')
                else:
                    print("_ ", end=' ')
            print()

    def get_user_turn(self):
        pass








v=View(12)