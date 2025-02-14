# -*- coding: utf-8 -*-
"""
演示TraitsUI的各种编辑器
"""
import os
from datetime import time
from enthought.traits.api import *
from enthought.traits.ui.api import *

class Employee(HasTraits):
    name = Unicode(label="姓名") 
    department = Unicode(label="部门")
    salary = Int(label="薪水")
    bonus = Int(label="奖金")
    view = View("name", "department", "salary", "bonus") 

    
class EditorDemoItem(HasTraits):
    code = Code()
    view = View(
        Group(
            Item("item", style="simple", label="simple", width=-300), 
            "_",  
            Item("item", style="custom", label="custom"),
            "_",            
            Item("item", style="text", label="text"),
            "_",
            Item("item", style="readonly", label="readonly"),
        ),
    )


    
class EditorDemo(HasTraits):
    codes = List(Str)
    selected_item = Instance(EditorDemoItem)  
    selected_code = Str 
    view = View(
        HSplit(
            Item("codes", style="custom", show_label=False,
                editor=ListStrEditor(editable=False, selected="selected_code")), 
            Item("selected_item", style="custom", show_label=False),
        ),
        resizable=True,
        width = 800,
        height = 400,
        title="各种编辑器演示"
    )
       
    def _selected_code_changed(self):
        item = EditorDemoItem(code=self.selected_code)
        item.add_trait("item", eval(self.selected_code)) 
        self.selected_item = item



employee = Employee()
demo_list = ["低通", "高通", "带通", "带阻"]

trait_defines ="""
    Array(dtype="int32", shape=(3,3)) 
    Bool(True)
    Button("Click me")
    List(editor=CheckListEditor(values=demo_list))
    Code("print 'hello world'")
    Color("red")
    RGBColor("red")
    Trait(*demo_list)
    Directory(os.getcwd())
    Enum(*demo_list)
    File()
    Font()
    HTML('<b><font color="red" size="40">hello world</font></b>')
    List(Str, demo_list)
    Range(1, 10, 5)
    List(editor=SetEditor(values=demo_list))
    List(demo_list, editor=ListStrEditor())
    Str("hello")
    Password("hello")
    Str("Hello", editor=TitleEditor())
    Tuple(Color("red"), Range(1,4), Str("hello"))
    Instance(EditorDemoItem, employee)    
    Instance(EditorDemoItem, employee, editor=ValueEditor())
    Instance(time, time(), editor=TimeEditor())
"""
demo = EditorDemo()
demo.codes = [s.split("#")[0].strip() for s in trait_defines.split("\n") if s.strip()!=""]
demo.configure_traits()
