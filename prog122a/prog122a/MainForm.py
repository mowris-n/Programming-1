﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(621, 279)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 322)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 58)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(457, 322)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 58)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(245, 322)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.HotTrack
        self.ClientSize = System.Drawing.Size(645, 414)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number\t\tSquare\t\tSquare Root"
        self._listBox1.Items.Add(heading)
        
        for num in range(1, 50+1):
            nsqrd = num**2
            nsqrt = math.sqrt(num)
            line = str(num) + "\t\t" + str(nsqrd) + "\t\t" + str(round(nsqrt,4))
            self._listBox1.Items.Add(line)
           

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button2Click(self, sender, e):
        Application.Exit()