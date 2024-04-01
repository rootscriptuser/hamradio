import json

from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
#from rich.padding import Padding
from rich.rule import Rule
from rich import print
from rich import box
import sys 

# HEADER

# TABLE DV
def tableDV():
    tableD1 = Table(title="DMR 1", box=box.ASCII2, row_styles=["","bold"], border_style="red")
    tableD2 = Table(title="DMR 2", box=box.ASCII2, row_styles=["","bold"], border_style="red")
    with open("./s5rpt-dv.json") as rpt:
        rpt_=rpt.read()
    tableD1.add_column("IN:", style="cyan")
    tableD1.add_column("OUT:", style="sky_blue1")
    tableD1.add_column("LOCATION:", style='green')
    tableD1.add_column("CC", style='gold3')
    tableD2.add_column("IN:", style="cyan")
    tableD2.add_column("OUT:", style="sky_blue1")
    tableD2.add_column("LOCATION:", style='green')
    tableD2.add_column("CC", style='gold3')
    parsed_rpt = json.loads(rpt_)
    no=1
    for rpt in parsed_rpt:
        no=no+1
        if no > 25:
            tableD2.add_row(rpt['IN'],rpt['OUT'],rpt['LOC'],rpt['CC'])
        else:
            tableD1.add_row(rpt['IN'],rpt['OUT'],rpt['LOC'],rpt['CC'])
    return tableD1, tableD2

# TABLE UHF
def tableUHF():
    tableU = Table(title="FM/UHF",box=box.ASCII2,row_styles=["","bold"],border_style="red")

    with open("./s5rpt-uhf.json") as rpt:
        rpt_=rpt.read()

    tableU.add_column("IN:", style="cyan")
    tableU.add_column("OUT:", style="sky_blue1")
    tableU.add_column("LOCATION:", style='green')
    tableU.add_column("CTCSS", style='gold3')

    parsed_rpt = json.loads(rpt_)

    for rpt in parsed_rpt:
        tableU.add_row(rpt['IN'],rpt['OUT'],rpt['LOC'],rpt['CTCSS'])
    return tableU

    # TABLE VHF
def tableVHF():
    tableV = Table(title="FM/VHF", box=box.ASCII2 ,row_styles=["","bold"], border_style="red")

    with open("./s5rpt-vhf.json") as rpt:
        rpt_=rpt.read()


    tableV.add_column("IN:", style="cyan")
    tableV.add_column("OUT:", style="sky_blue1")
    tableV.add_column("LOCATION:", style='green')
    tableV.add_column("CTCSS", style='gold3')

    parsed_rpt = json.loads(rpt_)

    for rpt in parsed_rpt:
        tableV.add_row(rpt['IN'],rpt['OUT'],rpt['LOC'],rpt['CTCSS'])
    return tableV
# LAYOUT 

layout=Layout()

layout.split_column(
    Layout(name="header"),
    Layout(name="main")
)


layout['header'].split_row(
    #(Panel(Text("S5RPT", justify="center", style="bold red on sky_blue1"),border_style="gold3"))
    (Rule(Text("S5RPT", style="bold red"), align="center", characters="=",style="green"))
)
layout['header'].size=3


args = sys.argv[1:]

if args  is None:
	prompt = Prompt.ask("Visualis FM or Digi Voice: [enter fm or dv]: ")

if args[0] =="-fm" or prompt =="fm":
  layout['main'].split_row(
    Layout(tableVHF(), name='VHF'),
    Layout(tableUHF(), name='UHF')
    )
elif args[0] =="-dv" or prompt == "dv":
    tableD1,tableD2 =tableDV()
    layout['main'].split_row(
        Layout(tableD1, name='DV'),
        Layout(tableD2, name='DV')
    )

#print(layout)

# set record=True for saving html
console=Console(width=150, height=55)
#console.print("S5RPT",style=" on white bold red", justify="center")

console.print(layout)
#console.save_html("s5rpt.html")
