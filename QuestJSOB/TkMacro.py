from tkinter import *

class McGrid:

    @staticmethod
    def fill_cell(root, widget, col, row, sticky=N+S+E+W):
        ''' Expand a widget to fill cell upon parent size-change '''
        widget.grid(row=row, column=col, sticky=sticky)
        root.grid(row=row, column=col, sticky=sticky)
        root.grid_columnconfigure(col, weight=1)
        root.grid_rowconfigure(row, weight=1)


class McListbox:

    @staticmethod
    def create(parent_frame):
        ''' Wire-up a Listbox + Scrollbar '''
        sb = Scrollbar(parent_frame, orient="vertical")
        sb.grid(row=0, column=0, padx=3, sticky=NS)
        _item_list = Listbox(parent_frame, height=6, width=100, yscrollcommand=sb.set)
        _item_list.grid(row=0, column=1, sticky=N+E)
        sb.config(command=_item_list.yview)
        return _item_list

    @staticmethod
    def set(list_box, items):
        list_box.delete(0, len(items))
        for ss, item in enumerate(items, 0):
            list_box.insert(ss, item)

    def get_selected(list_box) -> str:
        return list_box.get(list_box.curselection())

class McMenu:
    ''' Make Menu() management a tad easier.
    '''
    @staticmethod
    def enable_item(menubar, tag_name):
        menubar.entryconfig(tag_name, state="normal")

    @staticmethod
    def disable_item(menubar, tag_name):
        menubar.entryconfig(tag_name, state="disabled")

class McText:
    ''' Help the Text() work as in other platforms.
    '''
    @staticmethod
    def has_text(inst):
        text = McText.get(inst).strip()
        if not text:
            return False
        return True

    @staticmethod
    def get(inst) -> str:
        ''' Get text from the Text() Widget '''
        return inst.get("1.0", END)

    @staticmethod
    def put(inst, text) -> None:
        ''' Copy text into the Text() Widget '''
        inst.delete('1.0', END)
        inst.insert('1.0', text)

    @staticmethod
    def clear(inst) -> None:
        ''' Remove text from the Text() Widget '''
        inst.delete('1.0', END)

    @staticmethod
    def unlock(inst):
        inst.config(state=NORMAL)

    @staticmethod
    def lock(inst):
        inst.config(state=DISABLED)

    @staticmethod
    def upl(inst, text):
        McText.unlock(inst)
        McText.put(inst, text)
        McText.lock(inst)